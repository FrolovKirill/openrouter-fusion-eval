#!/usr/bin/env python3
"""
OpenRouter Fusion experiment runner (validated mechanism).

Каждый (конфиг × вопрос):
  - caller qwen3-235b с relay-system-промптом + tool_choice форсит fusion
  - panel/judge заданы в config.CORE_CONFIGS
  - из ответа извлекается структурный JSON (consensus/contradictions/blind_spots/...)
  - фиксируется usage.cost (полная стоимость вызова: panel+judge+web+caller)

Порядок: CORE-конфиги (параллельно по вопросам), затем BASELINE — только если
остался бюджет. Жёсткий стоп по сумме usage.cost (BUDGET_CAP_USD), иммунно к
параллельным сессиям на том же ключе.

Использование:
  set -a; source ../../.env; set +a; python3 runner.py --dry-run        # план + смета, без трат
  set -a; source ../../.env; set +a; python3 runner.py                   # core, потом baseline
  ... python3 runner.py --configs C2_cn_open C3_cn_small                 # только эти конфиги
  ... python3 runner.py --questions 5                                    # первые 5 вопросов
  ... python3 runner.py --cap 10                                         # переопределить budget cap
"""

import argparse
import json
import os
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

import httpx

from config import (
    BASELINE_CONFIGS,
    BUDGET_CAP_USD,
    CALLER_MODEL,
    CONCURRENCY,
    CORE_CONFIGS,
    MAX_RETRIES,
    MAX_TOKENS,
    MAX_TOOL_CALLS,
    OPENROUTER_BASE,
    QUESTIONS_DIR,
    RELAY_SYSTEM,
    RESULTS_DIR,
    RETRY_BACKOFF_S,
    REQUEST_TIMEOUT_S,
    TEMPERATURE,
)

API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://github.com/example/fusion-experiment",
    "X-Title": "Fusion Experiment",
}

_FUSION_KEYS = {"consensus", "contradictions", "unique_insights", "blind_spots", "partial_coverage", "responses"}

# Оценка $/вопрос по конфигам (для резерва бюджета и сметы). Резерв = оценка × множитель,
# с полом — заведомо выше измеренного максимума (C1 макс ~$0.31).
_EST_PER_Q = {
    "C1_west_closed": 0.225, "C2_cn_open": 0.117, "C3_cn_small": 0.045,
    "C5_smartpanel_dumbjudge": 0.108, "C5inv_dumbpanel_smartjudge": 0.060, "C6_echo": 0.074,
    "B_cn": 0.005, "B_west": 0.021,
}
RESERVE_MULT = 1.6      # запас над оценкой
RESERVE_FLOOR = 0.20    # минимальный резерв на вызов

# Потокобезопасный учёт: _spent = фактически завершённое, _reserved = в полёте (оценки).
# Гарантия: _spent + _reserved ≤ cap всегда → итоговый _spent ≤ cap даже с N в полёте.
_spend_lock = threading.Lock()
_spent = 0.0
_reserved = 0.0
_print_lock = threading.Lock()


def _log(msg: str):
    with _print_lock:
        print(msg, flush=True)


def _reserve_for(config_name: str) -> float:
    return max(RESERVE_FLOOR, _EST_PER_Q.get(config_name, 0.20) * RESERVE_MULT)


def _try_reserve(amount: float, cap: float) -> bool:
    """Резервирует amount если влезает в cap. True → можно стартовать вызов."""
    global _reserved
    with _spend_lock:
        if _spent + _reserved + amount > cap:
            return False
        _reserved += amount
        return True


def _settle(reserved_amount: float, actual) -> float:
    """Снимает резерв, добавляет фактическую стоимость. Возвращает суммарно потрачено."""
    global _spent, _reserved
    with _spend_lock:
        _reserved -= reserved_amount
        _spent += float(actual or 0.0)
        return _spent


def _get_spent() -> float:
    with _spend_lock:
        return _spent


# ─── HTTP с ретраями ──────────────────────────────────────────────────────────

