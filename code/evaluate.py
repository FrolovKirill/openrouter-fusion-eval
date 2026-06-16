#!/usr/bin/env python3
"""
Метрики по результатам Fusion-эксперимента (новый плоский формат runner.py).

Структурные метрики — БЕЗ API (бесплатно). Опционально:
  --grade  факто-точность (LLM-judge сверяет consensus с expected_answer)
  --ab     попарное качество конфигов (LLM-judge)

Использование:
  python evaluate.py results/run_YYYYMMDD_HHMMSS.json
  set -a; source ../../.env; set +a; python evaluate.py results/run_*.json --grade
"""

import argparse
import json
import os
import sys
import time
from collections import defaultdict
from pathlib import Path

import httpx

from config import OPENROUTER_BASE

API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
GRADER_MODEL = "qwen/qwen3-235b-a22b-2507"  # дешёвый, для grade/ab

ANALYSIS_FIELDS = ["consensus", "contradictions", "unique_insights", "blind_spots", "partial_coverage"]


# ─── Структурные метрики (без API) ────────────────────────────────────────────

def _field_items(val) -> int:
    """Сколько осмысленных элементов в поле (list → len непустых; str → 1 если длинная)."""
    if isinstance(val, list):
        return sum(1 for v in val if str(v).strip())
    if isinstance(val, str):
        return 1 if len(val.strip()) >= 30 else 0
    if isinstance(val, dict):
        return len(val)
    return 0


def structural_metrics(rows: list) -> dict:
    """rows = результаты одного конфига (fusion)."""
    n = len(rows)
    ok = [r for r in rows if r.get("ok") and not r.get("skipped")]
    struct = [r for r in ok if r.get("struct_extracted") and r.get("structure")]
    if not struct:
        return {"n": n, "ok": len(ok), "struct": 0}

    field_present = defaultdict(int)   # в скольких вопросах поле непусто
    field_items = defaultdict(int)     # суммарно элементов
    for r in struct:
        s = r["structure"]
        for f in ANALYSIS_FIELDS:
            c = _field_items(s.get(f))
            if c > 0:
                field_present[f] += 1
            field_items[f] += c

    m = len(struct)
    cov = sum(field_present[f] for f in ["consensus", "contradictions", "unique_insights", "blind_spots"]) / (4 * m)
    return {
        "n": n, "ok": len(ok), "struct": m,
        "avg_cost": round(sum(r.get("cost", 0) for r in rows) / max(n, 1), 4),
        "total_cost": round(sum(r.get("cost", 0) for r in rows), 3),
        "avg_latency": round(sum(r.get("latency_s", 0) for r in ok) / max(len(ok), 1)),
        "coverage": round(cov, 3),
        "contradiction_rate": round(field_present["contradictions"] / m, 3),
        "blind_spot_rate": round(field_present["blind_spots"] / m, 3),
        "unique_rate": round(field_present["unique_insights"] / m, 3),
        "avg_contradictions": round(field_items["contradictions"] / m, 2),
        "avg_blind_spots": round(field_items["blind_spots"] / m, 2),
        "avg_consensus": round(field_items["consensus"] / m, 2),
    }


# ─── LLM-judge: факто-точность ────────────────────────────────────────────────

GRADE_PROMPT = """Вопрос (факт): {q}

Эталонный ответ: {expected}

Кандидат (consensus из мультимодельного совещания): {consensus}

Кандидат фактически верен и согласуется с эталоном? Ответь одним словом: ДА, НЕТ или ЧАСТИЧНО.
Затем через пробел одно короткое предложение почему."""


def _judge(prompt: str, max_tokens: int = 120) -> str:
    try:
        r = httpx.post(OPENROUTER_BASE, headers=HEADERS, json={
            "model": GRADER_MODEL, "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens, "temperature": 0,
        }, timeout=120.0)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"ERR {str(e)[:60]}"


