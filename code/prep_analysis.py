#!/usr/bin/env python3
"""
Подготовка производных данных для глубокого анализа Fusion-эксперимента субагентами.
Детерминированно (без LLM) нарезает большой run_*.json в компактные артефакты:

  analysis/data/quant.json          — все числовые метрики (cost/latency/tokens/structural/grades)
  analysis/data/q_<qid>.md          — per-question: анализ всех 6 fusion-конфигов + 2 baseline (без responses)
  analysis/data/resp_<qid>.md       — per-question: сырые panel responses + judge-синтез (для judge-influence)
  analysis/data/INDEX.md            — легенда конфигов + список вопросов

Запуск:  python3 prep_analysis.py
"""
import json
import statistics
from collections import defaultdict
from pathlib import Path

CODE = Path(__file__).parent
FUSION = CODE.parent
RUN = FUSION / "results" / "run_20260615_202451.json"
METRICS = FUSION / "results" / "run_20260615_202451.metrics.json"
OUT = FUSION / "analysis" / "data"
OUT.mkdir(parents=True, exist_ok=True)

ANALYSIS_FIELDS = ["consensus", "contradictions", "unique_insights", "blind_spots", "partial_coverage"]
FUSION_CONFIGS = ["C1_west_closed", "C2_cn_open", "C5_smartpanel_dumbjudge",
                  "C5inv_dumbpanel_smartjudge", "C6_echo", "C3_cn_small"]
BASELINES = ["B_cn", "B_west"]
ANS_CAP = 4500  # обрезка одного panel-ответа в resp-файле

run = json.loads(RUN.read_text(encoding="utf-8"))
metrics = json.loads(METRICS.read_text(encoding="utf-8"))
configs = run["configs"]

# index results: (config, qid) -> row
by_cq = {(r["config"], r["question_id"]): r for r in run["results"]}
by_q = defaultdict(dict)
for r in run["results"]:
    by_q[r["question_id"]][r["config"]] = r

# questions metadata
qmeta = {}
for f in sorted((FUSION / "questions").glob("*.json")):
    for q in json.loads(f.read_text(encoding="utf-8")):
        qmeta[q["id"]] = q
qids = sorted(qmeta.keys())


def fmt_field(v) -> str:
    """Любое значение fusion-поля -> markdown-блок."""
    if v is None or v == "" or v == []:
        return "  _(пусто)_"
    if isinstance(v, str):
        return "  " + v.strip()
    if isinstance(v, dict):
        return "\n".join(f"  - **{k}**: {json.dumps(val, ensure_ascii=False) if not isinstance(val,str) else val}" for k, val in v.items())
    if isinstance(v, list):
        lines = []
        for item in v:
            if isinstance(item, str):
                lines.append(f"  - {item.strip()}")
            elif isinstance(item, dict):
                lines.append("  - " + json.dumps(item, ensure_ascii=False))
            else:
                lines.append(f"  - {item}")
        return "\n".join(lines)
    return f"  {v}"


# ─── per-question analysis files ────────────────────────────────────────────────
for qid in qids:
    q = qmeta[qid]
    parts = [f"# {qid} — {q['title']}  [block: {q['block']}", ]
    parts = []
    parts.append(f"# {qid} — {q['title']}")
    parts.append(f"**Block:** {q['block']}" + (f"  |  **difficulty:** {q.get('difficulty')}" if q.get("difficulty") else ""))
    parts.append(f"\n**Prompt:**\n{q['prompt']}")
    if q.get("expected_answer"):
        parts.append(f"\n**Expected answer (эталон):**\n{q['expected_answer']}")
    parts.append("\n---\n## FUSION-конфиги (judge-анализ; responses вынесены в resp_*.md)\n")
    for cfg in FUSION_CONFIGS:
        r = by_q[qid].get(cfg)
        if not r:
            continue
        cmeta = configs.get(cfg, {})
        panel = ", ".join(m.split("/")[-1] for m in cmeta.get("panel", []))
        judge = (cmeta.get("judge") or "").split("/")[-1]
        s = r.get("structure") or {}
        parts.append(f"### {cfg}")
        parts.append(f"_{cmeta.get('note','')}_  \npanel=[{panel}] | judge={judge} | "
                     f"cost=${r.get('cost',0):.4f} | {r.get('latency_s')}s | "
                     f"ptok={r.get('prompt_tokens')} ctok={r.get('completion_tokens')} | retries={r.get('retries',0)}")
        for f in ANALYSIS_FIELDS:
            parts.append(f"\n**{f}:**\n{fmt_field(s.get(f))}")
        parts.append("")
    parts.append("\n---\n## BASELINE (одиночная модель, без fusion)\n")
    for cfg in BASELINES:
        r = by_q[qid].get(cfg)
        if not r:
            continue
        model = (configs.get(cfg, {}).get("single") or "").split("/")[-1]
        ans = (r.get("final_content") or "").strip() or "_(пустой ответ)_"
        parts.append(f"### {cfg}  (model={model} | cost=${r.get('cost',0):.4f} | {r.get('latency_s')}s)")
        parts.append(ans)
        parts.append("")
    (OUT / f"q_{qid}.md").write_text("\n".join(parts), encoding="utf-8")