def _post_with_retries(payload: dict) -> dict:
    """Возвращает {ok, data|err, http, retries}. Ретраит транзиентные сбои."""
    last_err = None
    for attempt in range(MAX_RETRIES + 1):
        try:
            r = httpx.post(OPENROUTER_BASE, headers=HEADERS, json=payload, timeout=REQUEST_TIMEOUT_S)
            if r.status_code == 200:
                try:
                    data = r.json()
                except json.JSONDecodeError as e:
                    last_err = f"JSONDecode: {e}"  # транзиент (обрыв стрима) → ретрай
                    time.sleep(RETRY_BACKOFF_S * (attempt + 1))
                    continue
                if "choices" not in data:
                    # Ошибочный объект (часто транзиентный "Provider returned error")
                    last_err = f"no choices: {json.dumps(data)[:160]}"
                    time.sleep(RETRY_BACKOFF_S * (attempt + 1))
                    continue
                return {"ok": True, "data": data, "retries": attempt}
            elif r.status_code in (429, 500, 502, 503, 504):
                last_err = f"HTTP {r.status_code}: {r.text[:120]}"
                time.sleep(RETRY_BACKOFF_S * (attempt + 1))
                continue
            else:
                return {"ok": False, "err": f"HTTP {r.status_code}: {r.text[:200]}", "retries": attempt}
        except (httpx.TimeoutException, httpx.TransportError) as e:
            last_err = f"{type(e).__name__}: {str(e)[:100]}"
            time.sleep(RETRY_BACKOFF_S * (attempt + 1))
    return {"ok": False, "err": f"exhausted retries: {last_err}", "retries": MAX_RETRIES}


# ─── Извлечение структуры ─────────────────────────────────────────────────────

def _extract_structure(content: str) -> dict | None:
    """Извлекает структуру из relay-ответа. Устойчив к обрезке хвоста (responses):
    аналитические поля идут ДО responses, поэтому при невалидном JSON обрезаем
    перед "responses" и закрываем объект; иначе — прогрессивно откатываемся."""
    if not content:
        return None
    # прямой парс
    try:
        o = json.loads(content)
        if isinstance(o, dict) and (_FUSION_KEYS & set(o.keys())):
            return o
    except json.JSONDecodeError:
        pass
    # обрезать перед top-level "responses" (объёмное, идёт последним) и закрыть объект
    m = re.search(r',?\s*"responses"\s*:', content)
    if m:
        cut = content[:m.start()].rstrip().rstrip(",")
        for tail in ("}", "]}", '"]}'):
            try:
                o = json.loads(cut + tail)
                if isinstance(o, dict) and (_FUSION_KEYS & set(o.keys())):
                    return o
            except json.JSONDecodeError:
                continue
    # прогрессивный откат по последней целой паре ключ-значение
    for end in range(len(content), 0, -200):
        frag = content[:end].rstrip().rstrip(",")
        for tail in ("}", "]}", '"]}', '"}]}'):
            try:
                o = json.loads(frag + tail)
                if isinstance(o, dict) and len(_FUSION_KEYS & set(o.keys())) >= 3:
                    return o
            except json.JSONDecodeError:
                continue
    return None


# ─── Один вызов ───────────────────────────────────────────────────────────────

def call_fusion(cfg: dict, prompt: str) -> dict:
    tool = {"type": "openrouter:fusion", "parameters": {
        "analysis_models": cfg["panel"], "model": cfg["judge"], "max_tool_calls": MAX_TOOL_CALLS,
    }}
    payload = {
        "model": CALLER_MODEL,
        "messages": [{"role": "system", "content": RELAY_SYSTEM}, {"role": "user", "content": prompt}],
        "tools": [tool], "tool_choice": {"type": "openrouter:fusion"},
        "max_tokens": MAX_TOKENS, "temperature": TEMPERATURE,
    }
    t0 = time.time()
    res = _post_with_retries(payload)
    dt = round(time.time() - t0, 1)
    if not res["ok"]:
        return {"ok": False, "error": res["err"], "latency_s": dt, "retries": res.get("retries", 0), "cost": 0.0}
    data = res["data"]
    msg = data["choices"][0]["message"]
    content = msg.get("content") or ""
    usage = data.get("usage", {})
    structure = _extract_structure(content)
    return {
        "ok": True,
        "cost": usage.get("cost", 0.0) or 0.0,
        "prompt_tokens": usage.get("prompt_tokens"),
        "completion_tokens": usage.get("completion_tokens"),
        "latency_s": dt,
        "retries": res.get("retries", 0),
        "struct_extracted": structure is not None,
        "structure": structure,
        "final_content": content,
    }