def grade_factual(results: list) -> dict:
    """Для факто-вопросов сверяет consensus с expected_answer. По конфигам."""
    by_cfg = defaultdict(lambda: {"correct": 0, "partial": 0, "wrong": 0, "n": 0})
    fac = [r for r in results if r.get("block") == "factual" and r.get("ok") and r.get("structure")]
    print(f"\nFacto-grade: {len(fac)} (конфиг×вопрос) через {GRADER_MODEL}...")
    for r in fac:
        expected = _expected.get(r["question_id"])
        if not expected:
            continue
        cons = r["structure"].get("consensus")
        cons_txt = json.dumps(cons, ensure_ascii=False)[:1500] if cons else "(пусто)"
        verdict = _judge(GRADE_PROMPT.format(q=r["title"], expected=expected, consensus=cons_txt))
        w = verdict.split()[0].upper() if verdict else "?"
        s = by_cfg[r["config"]]
        s["n"] += 1
        if w.startswith("ДА"):
            s["correct"] += 1
        elif w.startswith("ЧАСТИ"):
            s["partial"] += 1
        else:
            s["wrong"] += 1
        time.sleep(0.5)
    return dict(by_cfg)


# ─── Отчёт ────────────────────────────────────────────────────────────────────

def print_report(run: dict, metrics: dict, grades: dict | None):
    print(f"\n{'='*88}")
    print(f"Run {run['run_id']} | потрачено ${run.get('total_cost_usd')} | время {run.get('elapsed_s')}s | caller {run['caller']}")
    print(f"\n{'config':32} {'struct':>7} {'cov':>5} {'contr':>6} {'blind':>6} {'uniq':>5} "
          f"{'#contr':>7} {'#blind':>7} {'$avg':>7} {'sec':>5}")
    print("─" * 100)
    order = list(run.get("configs", {}).keys())
    for cfg in order:
        m = metrics.get(cfg)
        if not m or m.get("struct", 0) == 0:
            print(f"{cfg:32} {'нет структуры / baseline':>30}")
            continue
        print(f"{cfg:32} {m['struct']:>3}/{m['n']:<3} {m['coverage']:>5.0%} "
              f"{m['contradiction_rate']:>6.0%} {m['blind_spot_rate']:>6.0%} {m['unique_rate']:>5.0%} "
              f"{m['avg_contradictions']:>7.1f} {m['avg_blind_spots']:>7.1f} {m['avg_cost']:>7.3f} {m['avg_latency']:>5}")

    if grades:
        print(f"\n─── Факто-точность (consensus vs эталон) ───")
        print(f"{'config':32} {'верно':>6} {'части':>6} {'невер':>6} {'n':>4}  accuracy")
        for cfg in order:
            g = grades.get(cfg)
            if not g or g["n"] == 0:
                continue
            acc = (g["correct"] + 0.5 * g["partial"]) / g["n"]
            print(f"{cfg:32} {g['correct']:>6} {g['partial']:>6} {g['wrong']:>6} {g['n']:>4}  {acc:.0%}")


# ─── Main ─────────────────────────────────────────────────────────────────────

_expected = {}


def main():
    global _expected
    ap = argparse.ArgumentParser()
    ap.add_argument("results_file")
    ap.add_argument("--grade", action="store_true", help="Факто-точность через LLM-judge")
    args = ap.parse_args()

    path = Path(args.results_file)
    if not path.exists():
        sys.exit(f"Нет файла: {path}")
    run = json.loads(path.read_text(encoding="utf-8"))

    # эталоны факто-вопросов
    qdir = Path(__file__).parent.parent / "questions"  # questions/ в корне fusion/, код в code/
    for f in qdir.glob("*.json"):
        for q in json.loads(f.read_text(encoding="utf-8")):
            if q.get("expected_answer"):
                _expected[q["id"]] = q["expected_answer"]

    by_cfg = defaultdict(list)
    for r in run["results"]:
        by_cfg[r["config"]].append(r)
    metrics = {cfg: structural_metrics(rows) for cfg, rows in by_cfg.items()}

    grades = None
    if args.grade:
        if not API_KEY:
            sys.exit("OPENROUTER_API_KEY нужен для --grade")
        grades = grade_factual(run["results"])

    print_report(run, metrics, grades)

    out = path.with_suffix(".metrics.json")
    out.write_text(json.dumps({"metrics": metrics, "grades": grades}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nМетрики → {out}")


if __name__ == "__main__":
    main()
