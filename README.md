# OpenRouter Fusion — evaluation

A small experiment to test OpenRouter's **Fusion** server-tool: a panel of models answers in parallel (with mandatory web search), a judge compares them, and you get back a structured analysis (`consensus` / `contradictions` / `blind_spots` / `unique_insights`).
Feature docs: https://openrouter.ai/docs/guides/features/server-tools/fusion

## What was tested

**23 questions in 3 tiers:** scientific (proposal critique), contested (open debates), factual (verifiable, with reference answers — Monty Hall → Therac-25).

**Models in several tiers** (6 fusion configs + 2 single-model baselines, 184 calls total):
- closed Western frontier — gpt-5.2 / gemini-3.1-pro / grok-4.3
- open Chinese frontier — deepseek-v4-pro / glm-5.1 / kimi-k2.6
- small open models, and an **echo control** (one model ×3, zero diversity)
- single-model baselines (no fusion)

The 2×2 axis ("panel intelligence × judge intelligence") isolates whether the panel or the judge drives quality.

## Results (short)

- **Fusion is effectively one smart, web-grounded call wrapped in structure by a judge** — not real multi-model deliberation.
- **16–68× the cost** and **9–15× the latency** of a single model.
- On open/reasoning questions its added value is **marginal** (a single frontier call sufficed every time); on facts it only "won" when a baseline returned an empty answer (i.e. redundancy, not knowledge).
- **The panel is largely theater:** the echo control (one model ×3) matches diverse panels, and per-model attribution in the output is frequently fabricated by the relay/judge.
- **Worth it narrowly:** offline adversarial fact-checking / redundancy *with a smart judge*. Otherwise a single frontier call + web search + one self-critique pass reproduces ~80–90% of the value far cheaper.

Full write-up: [`analysis/REPORT_EN.md`](analysis/REPORT_EN.md) (English) · [`analysis/REPORT.md`](analysis/REPORT.md) (Russian). Reproduction scripts in [`code/`](code/), questions in [`questions/`](questions/).

> The report in `analysis/` was produced via a **Claude Code multi-agent Workflow** (parallel sub-agents: fact-graders, deep-reads, judge-influence audits, thematic synthesis, and adversarial verification on top of the deterministic metrics).

---

This could be benchmarked much more and much better — more runs for variance, fresh/post-cutoff questions, a proper "single model + web" arm to isolate the web effect, human grading, etc. But I've already spent ~$20 of API credit on it and don't feel like spending more. Take it as directional, not gospel. PRs welcome.