def call_single(model: str, prompt: str) -> dict:
    payload = {"model": model, "messages": [{"role": "user", "content": prompt}],
               "max_tokens": 1500, "temperature": TEMPERATURE}
    t0 = time.time()
    res = _post_with_retries(payload)
    dt = round(time.time() - t0, 1)
    if not res["ok"]:
        return {"ok": False, "error": res["err"], "latency_s": dt, "cost": 0.0}
    data = res["data"]
    usage = data.get("usage", {})
    return {
        "ok": True, "cost": usage.get("cost", 0.0) or 0.0,
        "prompt_tokens": usage.get("prompt_tokens"), "completion_tokens": usage.get("completion_tokens"),
        "latency_s": dt, "final_content": data["choices"][0]["message"].get("content", ""),
    }


# ─── Задачи с budget cap ──────────────────────────────────────────────────────

def _run_task(config_name: str, cfg: dict, q: dict, cap: float) -> dict:
    """Выполняет один (конфиг, вопрос). Резервирует бюджет; не стартует если резерв не влезает в cap."""
    base = {"config": config_name, "question_id": q["id"], "block": q["block"], "title": q["title"]}
    reserve = _reserve_for(config_name)
    if not _try_reserve(reserve, cap):
        return {**base, "ok": False, "skipped": True, "error": "budget cap (reserve)", "cost": 0.0}
    if "single" in cfg:
        res = call_single(cfg["single"], q["prompt"])
    else:
        res = call_fusion(cfg, q["prompt"])
    total = _settle(reserve, res.get("cost", 0.0))
    status = "ok" if res.get("ok") else f"ERR {res.get('error','')[:50]}"
    struct = ("✓" if res.get("struct_extracted") else "✗") if "single" not in cfg else "—"
    _log(f"  [{config_name:28} {q['id']:7}] {status:14} ${res.get('cost',0):.4f}  "
         f"{res.get('latency_s')}s  struct={struct}  Σ=${total:.2f}")
    return {**base, **res}


def run_config_group(configs: dict, questions: list, cap: float, concurrency: int) -> list:
    tasks = [(name, cfg, q) for name, cfg in configs.items() for q in questions]
    results = []
    with ThreadPoolExecutor(max_workers=concurrency) as ex:
        futures = [ex.submit(_run_task, name, cfg, q, cap) for name, cfg, q in tasks]
        for fut in as_completed(futures):
            results.append(fut.result())
    return results


# ─── Вопросы ──────────────────────────────────────────────────────────────────

def load_questions(limit: int | None = None) -> list:
    questions = []
    for f in sorted(QUESTIONS_DIR.glob("*.json")):
        questions.extend(json.loads(f.read_text(encoding="utf-8")))
    return questions[:limit] if limit else questions


# ─── Смета (dry-run) ──────────────────────────────────────────────────────────