# ─── per-question raw responses (judge-influence) ────────────────────────────────
for qid in qids:
    q = qmeta[qid]
    parts = [f"# {qid} — {q['title']}  (raw panel responses + judge-синтез)",
             f"**Prompt:** {q['prompt']}",
             "\n> ВНИМАНИЕ: responses релеятся caller'ом (qwen3-235b), не verbatim — "
             "атрибуция модели местами заменена ролью ('Panel Model A'); текст ответа реальный.\n"]
    for cfg in FUSION_CONFIGS:
        r = by_q[qid].get(cfg)
        if not r:
            continue
        s = r.get("structure") or {}
        resp = s.get("responses")
        cmeta = configs.get(cfg, {})
        panel = ", ".join(m.split("/")[-1] for m in cmeta.get("panel", []))
        judge = (cmeta.get("judge") or "").split("/")[-1]
        parts.append(f"\n{'='*70}\n## {cfg}  (panel=[{panel}] | judge={judge})")
        parts.append("\n### JUDGE-СИНТЕЗ (что судья извлёк):")
        parts.append(f"**consensus:** {fmt_field(s.get('consensus'))}")
        parts.append(f"**contradictions:** \n{fmt_field(s.get('contradictions'))}")
        parts.append(f"**unique_insights:** \n{fmt_field(s.get('unique_insights'))}")
        parts.append(f"**blind_spots:** \n{fmt_field(s.get('blind_spots'))}")
        parts.append("\n### RAW PANEL RESPONSES (что панель реально сказала):")
        if isinstance(resp, list) and resp:
            for i, item in enumerate(resp):
                if not isinstance(item, dict):
                    continue
                m = item.get("model", f"#{i}")
                a = str(item.get("answer") or item.get("content") or "").strip()
                if len(a) > ANS_CAP:
                    a = a[:ANS_CAP] + f"\n…[обрезано, всего {len(a)} симв]"
                parts.append(f"\n**[{m}]:**\n{a or '_(пусто)_'}")
        else:
            parts.append("_(responses отсутствуют для этого вопроса/конфига)_")
    (OUT / f"resp_{qid}.md").write_text("\n".join(parts), encoding="utf-8")


# ─── quant.json: все детерминированные числа ─────────────────────────────────────
def stats(vals):
    vals = [v for v in vals if v is not None]
    if not vals:
        return None
    return {"n": len(vals), "sum": round(sum(vals), 4), "mean": round(statistics.mean(vals), 4),
            "median": round(statistics.median(vals), 4), "min": round(min(vals), 4), "max": round(max(vals), 4)}


quant = {"run_id": run["run_id"], "caller": run["caller"], "total_cost_usd": run["total_cost_usd"],
         "elapsed_s": run["elapsed_s"], "n_questions": len(qids), "configs": {}, "legend": {}}

