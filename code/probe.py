#!/usr/bin/env python3
"""
Пробник Fusion API. Цель — эмпирически выяснить:
  1. Можно ли форсировать fusion через tool_choice без «умного» caller'а.
  2. Что caller кладёт в arguments forced tool call (переформулирует вопрос или нет).
  3. В каком поле ответа приходит fusion-анализ (consensus/contradictions/...).
  4. Возвращается ли структура за один round-trip или нужен второй запрос.

Запуск (ключ берётся из окружения, не печатается):
  set -a; source .env; set +a; python3 probe.py --check
  set -a; source .env; set +a; python3 probe.py --fusion
"""

import argparse
import json
import os
import sys

import httpx

BASE = "https://openrouter.ai/api/v1"
API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://github.com/example/fusion-experiment",
    "X-Title": "Fusion Probe",
}

# Дешёвые модели для пробы (правим после --check, если ID невалидны)
CALLER = "qwen/qwen3-235b-a22b-2507"
PANEL = ["qwen/qwen-2.5-7b-instruct", "z-ai/glm-4.5-air"]

PROBE_QUESTION = "What are the main trade-offs between nuclear and solar power for grid baseload? Be concise."


def check():
    """Подтвердить auth и показать несколько дешёвых моделей с ценами."""
    r = httpx.get(f"{BASE}/key", headers=HEADERS, timeout=30.0)
    print(f"GET /key → {r.status_code}")
    if r.status_code == 200:
        data = r.json().get("data", {})
        print(f"  label={data.get('label')}  usage=${data.get('usage')}  limit={data.get('limit')}")
    else:
        print(f"  {r.text[:300]}")
        return

    r = httpx.get(f"{BASE}/models", headers=HEADERS, timeout=30.0)
    models = r.json().get("data", [])
    print(f"\nВсего моделей: {len(models)}. Проверяю наличие кандидатов для панели:")
    wanted = [CALLER, *PANEL]
    ids = {m["id"] for m in models}
    for w in wanted:
        print(f"  {'✓' if w in ids else '✗'} {w}")

    print("\nСамые дешёвые не-free chat-модели (по prompt-цене):")
    priced = []
    for m in models:
        p = m.get("pricing", {})
        try:
            pp = float(p.get("prompt", "0"))
            cp = float(p.get("completion", "0"))
        except (TypeError, ValueError):
            continue
        if pp > 0:
            priced.append((pp, cp, m["id"]))
    for pp, cp, mid in sorted(priced)[:15]:
        print(f"  prompt=${pp*1e6:.3f}/M  completion=${cp*1e6:.3f}/M  {mid}")


def fusion_probe():
    """Один forced-fusion вызов. Дамп всей структуры ответа."""
    fusion_tool = {
        "type": "openrouter:fusion",
        "parameters": {
            "analysis_models": PANEL,
            "max_tool_calls": 2,
        },
    }
    payload = {
        "model": CALLER,
        "messages": [{"role": "user", "content": PROBE_QUESTION}],
        "tools": [fusion_tool],
        "tool_choice": "required",
        "max_tokens": 800,
    }
    print(f"POST /chat/completions  caller={CALLER}  panel={PANEL}  tool_choice=required")
    print(f"Вопрос: {PROBE_QUESTION}\n")

    r = httpx.post(f"{BASE}/chat/completions", headers=HEADERS, json=payload, timeout=240.0)
    print(f"HTTP {r.status_code}")
    if r.status_code != 200:
        print(r.text[:2000])
        return

    data = r.json()
    # Полный дамп в файл
    out = os.path.join(os.path.dirname(__file__), "..", "results", "probe_fusion_raw.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Полный ответ → {out}\n")

    # Разбор ключевых полей
    print("─── ВЕРХНЕУРОВНЕВЫЕ КЛЮЧИ ОТВЕТА ───")
    print(" ", list(data.keys()))

    choice = data.get("choices", [{}])[0]
    msg = choice.get("message", {})
    print(f"\n─── choices[0] ───")
    print(f"  finish_reason: {choice.get('finish_reason')}")
    print(f"  message.keys: {list(msg.keys())}")

    print(f"\n─── tool_calls (ЧТО CALLER СГЕНЕРИРОВАЛ) ───")
    tcs = msg.get("tool_calls") or []
    if not tcs:
        print("  НЕТ tool_calls в message")
    for tc in tcs:
        fn = tc.get("function", {})
        print(f"  name: {fn.get('name')}")
        print(f"  arguments (raw): {fn.get('arguments')!r}")

    print(f"\n─── message.content (ФИНАЛЬНЫЙ ОТВЕТ CALLER'А) ───")
    content = msg.get("content")
    print(f"  {(content or '(пусто)')[:500]}")

    print(f"\n─── ПОИСК FUSION-АНАЛИЗА (consensus/contradictions/...) ───")
    found = _find_fusion_fields(data)
    if found:
        for path, keys in found:
            print(f"  найдено в {path}: {keys}")
    else:
        print("  В ответе НЕТ полей fusion-анализа на верхнем уровне.")
        print("  → Возможно, нужен второй round-trip или анализ в annotations/другом поле.")

    print(f"\n─── annotations / прочие нестандартные поля ───")
    for key in ("annotations", "fusion", "metadata", "provider"):
        if key in data:
            print(f"  data.{key}: {json.dumps(data[key], ensure_ascii=False)[:400]}")
    if "annotations" in msg:
        print(f"  message.annotations: {json.dumps(msg['annotations'], ensure_ascii=False)[:600]}")

    print(f"\n─── usage ───")
    print(" ", data.get("usage"))