def print_plan(core: dict, baselines: dict, questions: list, cap: float):
    n = len(questions)
    _log(f"\n=== ПЛАН ({n} вопросов, cap=${cap}) ===")
    total = 0.0
    _log("CORE (выполняется первым):")
    for name, cfg in core.items():
        est = _EST_PER_Q.get(name, 0.1) * n
        total += est
        models = cfg.get("panel", [cfg.get("single", "?")])
        _log(f"  {name:30} ~${est:5.2f}  panel={','.join(m.split('/')[-1] for m in models)} | judge={cfg.get('judge','—').split('/')[-1]}")
    _log(f"  → CORE итого ~${total:.2f}")
    if baselines:
        bt = sum(_EST_PER_Q.get(n_, 0.02) * n for n_ in baselines)
        _log(f"BASELINE (только если останется бюджет): ~${bt:.2f}")
        total += bt
    _log(f"\n  ВСЕГО ~${total:.2f}  (+ретраи/веб разброс ±20%)")


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--configs", nargs="+", help="Только эти core-конфиги")
    ap.add_argument("--questions", type=int, help="Лимит вопросов")
    ap.add_argument("--cap", type=float, default=BUDGET_CAP_USD, help="Budget cap $ (сумма usage.cost)")
    ap.add_argument("--concurrency", type=int, default=CONCURRENCY, help=f"Параллельных вызовов (дефолт {CONCURRENCY})")
    ap.add_argument("--no-baseline", action="store_true", help="Не запускать baseline в конце")
    ap.add_argument("--baseline-only", action="store_true", help="Только baseline-конфиги (B_cn, B_west), по всем вопросам")
    ap.add_argument("--dry-run", action="store_true", help="Показать план и смету, без вызовов")
    args = ap.parse_args()

    questions = load_questions(args.questions)
    if args.baseline_only:
        core = BASELINE_CONFIGS        # гоняем baseline как основную группу (не деприоритизируем)
        baselines = {}
    else:
        core = {k: v for k, v in CORE_CONFIGS.items() if not args.configs or k in args.configs}
        baselines = {} if args.no_baseline else BASELINE_CONFIGS

    if args.dry_run:
        print_plan(core, baselines, questions, args.cap)
        return

    if not API_KEY:
        sys.exit("OPENROUTER_API_KEY не задан (set -a; source ../../.env; set +a)")
    if not core:
        sys.exit(f"Нет конфигов (фильтр: {args.configs})")

    RESULTS_DIR.mkdir(exist_ok=True)
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    _log(f"Run {run_id} | {len(questions)} вопросов × {len(core)} core-конфигов | cap=${args.cap} | caller={CALLER_MODEL}")
    print_plan(core, baselines, questions, args.cap)
    _log("\n=== CORE ===")

    _log(f"concurrency={args.concurrency}")
    t0 = time.time()
    results = run_config_group(core, questions, args.cap, args.concurrency)

    # BASELINE — только если остался бюджет
    if baselines and _get_spent() < args.cap:
        _log(f"\n=== BASELINE (потрачено ${_get_spent():.2f} < cap) ===")
        results += run_config_group(baselines, questions, args.cap, args.concurrency)
    elif baselines:
        _log(f"\n=== BASELINE пропущен: бюджет исчерпан (${_get_spent():.2f}) ===")

    elapsed = round(time.time() - t0)
    total_cost = _get_spent()

    # Сводка по конфигам
    per_config = {}
    for r in results:
        c = per_config.setdefault(r["config"], {"n": 0, "ok": 0, "struct": 0, "cost": 0.0, "skipped": 0})
        c["n"] += 1
        c["cost"] += r.get("cost", 0.0)
        if r.get("skipped"):
            c["skipped"] += 1
        elif r.get("ok"):
            c["ok"] += 1
            if r.get("struct_extracted"):
                c["struct"] += 1

    output = {
        "run_id": run_id, "caller": CALLER_MODEL, "elapsed_s": elapsed,
        "total_cost_usd": round(total_cost, 4), "budget_cap": args.cap,
        "configs": {**core, **baselines}, "per_config": per_config, "results": results,
    }
    out_path = RESULTS_DIR / f"run_{run_id}.json"
    out_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")

    _log(f"\n{'='*64}\nИТОГО потрачено: ${total_cost:.4f} | время {elapsed}s")
    _log(f"{'config':30} {'ok':>6} {'struct':>7} {'cost$':>8}")
    for name, c in per_config.items():
        _log(f"{name:30} {c['ok']}/{c['n']:<4} {c['struct']:>6} {c['cost']:>8.3f}")
    _log(f"\nРезультат → {out_path}")


if __name__ == "__main__":
    main()