for cfg in FUSION_CONFIGS + BASELINES:
    rows = [r for r in run["results"] if r["config"] == cfg]
    cmeta = configs.get(cfg, {})
    quant["legend"][cfg] = {
        "panel": cmeta.get("panel"), "judge": cmeta.get("judge"),
        "single": cmeta.get("single"), "note": cmeta.get("note"),
    }
    costs = [r.get("cost", 0) for r in rows]
    lats = [r.get("latency_s") for r in rows if r.get("latency_s")]
    ptok = [r.get("prompt_tokens") for r in rows if r.get("prompt_tokens")]
    ctok = [r.get("completion_tokens") for r in rows if r.get("completion_tokens")]
    retries = sum(r.get("retries", 0) or 0 for r in rows)
    # per-block cost
    block_cost = defaultdict(list)
    for r in rows:
        block_cost[r["block"]].append(r.get("cost", 0))
    entry = {
        "cost": stats(costs), "latency_s": stats(lats),
        "prompt_tokens": stats(ptok), "completion_tokens": stats(ctok),
        "retries_total": retries,
        "cost_per_block": {b: round(sum(v) / len(v), 4) for b, v in block_cost.items()},
        "struct_extracted": sum(1 for r in rows if r.get("struct_extracted")),
        "responses_present": sum(1 for r in rows if (r.get("structure") or {}).get("responses")),
    }
    # structural + grades из metrics.json
    m = metrics.get("metrics", {}).get(cfg)
    if m and m.get("struct", 0) > 0:
        entry["structural"] = {k: m.get(k) for k in
                               ["coverage", "contradiction_rate", "blind_spot_rate", "unique_rate",
                                "avg_contradictions", "avg_blind_spots", "avg_consensus"]}
    g = (metrics.get("grades") or {}).get(cfg)
    if g:
        acc = (g["correct"] + 0.5 * g["partial"]) / g["n"] if g["n"] else None
        entry["factual_grade"] = {**g, "accuracy": round(acc, 3) if acc is not None else None}
    quant["configs"][cfg] = entry

# cost multipliers vs baselines
b_cn = quant["configs"]["B_cn"]["cost"]["mean"]
b_west = quant["configs"]["B_west"]["cost"]["mean"]
quant["cost_multipliers"] = {}
for cfg in FUSION_CONFIGS:
    avg = quant["configs"][cfg]["cost"]["mean"]
    quant["cost_multipliers"][cfg] = {
        "avg_cost_per_q": avg,
        "x_vs_B_cn": round(avg / b_cn, 1) if b_cn else None,
        "x_vs_B_west": round(avg / b_west, 1) if b_west else None,
    }

# cost per structural unit (стоимость за единицу "ценности")
quant["cost_per_unit"] = {}
for cfg in FUSION_CONFIGS:
    e = quant["configs"][cfg]
    s = e.get("structural")
    if not s:
        continue
    units = (s["avg_contradictions"] or 0) + (s["avg_blind_spots"] or 0) + \
            (s.get("avg_consensus") or 0)
    quant["cost_per_unit"][cfg] = {
        "avg_cost": e["cost"]["mean"],
        "units_per_q (contr+blind+consensus)": round(units, 2),
        "cost_per_unit": round(e["cost"]["mean"] / units, 4) if units else None,
        "cost_per_contradiction": round(e["cost"]["mean"] / s["avg_contradictions"], 4) if s["avg_contradictions"] else None,
        "cost_per_blind_spot": round(e["cost"]["mean"] / s["avg_blind_spots"], 4) if s["avg_blind_spots"] else None,
    }

(OUT / "quant.json").write_text(json.dumps(quant, ensure_ascii=False, indent=2), encoding="utf-8")

# ─── INDEX.md ────────────────────────────────────────────────────────────────────
idx = ["# Fusion-эксперимент — индекс данных для анализа\n",
       "## Легенда конфигов\n"]
for cfg in FUSION_CONFIGS + BASELINES:
    cm = configs.get(cfg, {})
    if cm.get("single"):
        idx.append(f"- **{cfg}**: single={cm['single']} — {cm.get('note','')}")
    else:
        idx.append(f"- **{cfg}**: panel=[{', '.join(cm.get('panel',[]))}] | judge={cm.get('judge')} — {cm.get('note','')}")
idx.append("\n## Вопросы (23)\n")
for qid in qids:
    q = qmeta[qid]
    idx.append(f"- **{qid}** [{q['block']}{'/'+q['difficulty'] if q.get('difficulty') else ''}]: {q['title']}")
idx.append("\n## Файлы\n- `quant.json` — числа\n- `q_<qid>.md` — анализ всех конфигов по вопросу\n- `resp_<qid>.md` — сырые panel responses + judge-синтез")
(OUT / "INDEX.md").write_text("\n".join(idx), encoding="utf-8")

# sizes report
files = sorted(OUT.glob("*"))
print(f"Готово: {len(files)} файлов в {OUT}")
for f in files:
    print(f"  {f.name:22} {f.stat().st_size:>8} B")
print(f"\nИтого размер: {sum(f.stat().st_size for f in files)//1024} KB")