RELAY_SYSTEM_RAW = (
    "You have access to a multi-model deliberation tool (fusion). "
    "Step 1: call the tool with the user's question. "
    "Step 2: the tool returns a structured analysis with these fields: "
    "consensus, contradictions, unique_insights, blind_spots, partial_coverage, "
    "and responses (each panel model's full answer). "
    "Your ONLY job is to output that structured analysis VERBATIM as a single JSON object. "
    "Do NOT summarize, do NOT add your own opinion, do NOT write your own answer. "
    "Output raw JSON only, nothing else."
)

RELAY_SYSTEM_BASED = (
    "You have access to a multi-model deliberation tool (fusion). "
    "Call the tool with the user's question, then answer STRICTLY based on the tool's "
    "structured result. Do not inject your own knowledge or opinions. "
    "Before your answer, reproduce the tool's contradictions and blind_spots fields verbatim."
)


def relay_probe(mode: str):
    """Caller-проводник: пытаемся вытащить структуру fusion через system-инструкцию."""
    system = RELAY_SYSTEM_RAW if mode == "raw" else RELAY_SYSTEM_BASED
    fusion_tool = {
        "type": "openrouter:fusion",
        "parameters": {"analysis_models": PANEL, "max_tool_calls": 2},
    }
    payload = {
        "model": CALLER,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": PROBE_QUESTION},
        ],
        "tools": [fusion_tool],
        "tool_choice": "required",
        "max_tokens": 2000,
    }
    print(f"RELAY mode={mode}  caller={CALLER}  panel={PANEL}")
    print(f"Вопрос: {PROBE_QUESTION}\n")

    r = httpx.post(f"{BASE}/chat/completions", headers=HEADERS, json=payload, timeout=240.0)
    print(f"HTTP {r.status_code}")
    if r.status_code != 200:
        print(r.text[:2000])
        return
    data = r.json()
    out = os.path.join(os.path.dirname(__file__), "..", "results", f"probe_relay_{mode}.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    content = data["choices"][0]["message"].get("content") or ""
    print(f"─── content ({len(content)} симв) → {out} ───")
    print(content[:2500])

    print("\n─── Маркеры структуры в content ───")
    low = content.lower()
    for w in ["consensus", "contradict", "blind_spot", "unique_insight", "partial_coverage", "responses"]:
        print(f"  {w!r}: {low.count(w)}")
    # Пробуем распарсить как JSON
    parsed = _try_extract_json(content)
    if parsed:
        print(f"\n  ✓ Удалось извлечь JSON с ключами: {sorted(parsed.keys())}")
    else:
        print("\n  ✗ Чистый JSON не извлёкся (проза или смесь)")
    print(f"\nusage: prompt={data['usage'].get('prompt_tokens')}  cost=${data['usage'].get('cost')}")


def _try_extract_json(s: str):
    import re
    # прямой парс
    try:
        o = json.loads(s)
        return o if isinstance(o, dict) else None
    except Exception:
        pass
    # из ```json ... ``` или первой { до последней }
    m = re.search(r"\{.*\}", s, re.DOTALL)
    if m:
        try:
            o = json.loads(m.group(0))
            return o if isinstance(o, dict) else None
        except Exception:
            return None
    return None


def stream_probe():
    """Streaming forced-fusion вызов. Цель — поймать структуру fusion в чанках потока."""
    fusion_tool = {
        "type": "openrouter:fusion",
        "parameters": {"analysis_models": PANEL, "max_tool_calls": 2},
    }
    payload = {
        "model": CALLER,
        "messages": [{"role": "user", "content": PROBE_QUESTION}],
        "tools": [fusion_tool],
        "tool_choice": "required",
        "max_tokens": 800,
        "stream": True,
    }
    print(f"POST /chat/completions (STREAM)  caller={CALLER}  panel={PANEL}")
    print(f"Вопрос: {PROBE_QUESTION}\n")

    raw_lines = []
    chunk_count = 0
    with httpx.stream("POST", f"{BASE}/chat/completions", headers=HEADERS, json=payload, timeout=240.0) as r:
        print(f"HTTP {r.status_code}")
        if r.status_code != 200:
            print(r.read().decode()[:2000])
            return
        for line in r.iter_lines():
            if not line:
                continue
            raw_lines.append(line)
            if line.startswith("data: "):
                chunk_count += 1
                payload_str = line[6:]
                if payload_str.strip() == "[DONE]":
                    continue
                try:
                    obj = json.loads(payload_str)
                except json.JSONDecodeError:
                    continue
                # Ищем любые нестандартные поля в чанке (не choices/usage/id/...)
                delta = obj.get("choices", [{}])[0].get("delta", {})
                extra_keys = set(delta.keys()) - {"role", "content", "reasoning", "tool_calls", "refusal"}
                if extra_keys:
                    print(f"  [chunk {chunk_count}] НЕОБЫЧНЫЕ delta-ключи: {extra_keys}")
                top_extra = set(obj.keys()) - {"id", "object", "created", "model", "provider", "choices", "usage", "system_fingerprint", "service_tier"}
                if top_extra:
                    print(f"  [chunk {chunk_count}] НЕОБЫЧНЫЕ top-ключи: {top_extra} → {json.dumps({k:obj[k] for k in top_extra}, ensure_ascii=False)[:300]}")

    out = os.path.join(os.path.dirname(__file__), "..", "results", "probe_stream_raw.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(raw_lines))
    print(f"\nВсего чанков: {chunk_count}. Сырой поток → {out}")

    blob = "\n".join(raw_lines).lower()
    print("\n─── Поиск маркеров fusion в сыром потоке ───")
    for w in ["consensus", "contradict", "blind_spot", "unique_insight", "partial_coverage", '"responses"', "panel"]:
        print(f"  {w!r}: {blob.count(w)} раз")


_FUSION_KEYS = {"consensus", "contradictions", "unique_insights", "blind_spots", "partial_coverage", "responses"}


def _find_fusion_fields(obj, path="root"):
    """Рекурсивно ищет dict'ы, похожие на fusion-анализ."""
    found = []
    if isinstance(obj, dict):
        hit = _FUSION_KEYS & set(obj.keys())
        if len(hit) >= 2:
            found.append((path, sorted(hit)))
        for k, v in obj.items():
            found.extend(_find_fusion_fields(v, f"{path}.{k}"))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            found.extend(_find_fusion_fields(v, f"{path}[{i}]"))
    return found


if __name__ == "__main__":
    if not API_KEY:
        sys.exit("OPENROUTER_API_KEY не задан в окружении (set -a; source .env; set +a)")
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="Auth + дешёвые модели")
    ap.add_argument("--fusion", action="store_true", help="Один forced-fusion вызов с дампом")
    ap.add_argument("--stream", action="store_true", help="Streaming fusion — ловим структуру в чанках")
    ap.add_argument("--relay", choices=["raw", "based"], help="Caller-проводник: raw=дамп структуры, based=ответ строго по тулу")
    args = ap.parse_args()
    if args.check:
        check()
    elif args.fusion:
        fusion_probe()
    elif args.stream:
        stream_probe()
    elif args.relay:
        relay_probe(args.relay)
    else:
        print("Укажи --check, --fusion, --stream или --relay raw|based")
