# OpenRouter Fusion — Deep-Dive Experiment Analysis

> Run `run_20260615_202451`: 6 fusion configs × 23 questions + 2 single-model baselines = 184 calls, $14.73, 56 min.
> Analysis built by a multi-agent workflow (37 sub-agents: 13 fact-graders on Sonnet, 10 deep-reads + 5 judge audits + 4 thematic + 4 adversarial skeptics on Opus) on top of deterministic metrics. Date: 2026-06-16.

---

## 0. TL;DR

**Fusion is not "a council of multiple models." It is effectively a single smart call with mandatory web search, wrapped by a judge into a structured output (consensus/contradictions/blind_spots) — at 16–68× the cost and 9–15× the latency of a single model/baseline.** The experiment demonstrates this from three independent angles, and the conclusion held up under adversarial verification:

1. **Cost/latency (rock-solid, deterministic data):** $0.047–0.192 per question vs. $0.003 (deepseek solo) / $0.012 (gpt-5.2 solo). Average latency 231–376s vs. ~22s, tails up to **1248s**. For synchronous/interactive scenarios with second-level SLAs — **ruled out**.
2. **Marginal value per single question.** All 10 open questions received a verdict of `marginal_value` and `single_model_suffices=true`: the best fusion adds 1–3 web-grounded facts and occasionally one error catch by the judge on top of an answer a single frontier model already delivers. On factual questions fusion "won" strictly **2 times out of 13** (fac-08, fac-12) — and in both cases only because the baseline returned an **empty/incorrect** answer (reliability, not knowledge superiority).
3. **The panel is largely decorative, provenance is unreliable.** Echo control (one model ×3) produces structure comparable to diverse panels. Attribution of "who said what" is massively fabricated by the relay/caller and judge (phantom models `gpt-4o`/`claude-3-opus`/`Model-A/B/C`, the `evidence` voice = the judge's own knowledge). **`consensus`/`contradictions` cannot be presented as proof of multi-model agreement.**

**What Fusion actually buys (narrow, but real):** (a) **redundancy** against an empty/failed call from a single model; (b) **adversarial fact-check** by a smart judge with live web (caught a retracted paper, fabricated numbers, hallucinated names); (c) **web-grounding** of fresh empirical anchors. All three can be reproduced more cheaply: **one frontier call with web search enabled + an optional self-critique pass** — ~80–90% of the value at 10–65× lower cost and ~30s instead of minutes.

**Model availability:** in environments where closed Western frontier models are unavailable or restricted (geo-blocks, open-weights requirements), config **C1 (gpt-5.2/gemini/grok) is non-operational**. There, the only viable "council" is **C2 (open weights: deepseek-v4-pro/glm-5.1/kimi-k2.6 + judge qwen3-235b, $0.122/q)** — and it is also cheaper than C1.

---

## 1. What is Fusion (per OpenRouter documentation)

Fusion is a server-side tool: a caller model decides that a question benefits from multiple perspectives and invokes `openrouter:fusion`. A **panel of models then responds in parallel**, a **judge compares** their answers and returns a structured analysis, which is passed back to the calling model for a final response.

Key tool parameters:
- `analysis_models` — the panel (1–8 models). **Each panel model operates with `openrouter:web_search` and `openrouter:web_fetch` force-enabled.**
- `model` — the judge, which produces structured JSON (defaults to an external model).
- `max_tool_calls` — tool-loop steps per panel model and judge (default **8**, range 1–16).
- The judge **compares, not merges**: what all models agree on becomes high-confidence (`consensus`), disagreements become `contradictions`, what only one model contributes becomes `unique_insights`, and what no one covered becomes `blind_spots`.

Canonical output: `{status, analysis:{consensus, contradictions, partial_coverage, unique_insights, blind_spots}, responses:[{model, content}]}`.

Two facts from the documentation that are critical for interpretation:
- **Web is built in and mandatory.** There is no option to disable it — this is the primary driver of cost and latency.
- **Billing is not described in the docs.** Consequently, all cost figures from this experiment represent the only measured source.

---

## 2. Experiment Methodology and Its Limitations

**Design (well-structured):** 2×2 "panel intelligence × judge intelligence" across open Chinese models + controls.

| Config | Panel | Judge | Intent |
|---|---|---|---|
| **C2_cn_open** | deepseek-v4-pro / glm-5.1 / kimi-k2.6 | qwen3-235b | smart panel + smart judge |
| **C5_smartpanel_dumbjudge** | same smart panel | qwen3-8b | smart panel + **dumb** judge |
| **C5inv_dumbpanel_smartjudge** | qwen3-8b / gemma-3-12b / glm-4.7-flash | glm-5.1 | **dumb** panel + smart judge |
| **C3_cn_small** | qwen3.6-27b / glm-4.7-flash / qwen3-32b | qwen3-32b | all-small (≈dumb+dumb) |
| **C6_echo** | qwen3-235b ×3 (single model) | qwen3-235b | **control: echo chamber** (zero diversity) |
| **C1_west_closed** | gpt-5.2 / gemini-3.1-pro / grok-4.3 | gpt-5.2 | western closed frontier |
| **B_cn** | — | — | single deepseek-v4-pro without fusion |
| **B_west** | — | — | single gpt-5.2 without fusion |

**Questions (23):** 5 scientific (proposal critique), 5 adversarial (debates), 13 factual (with reference answers; ranging from Monty Hall to Therac-25 and backprop-1986).

**Capture mechanics:** `max_tool_calls=1` (minimum; web is hardwired regardless), `max_tokens=20000`. Caller `qwen3-235b` with a relay prompt forces fusion and outputs the structure as flat JSON.

### Limitations that keep the entire interpretation at the level of "direction, not proof"

These caveats were confirmed by the adversarial analysis layer — they must be kept in mind at all times:

1. **N=23, ONE run, no repetitions.** No variance estimate. The difference "accuracy 1.0 vs 0.962" = one partial out of 13 = **noise**. Intra-config spread is enormous (cost up to 17.6×, latency 42–1248s). The C2/C5/C5inv swaps are compared on 1 observation per question — temperature noise and isolated tool failures can explain part of the "judge effect."
2. **The captured structure is the RELAY qwen3-235b, not the raw tool output.** Model attribution is renamed into roles, fabricated, or lost (`responses_present` 18–23/23). The structure and attribution across all cells are shaped by the same single caller — this may artificially **flatten** configs and fake "the judge writes the structure" (part of it is written by the caller).
3. **The grader is a model from the same family (qwen3-235b)**, which also serves as the caller everywhere and as the judge in C6. Conflicts of interest / grader leniency toward "its own" were not controlled.
4. **Web is mandatory and cannot be disabled → fusion conflates TWO variables:** "panel aggregation" and "web access." There is no arm of "single model + web," so the **marginal value of aggregation beyond web is literally unmeasured**. The strongest value examples (ADEKA anchors, catching retractions) are attributed to **web**, not to panel diversity.
5. **The question set represents canonical knowledge** (classic facts/debates) — precisely the regime where single-model frontiers are strongest and web adds the least. The conclusion "web does not add correctness" may not generalize to fresh/post-cutoff/long-tail queries.

---

## 3. Cost and Latency (the most robust layer)

Deterministic numbers from `quant.json`. This is data that can be trusted without qualification.

| Config | $/question | ×B_cn | ×B_west | Latency avg (max) | prompt/compl | retries | responses |
|---|---:|---:|---:|---:|---:|---:|---:|
| B_cn (deepseek solo) | **0.0028** | 1.0× | 0.2× | 25s (65s) | ~57 k tok prompt | 0 | — |
| B_west (gpt-5.2 solo) | **0.0123** | 4.4× | 1.0× | 21s (49s) | ~59 k tok prompt | 0 | — |
| C3_cn_small | 0.0467 | 16.7× | 3.8× | 376s (938s) | 4.5× | 5 | 23/23 |
| C6_echo | 0.0528 | 18.9× | 4.3× | 342s (**1248s**) | 6.6× | 0 | 20/23 |
| C5inv (dumb panel+smart judge) | 0.0896 | 32.0× | 7.3× | 231s (401s) | 5.0× | 3 | **18/23** |
| C2_cn_open | 0.1219 | 43.5× | 9.9× | 269s (505s) | 7.2× | 1 | 22/23 |
| C5 (smart panel+dumb judge) | 0.1223 | 43.7× | 9.9× | 363s (845s) | 4.6× | 0 | 21/23 |
| C1_west_closed | **0.1919** | **68.5×** | 15.6× | 246s (696s) | 5.7× | 6 | 23/23 |

**Findings:**
- **Fusion is 16.7–68.5× more expensive than a single CN model** and 3.8–15.6× more expensive than a single gpt-5.2.
- **Latency 231–376s (9–15× baseline), tails up to 1248s** (>20 min per question). This **exceeds typical SLA windows and HTTP client/proxy timeouts** — risk of paid-but-aborted calls. Notably, "intelligence" does not correlate with speed — the slowest configs are C3 (all small) and C6 (echo); latency is driven by **web round-trips**, not model size.
- **Token asymmetry: prompt ≫ completion (4.5–7.2×).** The single baseline has ~57 prompt tokens (bare question); fusion inflates the prompt to 16–34k tokens/question (**×280–600**) — this is downloaded web content pumped through **each** of the three panel models. The bulk of the cost is paid for **input tokens (web)**, not reasoning.

### Where the money goes: the cost driver is the PANEL + WEB, not the judge

The decisive observation from swapping on the **same** smart panel:
- **C2** (judge qwen3-235b) = $0.1219/q vs **C5** (same panel, judge downgraded to qwen3-8b) = $0.1223/q — **delta +$0.0004**.
- Reverse swap: **C5inv** (same expensive judge glm-5.1, but **dumb panel**) = $0.0896/q — the dumb panel saves **$0.0327/q (−27%)**.

→ **Cost lives in three parallel web-grounded panel inferences. The judge in this architecture is economically near-free.**

> ⚠️ **Caveat (noted by the skeptic):** "the judge is near-free" is an artifact of cheap qwen3-8b pricing. On an identical panel, C5 generates **+64% completion tokens** vs C2 (119687 vs 73055) and is **35% slower** (362s vs 269s). The judge is doing *a lot* of work — it is simply cheap per token. With an expensive judge, the delta would be material.

---

## 4. Quality: What Fusion Actually Delivers

### 4.1 Open-ended questions (10 items, scientific + controversial) — subjective deep-read assessments

| qid | Best config | Worst | Verdict | Single suffices? |
|---|---|---|---|---|
| sci-01..05 | C5inv ×3, C2 ×2 | C3 (×4) | all `marginal_value` | all `true` |
| con-01..05 | C2 ×3, C5inv ×3 | C3 (×3), C5, C6 | all `marginal_value` | all `true` |

- **10/10 questions: `marginal_value` + `single_model_suffices=true`.** The best fusion adds 1–3 web facts + occasionally catches an error. The substantive verdict ("implausible" / "portfolio approach" / …) is **identical with and without the panel**.
- In subjective ranking, the top positions are occupied by configs with a **smart judge**: C5inv (best in 6/10), C2 (4/10). The worst is almost always C3 (all small models).

> ⚠️ **Caveat (raised by the skeptic):** The "6/10 vs 4/10" ranking is a **single-pass subjective assessment by one Opus reader** with no rubric, repetition, or independent grader. This is a directional hypothesis, not a measurement. The deep-read input (`q_*.md`) contains only the judge's synthesis, so "panel ranking" is partly comparing **judge styles** (qwen3-235b verbose vs gpt-5.2 terse), not panel quality.

### 4.2 Factual accuracy (13 questions) — objective metric, and it tells a different story

Grades per config (independent Sonnet graders, including baselines):

| Config | correct/partial/wrong | acc* | Note |
|---|---|---:|---|
| **C1** (strong western panel) | 13 / 0 / 0 | **1.00** | the only 13/13 + responses 23/23 |
| **C2** (strong CN panel) | 13 / 0 / 0 | **1.00** | |
| **C5** (strong panel + **dumb** judge) | 13 / 0 / 0 | **1.00** | dumb judge did NOT corrupt facts from a strong panel |
| C6_echo | 10 / 3 / 0 | 0.885 | fac-06, fac-08, fac-12 — single model level |
| C3_cn_small | 10 / 3 / 0 | 0.885 | fac-08, fac-11, fac-12 |
| **C5inv** (**weak** panel + smart judge) | 8 / 5 / 0 | **0.81** | **worst fusion config on facts** |
| B_cn (deepseek solo) | 11 / 1 / 1 | 0.88 | wrong/empty: fac-08, fac-12 |
| B_west (gpt-5.2 solo) | 11 / 0 / 2 | 0.85 | wrong/empty: fac-08, fac-12 |

<sub>*acc = (correct + 0.5·partial)/13; LLM grading, at N=13 differences of one or two points = noise.</sub>

**Key counterpoint to "the judge dominates":** on the **objective** metric, **panel strength** wins. All three configs with a strong panel (C1/C2/C5) score 13/13, and **C5 achieved this with a dumb judge**. Meanwhile, "smart judge + weak panel" (C5inv) is the **worst** fusion config on facts (8/13, 5 partial: the smart judge glm-5.1 hedges/softens where the weak panel provided no solid factual grounding). That is:

> **The judge drives the quality of the critic function and structural richness; the PANEL drives factual correctness of substance. These are not interchangeable levers.** The only config that is strong on both dimensions is **C2 (strong panel + smart judge)**.

**fusion vs baseline on facts:**
- **Helped in 2/13** (fac-08 "real author of fast-inverse-sqrt", fac-12 Therac-25) — both times because **both baselines returned wrong/empty**, while the strong-panel configs answered correctly. This is **redundancy/reliability**, not unique knowledge.
- **"Baseline beat fusion" in 1/13 (fac-06)** — but this applies **only to echo control C6**, which dropped to partial (web pulled in a noisy figure). **All 5 genuine fusion configs answered correctly.** The headline "baseline beat fusion" is a categorical error (a failure of the control, not of the fusion class).
- On canonical facts (Monty Hall, Sputnik, Nobel-2023, Transformer-base, AlphaFold/CASP14, two's-complement, backprop-1986) the answer **lives in the models' weights** — web did not add correctness.

### 4.3 Where web-grounding delivered a qualitative (non-marginal) upgrade

The skeptic rightly noted that on the scientific block the value is in places **greater** than "1–3 facts." Example sci-01 (Li-S battery): the single B_west gave a competent but **ungrounded** answer — "300–500 Wh/kg, beyond demonstrated" with no references; C2/C5inv+web provided **falsifiable empirical anchors** — ADEKA 761/800 Wh/kg (Nov-2024, 0.05C), Nature Communications 2025 (866 charts/184 studies, 441 Wh/kg verified maximum), the counterexample SPAN‖Gr with graphite anode 1000 cycles/99%. This shifts the answer from "implausible" to "on the boundary of what has been demonstrated only at impractical 0.05C." **But this value comes from the WEB tool — reproducible by a single frontier model with web access — not from panel aggregation.**

---

## 5. Panel vs Judge (2×2 breakdown)

**Direction (medium confidence):** with a fixed panel, swapping the judge noticeably shifts the *qualitative* side of the output; with a fixed judge, swapping the panel shifts it less (but **shifts objective accuracy more strongly** — see §4.2).

**What a weak judge does with a strong panel (C5 vs C2)** — confirmed by verbatim audit:
- collapses `consensus` into generic bullets with no numbers;
- loses quantitative specificity (sci-04: anchors 370M Loihi, 7.3× energy-scaling, 72.7× NorthPole are lost);
- injects amplified claims ("KV cache bandwidth **DOMINATES** energy", whereas the panel only said "memory-bandwidth-bound");
- yet **saves no money** (C5≈C2 in $) and is **slower** → **anti-pattern**: pay for an expensive panel and discard its signal.

**What a smart judge does with a weak panel (C5inv)** — "rescue through SUBSTITUTION":
- glm-5.1 catches real errors from the weak panel: the hallucinated name "Walter Fendt" (fac-08), the fabricated "84% game/94% HFT" (con-04), the retracted "86% replication" Nature Human Behaviour article (con-05), the category error "GPT-3.5/4 API as an argument for open release" (con-03);
- but adds this **from its own knowledge/web**, presenting it as "panel consensus" → attribution fidelity drops (C5inv loses 22% of raw responses), and it also **fabricates unearned precision** (nonexistent arxiv IDs, "7.41 tok/W").

> ⚠️ **Main caveat (skeptic):** "judge dominates DECISIVELY / high confidence" — **overstated**. The only objective metric (factual accuracy) **is not predicted by judge intelligence**: weak judge C5 = 1.00 ≥ smart judge C5inv = 0.81. "C5inv structural > all" is confounded with **judge verbosity and assembly collapse** (maximum structure at minimum 18/23 responses). "More structure" = more judge text, not more signal. And the panel **is not decorative**: its errors are load-bearing (they contaminate the output and require cleanup by a smart judge).

**Spending takeaway:** if fusion is fixed — put money into a **smart judge**, not an expensive panel (but a *sufficient* panel is still needed for factual correctness). Never put a weak judge on an expensive panel (C5 — strictly dominated). The most honest conclusion: **for a single question, don't build fusion at all.**

---

## 6. Value of Diversity — Echo Control

**Conclusion (moderate confidence):** a premium for panel diversity **is not justified by this data** — but "diversity contributes NOTHING" would be an overstatement.

The clean natural experiment is **C2 vs C6** (identical judge qwen3-235b, diverse panel vs echo):
- C6_echo (qwen3-235b ×3, zero diversity): `avg_contradictions` **1.09** — within 7% of diverse C2 (1.17) and exactly equal to C3.
- `avg_consensus` for echo (4.04) is even **higher** than C2 (3.30) and C1 (2.91) — but this is a **tautology** (three identical models trivially agree; consensus and contradictions are mechanically anti-correlated).
- On closed scientific questions C6 honestly returns **empty** contradictions (`_(empty)_`); on contested ones it fills them with divergences **between web sources** (Metaculus vs Samotsvety vs Grace vs XPT), not between models. This reaches the point of absurdity: con-04 — "qwen3-235b vs qwen3-235b vs qwen3-235b" (the model "argues with itself").

> ⚠️ **Caveat (skeptic):** diversity **caught a real hallucination that echo is structurally incapable of catching** — fac-12: gemma-3-12b fabricated the flag name `high_dose_allowed`, glm-4.7-flash gave the correct `Class3`, qwen3-8b said "unnamed"; the smart judge resolved in favor of `Class3`. This is genuine disambiguation work performed by independent models. Furthermore, C1 (diverse panel) yields the highest `avg_contradictions` (1.70) and `avg_blind_spots` (5.17) among real panels — a small but directionally correct signal. So to be precise: "diversity contributes a small amount that doesn't justify its premium," not "contributes nothing."

**§6 Summary:** the substantive core of the answer = output of one good model + web; cross-model composition adds primarily (often spurious) disagreements. The data do not justify a premium for three different models.

---

## 7. Judge Influence and Provenance (Audit of Raw Responses)

The most important finding for trusting the output:

- **Attribution is fabricated at scale.** Raw `responses` across ≥9 files contain **phantom models** that appeared in no panel (`gpt-4o`, `claude-3-5-sonnet`, `claude-3-opus`, `Advocate_Open`, `Panel A-C`). Internal role-personas of a single model ("gemini Model-A/B/C") are promoted by the judge into "three panel positions." A participant voice called `evidence` — the judge's own parametric knowledge — is invented wholesale.
- **Structure is emitted even when the panel is absent.** On sci-02, for both C2 **and** C5inv the raw responses are missing, yet the judge produced a full consensus + 4 contradictions + 6 blind_spots. On con-02, the C1 panelist gpt-5.2 returned a tool-failure stub, yet the judge assembled a 4–6-row contradiction matrix with named sources (NuScale-2023, French PWR, NREL ReEDS, IPCC WG3) — **none of which appear in any panel response**.

> ⚠️ **Caveat (skeptic):** "responses absent" is partly a **serialization artifact of the dump**, not proof of fabrication: gaps also hit the recommended C2 (6 files). Per `quant.json`, C2 is missing only 1/23. Therefore "the judge invented an answer from weights over an empty panel" cannot be asserted as a systematic rule — but as a **risk** (when the panel genuinely collapses, the judge fills in from itself) it is confirmed.

**Practical conclusion:** `consensus`/`contradictions`/attribution **cannot** be presented as evidence of multi-model agreement without cross-checking against the raw `responses`. This is the output of the **judge** (plus the caller-relay), not a grounded voice of the panel.

---

## 8. West-closed (C1) vs East-open (C2)

**Decision: DO NOT pay the ~57% premium for C1.** It rests primarily on deterministic/political facts rather than on demonstrated reasoning superiority:

1. **Availability/openness (decisive argument in certain environments):** the entire C1 panel (gpt-5.2/gemini-3.1-pro/grok-4.3) is a closed Western frontier that is unavailable or throttled in a number of jurisdictions. Where this applies, **C1 is a non-starter regardless of quality.** C2 (deepseek-v4-pro/glm-5.1/kimi-k2.6 + qwen3-235b) consists entirely of open-weight models.
2. **Cost/latency:** C1 $0.192 vs C2 $0.122 (+57%), 6 retries vs 1.
3. **Factual reliability — the only real advantage of C1:** 13/13 + responses 23/23 + 0 empty. However, this accuracy ceiling is achievable **more cheaply** with a single frontier model.

> ⚠️ **Caveat (skeptic):** "C2 outperforms C1 in reasoning (rank 1.9 vs 3.0)" — **not proven**: this is a single-pass subjective judgment, confounded by judge identity (qwen verbose vs gpt-5.2 terse) and web-sample volume (C2 pulled in more web context: 22.9k vs 16k prompt tokens). "C1 collapsed on 4/5 contested" is actually ~3/5 (on con-03 the gpt-5.2 panel was strong). More accurate framing: **"C1 may be unavailable in geo-restricted environments, and the quality case for its premium is unproven (not disproven)"** — rather than "C2 is the stronger advisor."

---

## 9. Price Ladder C1 → C2 → C3 → C6: Quality, Cost, Swaps (Reasoning)

The practical question of "where expensive models can be swapped for cheaper ones" is most conveniently examined on a price ladder of four configs and **specifically on open-ended reasoning questions** (5 scientific-critique + 5 contested-debate): on factual questions even a single model/baseline hits the ceiling, so only the differentiation on reasoning is of interest.

Two independent quality measurements converge on the same finding: **on reasoning there are exactly two tiers.**

| Config | $/q | Score 0–10 (focus run, 2 lenses: rigor / usefulness) | Rank among 6 (1 = best) | Factual (13 Q, reference) |
|---|---:|---|---:|---:|
| **C1** closed West | 0.192 | **8.3** (rigor 8.1 / useful 8.6) | 3.0 | 1.00 |
| **C2** open CN | 0.122 | **8.0** (7.9 / 8.1) | **1.9** | 1.00 |
| *— tier gap ≈ 3 points —* | | | | |
| **C6** echo qwen3-235b ×3 | 0.053 | **5.1** (4.9 / 5.4), spread [2–7] | 4.4 | 0.885 |
| **C3** small CN | 0.047 | **4.8** (4.1 / 5.7) | 5.5 | 0.885 |

**The key finding:** the frontier tier (C1≈C2, ~8/10) on reasoning is **~3 points / ~40% higher** than the cheap tier (C3≈C6, ~5/10), and this is visible with both methods. Swapping frontier → cheap on reasoning **is not viable**: quantitative grounding, depth of mechanism analysis, and self-error detection are all lost.

**Frontier tier (C1 vs C2) → choose C2.** Quality is essentially equal. C1's score is marginally higher because the scoring reads the judge's finished synthesis, and the C1 judge (gpt-5.2) writes confident prose with citations even when the panel collapses (gpt-5.2 refuses on sci-03/04 and con-04 → effectively 2 models for the price of 3, plus named citations absent from the panel's responses). Accounting for provenance, C2 ranks higher (rank 1.9 vs 3.0). At equal quality, C2 is 57% cheaper, does not inflate with fabrication, and **is available where the closed Western frontier is restricted** (C2 — open weights, C1 — not).

**Cheap tier (C3 vs C6) → equal, neither dominates.**
- On factual questions both are tied (both 0.885 = the level of a single cheap model/baseline; fusion buys no accuracy here).
- **C6 is stronger on contested debates** (5–6.5): the single qwen3-235b's web-grounding helps. However, the panel is one model ×3, so `contradictions` on scientific questions are **empty** (three copies don't disagree), and on critique C6 collapses (sci-03 = 2.5). A "panel ×3" on top of a single qwen3-235b adds nothing, yet costs +13% more than C3 and delivers worse latency (tail 1248s).
- **C3 is slightly stronger/cheaper on scientific critique**; the skeleton of "what to check" holds (useful 5.7 ≫ rigor 4.1), but its failure mode is **citation hallucination** on complex/contested questions (fabricated benchmarks, inverted numbers, swallowed retracted papers). It does not catch its own errors.

### Swap Matrix (Reasoning)

| Task | Minimum safe config | MUST NOT drop to |
|---|---|---|
| Draft risk screening / "what to ask a startup", low-stakes | **C3 ($0.047)** — but do not trust its citations and numbers | — |
| Contested debates (requires clash of positions) | **C2 ($0.122)** — 3 different models produce live positions | C3 (fabricates), C6 (empty contradictions) |
| Scientific critique with quantitative anchors | frontier **C2** | C3/C6 lose specificity and numbers |
| Final analysis for a decision | frontier **C2** | entire cheap tier |

**The swap that dominates all others:** across every one of the 10 reasoning questions the verdict is `marginal_value` + `single_model_suffices=true`. That is, **one web-grounded frontier call + a self-critique pass** reproduces nearly all the value; a panel is only justified offline for adversarial fact-check or redundancy against an empty response. If a panel is still needed and budget matters — money is better spent on the **judge**, not on an expensive panel (outside this foursome, a config of "smart judge glm-5.1 + cheap panel" achieved the best reasoning rank of 1.5 at $0.090, but its structure requires validation — up to 22% of raw panel responses were lost).

> Confidence in resolution: scores 0–10 are subjective LLM scoring across two lenses on a SINGLE run (N=23, one sample per cell); the factual grader belongs to the same qwen3-235b family as the C2/C6 judge. Therefore what is robust is the **tier gap (~3 points)** and the **ordering C2 ≥ C1 ≫ {C6 ≈ C3}**; fine-grained differences within a tier (C1 vs C2, C3 vs C6) are within noise and do not yield hard rules.

---

## 10. Feature Meaningfulness / ROI — When It Makes Sense, When It Doesn't

### ✅ Fusion is worth it (narrowly):
- **Offline/batch stages** where 4–10 min per query is acceptable, **and** adversarial fact-checking of named numeric claims against the live web is required (was the paper retracted? is the benchmark figure current?) — with a **smart** judge (qwen3-235b+).
- **Redundancy** against an empty/failed single call in a high-stakes response (proven fusion value: coverage of 2 baseline-empty cases).
- **Calibration check** on someone else's overconfident forecast/number (con-01 inflated AGI timeline, con-05 retracted 86%).
- A fresh web-grounded anchor unavailable to a closed-weights model — **but this is the value of the web, not the panel**.

### ❌ Fusion is NOT worth it:
- **Any synchronous/user-facing path** with a seconds-level SLA (9–15× slowdown, tails up to 1248s → blown timeouts/SLA windows).
- **Well-known factual questions** — the answer is in the weights, the web adds nothing and may introduce noise.
- **Single analytical/critical responses** — a single frontier model already delivers the skeleton (10/10 `single_model_suffices`). Add a self-critique pass ≈ free for the critic effect.
- When you need to **trust per-model attribution** or treat `consensus` as genuine panel agreement — both are unreliable.
- **A weak judge on an expensive panel** (C5) — strictly dominated.
- **Bulk work that is price-sensitive** — 16–68× does not pay off for 1–3 facts.

### Best config if fusion is required nonetheless: **C2_cn_open ($0.122/q)**
The only one with a genuine 3-model panel **and** a smart judge, best synthesis fidelity in the audit, 13/13 on facts, top on reasoning at 6/10. C1 buys slightly greater factual reliability at maximum price (and is unavailable in geo-restricted environments). **C5inv "cheapest per structural unit" is a trap** (an artifact of structure fabrication by a smart judge over a weak panel; 22% lost responses; worst on facts).

### Cheap substitute for ~80–90% of the value
**A single open frontier call (e.g. deepseek-v4-pro) with web search enabled + an optional second self-critique pass** ("adversarially check your key numbers, check for retractions") — reproduces the web anchors and judge's fact-catch for **30–65s and $0.003–0.012/q** instead of $0.09–0.19 and 230–380s. The experiment shows: the incremental value of fusion = **web-grounding + critic pass**, not cross-model emergence (echo control confirms this).

---

## 11. What Held Up Under Adversarial Review — and What Did Not

All 4 thematic conclusions hold **with caveats** (none collapsed outright, none survived "as-is").

**Solid (deterministically / verbatim verified):**
- Cost multipliers 16.7–68.5× / 3.8–15.6×; latency 231–376s, tail 1248s; asymmetry prompt≫completion.
- Web is the driver of cost/latency; cannot be disabled.
- Provenance is unreliable: fabrication/renaming of attribution by the relay and the judge.
- A smart judge catches real errors (retractions, fabricated numbers, name hallucinations) that a dumb/small one misses — **judge-IQ-dependent**.
- Practical guidance: for a single question — single frontier + web + self-critique instead of fusion. C5 (smart panel + dumb judge) is an anti-pattern. C1 is expensive and unavailable in geo-restricted environments.

**Downgraded in confidence / do not assert with certainty:**
- "The judge dominates the panel **decisively**" → medium. Objective factual accuracy metrics show the opposite (panel **strength** drives correctness).
- "Diversity yields **nothing** / premise rejected" → "small contribution, not worth the premium **here**." There is a directional signal plus one real hallucination catch (fac-12) that echo control cannot replicate.
- "C2 outperforms C1 in **reasoning**" → unproven (confounded by judge style + web volume).
- "fusion = baseline in accuracy for cents" → baselines **were not labeled in the original metrics** (labeled separately in this analysis, see §4.2); and single models are **not** per-call reliable (frequent empty responses) — fusion buys redundancy.

**Specific "headline" claims refuted by the skeptic (corrected above):**
- "baseline beat fusion on fac-06" → no, only echo control C6 failed.
- "the dumb judge loses ~80% of the numeric base" → not a stable pattern (C5≈C2 on structural; C5 even emits more tokens); holds only on individual questions.
- "300M out of 370M is confabulation by the dumb judge" → misread; these are two different real figures in smart-judged C2.

---

## 12. Practical Recommendations

1. **Do not use Fusion in synchronous/interactive paths** with second-level SLA. Latency of 230–376s (tail 1248s) will exceed typical timeouts and produce billed-but-aborted calls.
2. **If a "model panel" is needed — only offline/batch** (due diligence, research, freshness/retraction checks on named claims), preferably with a smart judge — profile **C2** (open weights, judge of qwen3-235b class or higher). Do not put a weak judge on an expensive panel (C5) — strictly dominated.
3. **A cheap alternative for ~90% of cases:** a single open frontier call (deepseek-v4-pro / glm-5.1) **with web-search enabled** + an optional self-critique pass by the same model. Reproduces the web-grounding anchors and critic effect of fusion for cents and tens of seconds instead of $0.09–0.19 and minutes.
4. **Never present `consensus`/`contradictions`/attribution as "opinions of N models"** without cross-checking against the raw `responses` — this is the judge+relay output; attribution is fabricated.
5. **Replicate across ≥3 runs and on fresh/post-cutoff questions** (where web-grounding should show maximum effect) before treating anything as a causal fact — current findings are directional at N=23 / single run.

---

## Appendix A. Structural Metrics (`quant.json`)

| Config | coverage | contr_rate | blind_rate | avg_contr | avg_blind | avg_cons | $/unit | $/contr |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| C1_west_closed | 0.88 | 0.61 | 1.00 | 1.70 | 5.17 | 2.91 | 0.0196 | 0.1129 |
| C2_cn_open | 0.91 | 0.65 | 1.00 | 1.17 | 4.13 | 3.30 | 0.0142 | 0.1042 |
| C5_smartpanel_dumbjudge | 0.85 | 0.57 | 0.91 | 1.43 | 3.43 | 3.13 | 0.0153 | 0.0855 |
| C5inv_dumbpanel_smartjudge | 0.97 | 0.87 | 1.00 | 2.39 | 5.87 | 4.22 | 0.0072 | 0.0375 |
| C6_echo | 0.85 | 0.61 | 0.91 | 1.09 | 3.57 | 4.04 | 0.0061 | 0.0484 |
| C3_cn_small | 0.89 | 0.57 | 1.00 | 1.09 | 3.30 | 2.78 | 0.0065 | 0.0428 |

> Cost-per-unit paradox: the "cheapest per unit" configs are the weak-panel ones — C5inv/C6/C3. But "units" = schema slot fills, which the analysis itself identifies as largely judge fabrication — making the metric **partially circular** (cheap-garbage-per-dollar ≠ quality). Do not use as a value metric.

## Appendix B. Artifacts

- Raw results: `results/run_20260615_202451.json` (184 calls), `.metrics.json`.
- Derived for analysis: `analysis/data/quant.json` (deterministic metrics), `q_<qid>.md` (×23 — per-question config analysis), `resp_<qid>.md` (×23 — raw panel responses + judge synthesis), `INDEX.md` (config and question legend).
- Experiment scripts (`code/`): `probe.py` (API probe), `measure_cost.py` (cost measurement), `runner.py` (matrix run), `evaluate.py` (metrics + LLM grading), `prep_analysis.py` (data slicing for analysis).
