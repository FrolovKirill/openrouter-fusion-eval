#!/usr/bin/env python3
"""
Измеряет РЕАЛЬНУЮ стоимость relay-fusion вызова по архетипам конфигов.
Один открытый вопрос (дорогой случай), temp 0, валидированный механизм
(форс именно fusion + relay-system-промпт → структура в content).

Запуск:
  set -a; source ../../.env; set +a; python3 measure_cost.py
"""

import json
import os
import time

import httpx

BASE = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.environ["OPENROUTER_API_KEY"]
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

CALLER = "qwen/qwen3-235b-a22b-2507"

RELAY = (
    "You have access to a multi-model deliberation tool (fusion). Call it with the user's question, "
    "then output its structured result VERBATIM as one JSON object with fields consensus, contradictions, "
    "unique_insights, blind_spots, partial_coverage, responses. No own opinion, raw JSON only."
)

# Открытый вопрос — дорогой случай (длинные ответы панели). Факто-вопросы будут дешевле.
QUESTION = (
    "Should nuclear power be a central part of the global energy transition, or should resources "
    "focus on renewables and storage? Make the strongest case for each side and give your assessment."
)

# Архетипы. web = max_tool_calls (>=1 обязательно — 0 ломает fusion).
# Меряем минимальный web=1. Уже известно: web=4 для C2 = $0.172; B-west один = $0.021.
CONFIGS = [
    {"name": "C1 West-closed (web1)", "panel": ["openai/gpt-5.2", "google/gemini-3.1-pro-preview", "x-ai/grok-4.3"], "judge": "openai/gpt-5.2", "web": 1},
    {"name": "C2 CN-open (web1)", "panel": ["deepseek/deepseek-v4-pro", "z-ai/glm-5.1", "moonshotai/kimi-k2.6"], "judge": "qwen/qwen3-235b-a22b-2507", "web": 1},
    {"name": "C3 CN-small (web1)", "panel": ["qwen/qwen3.6-27b", "z-ai/glm-4.7-flash", "qwen/qwen3-32b"], "judge": "qwen/qwen3-32b", "web": 1},
    {"name": "C6 echo qwen235 x3 (web1)", "panel": ["qwen/qwen3-235b-a22b-2507"] * 3, "judge": "qwen/qwen3-235b-a22b-2507", "web": 1},
]


def run_single(model: str) -> dict:
    t0 = time.time()
    r = httpx.post(BASE, headers=HEADERS, json={
        "model": model,
        "messages": [{"role": "user", "content": QUESTION}],
        "max_tokens": 1500, "temperature": 0,
    }, timeout=300.0)
    dt = time.time() - t0
    if r.status_code != 200:
        return {"ok": False, "err": f"HTTP {r.status_code}: {r.text[:120]}", "dt": dt}
    d = r.json()
    u = d.get("usage", {})
    return {"ok": True, "cost": u.get("cost"), "ptok": u.get("prompt_tokens"), "ctok": u.get("completion_tokens"),
            "dt": dt, "struct": False, "clen": len(d["choices"][0]["message"].get("content") or "")}


def run_fusion(cfg: dict) -> dict:
    tool = {"type": "openrouter:fusion", "parameters": {"analysis_models": cfg["panel"], "model": cfg["judge"], "max_tool_calls": cfg["web"]}}
    t0 = time.time()
    r = httpx.post(BASE, headers=HEADERS, json={
        "model": CALLER,
        "messages": [{"role": "system", "content": RELAY}, {"role": "user", "content": QUESTION}],
        "tools": [tool], "tool_choice": {"type": "openrouter:fusion"},
        "max_tokens": 3000, "temperature": 0,
    }, timeout=300.0)
    dt = time.time() - t0
    if r.status_code != 200:
        return {"ok": False, "err": f"HTTP {r.status_code}: {r.text[:200]}", "dt": dt}
    d = r.json()
    if "choices" not in d:
        return {"ok": False, "err": f"NO choices: {json.dumps(d, ensure_ascii=False)[:250]}", "dt": dt}
    u = d.get("usage", {})
    content = d["choices"][0]["message"].get("content") or ""
    struct = "consensus" in content.lower() and "contradict" in content.lower()
    return {"ok": True, "cost": u.get("cost"), "ptok": u.get("prompt_tokens"), "ctok": u.get("completion_tokens"),
            "dt": dt, "struct": struct, "clen": len(content)}


def main():
    print(f"Вопрос (открытый, дорогой случай): {QUESTION[:70]}...\n")
    print(f"{'config':34} {'cost$':>9} {'ptok':>7} {'ctok':>7} {'sec':>5} {'struct':>7} {'clen':>6}")
    print("─" * 80)
    rows = []
    for cfg in CONFIGS:
        try:
            res = run_single(cfg["single"]) if "single" in cfg else run_fusion(cfg)
        except Exception as e:
            res = {"ok": False, "err": f"EXC {type(e).__name__}: {str(e)[:150]}"}
        rows.append((cfg["name"], res))
        if res["ok"]:
            print(f"{cfg['name']:34} {res['cost'] or 0:>9.5f} {res['ptok']:>7} {res['ctok']:>7} {res['dt']:>5.0f} "
                  f"{'✓' if res['struct'] else ('—' if 'single' in cfg else '✗'):>7} {res['clen']:>6}", flush=True)
        else:
            print(f"{cfg['name']:34} ERR {res['err']}", flush=True)
        time.sleep(2)

    # Экстраполяция на 23 вопроса. Факто-вопросы дешевле (короткие ответы) — берём коэф 0.55.
    print("\n─── ЭКСТРАПОЛЯЦИЯ на 23 вопроса (13 факто ~0.4x + 10 открытых ~1.0x ≈ 0.74x от open-цены) ───")
    FACTOR = 0.74 * 23
    total = 0.0
    for name, res in rows:
        if res["ok"] and res.get("cost"):
            est = res["cost"] * FACTOR
            total += est
            print(f"  {name:34} ~${est:.2f}")
    print(f"\n  ИТОГО матрица (один прогон каждого конфига): ~${total:.2f}")
    print(f"  + A/B judge eval (дешёвая модель) ~$0.5")
    print(f"  Ключ: осталось ~$8")


if __name__ == "__main__":
    main()
