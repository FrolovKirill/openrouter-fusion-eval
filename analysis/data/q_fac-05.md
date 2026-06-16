# fac-05 — AlphaFold2 CASP competition
**Block:** factual  |  **difficulty:** medium

**Prompt:**
In which year did DeepMind's AlphaFold2 win the CASP competition? What was the edition called, and what median GDT score did it achieve?

**Expected answer (эталон):**
2020. CASP14. Median GDT score ~92.4 (out of 100).

---
## FUSION-конфиги (judge-анализ; responses вынесены в resp_*.md)

### C1_west_closed
_западный закрытый фронтир_  
panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2 | cost=$0.1501 | 695.7s | ptok=9984 ctok=1503 | retries=1

**consensus:**
  - AlphaFold2’s CASP win was in 2020 (CASP14 took place May–Dec 2020, with results presented Nov 30–Dec 4, 2020).
  - The edition was the 14th CASP experiment, called CASP14 (the 14th Critical Assessment of protein Structure Prediction / 14th CASP assessment).
  - Reported median GDT score for AlphaFold2 at CASP14 was 92.4 (commonly reported as median GDT_TS / median domain GDT_TS = 92.4).

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "x-ai/grok-4.3", "insight": "Mentions the breakdown that AlphaFold2’s median GDT was 87.0 for the hardest free-modeling targets (in addition to 92.4 overall), which helps contextualize the headline number."}

**blind_spots:**
  - No response cleanly disambiguates what “median GDT 92.4” refers to across sources (e.g., median over targets vs median over domains; “overall across all targets” vs “median over domains”), even though both phrasings appear in primary/secondary reports.
  - No response cites primary evidence for the specific trio of facts (year, edition name, median score), despite these being checkable (e.g., CASP14 official site timeline and DeepMind’s CASP14 announcement; CASP14 assessment papers).
  - No response explains that GDT typically means GDT_TS in CASP context, nor warns that GDT_HA is a different metric with a different scale/typical values (e.g., median GDT_HA reported around 78% for CASP14 top performance).
  - No response clarifies what “win” means operationally in CASP (e.g., ranking methodology such as summed z-scores by assessors) versus the popular-press framing.

**partial_coverage:**
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "Explicitly labels the metric as GDT_TS (rather than just “GDT”)."}
  - {"models": ["x-ai/grok-4.3"], "point": "Adds that DeepMind also reported a separate median GDT of 87.0 on the hardest (free-modeling) targets."}
  - {"models": ["x-ai/grok-4.3"], "point": "Notes some sources emphasize GDT_HA (high-accuracy) rather than standard GDT_TS, implying possible metric mix-ups."}

### C2_cn_open
_открытый китайский фронтир (умн+умн)_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507 | cost=$0.0628 | 191.7s | ptok=7208 ctok=855 | retries=0

**consensus:**
  - DeepMind's AlphaFold2 won the CASP competition in 2020.
  - The edition was called CASP14 (the 14th Critical Assessment of protein Structure Prediction).
  - AlphaFold2 achieved a median GDT score of 92.4.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "z-ai/glm-5.1", "insight": "A GDT score above 90 is informally considered competitive with experimental methods, contextualizing AlphaFold2's 92.4 achievement."}

**blind_spots:**
  - None of the models mentioned that AlphaFold2 was entered under the team name 'AlphaFold2' during CASP14, distinct from the earlier CASP13 system.
  - No model noted that AlphaFold2's performance was evaluated on blind tests using recently solved structures not yet in the PDB.
  - The role of the Evoformer architecture and end-to-end deep learning in enabling this breakthrough was not addressed by any model.
  - No response mentioned that AlphaFold2's predictions had a median backbone accuracy of 0.96 Å r.m.s.d.95, comparable to atomic resolution.
  - The use of confidence metrics like pLDDT and pTM, which allow per-residue reliability estimation, was omitted from all responses.

**partial_coverage:**
  - {"models": ["z-ai/glm-5.1"], "point": "AlphaFold2 achieved a median GDT of 87.0 on the hardest 'free-modelling' targets, 25 points above the next-best team."}

### C5_smartpanel_dumbjudge
_умная панель + глупый судья_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b | cost=$0.0454 | 104.2s | ptok=8088 ctok=1099 | retries=0

**consensus:**
  - DeepMind's AlphaFold2 won the CASP competition in 2020. The edition was called CASP14, and the median GDT score achieved was 92.4.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "deepseek/deepseek-v4-pro", "insight": "Median GDT scores sourced from DeepMind blog post with publication date (November 30, 2020)"}
  - {"model": "z-ai/glm-5.1", "insight": "Comparison of AlphaFold2's 244.0 z-score vs Baker's 90.8 z-score"}

**blind_spots:**
  - Potential disputes/amendments to results
  - Broader implications beyond CASP competition

**partial_coverage:**
  - {"models": ["deepseek/deepseek-v4-pro", "z-ai/glm-5.1"], "point": "CASP14 ran from May–July 2020 with results released in November 2020"}
  - {"models": ["z-ai/glm-5.1"], "point": "AlphaFold2's 87.0 GDT score on Free Modeling targets"}

### C5inv_dumbpanel_smartjudge
_глупая панель + умный судья (qwen-2.5-7b → gemma-3-12b-it)_  
panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1 | cost=$0.0684 | 239.8s | ptok=14880 ctok=2761 | retries=0

**consensus:**
  - AlphaFold2 won CASP14 in 2020, achieving a median GDT_TS score of 92.4.
  - AlphaFold2's performance was considered a major breakthrough, dramatically outperforming all other groups.
  - CASP14 was the 14th edition of the Critical Assessment of Protein Structure Prediction competition.

**contradictions:**
  - {"topic": "Interpretation of 'median GDT score' — GDT_TS vs GDT_HA", "stances": [{"model": "qwen/qwen3-8b", "stance": "Identifies a discrepancy between 92.4 (GDT_TS) and 78% (GDT_HA), noting they are different metrics"}, {"model": "google/gemma-3-12b-it", "stance": "Reports only 92.4 as 'median GDT score' without distinguishing GDT_TS from GDT_HA"}, {"model": "z-ai/glm-4.7-flash", "stance": "Reports only 92.4 as 'median GDT score' without distinguishing metrics"}, {"model": "evidence", "stance": "DeepMind's own paper confirms median GDT_TS of 92.4; the CASP14 high-accuracy assessment paper confirms median GDT_HA of 78%. These are two distinct, coexisting metrics — not contradictory values but different scoring systems. The original question's term 'GDT score' is ambiguous but conventionally refers to GDT_TS in CASP context."}]}

**unique_insights:**
  - {"model": "qwen/qwen3-8b", "insight": "Identified that the apparent score discrepancy (92.4 vs 78%) stems from different metrics (GDT_TS vs GDT_HA), which measure accuracy at different tolerances — a critical distinction for interpreting AlphaFold2's performance"}
  - {"model": "z-ai/glm-4.7-flash", "insight": "Quantified AlphaFold2's dominance with the summed z-score gap (244.0 vs 90.8), showing it outperformed the runner-up by nearly 3x — the largest margin in CASP history"}

**blind_spots:**
  - No model clarified that the original question's term 'GDT score' is ambiguous — GDT_TS and GDT_HA are both GDT-family metrics with different tolerance thresholds (1/2/4/8Å vs 0.5/1/2/4Å), and 92.4 specifically refers to GDT_TS
  - No model mentioned AlphaFold2's specific performance on the hardest Free Modeling (FM) targets, where median GDT_TS was ~87-88.5, lower than the overall 92.4 but still revolutionary
  - No model noted that 58 of 92 domains achieved GDT_TS > 90, crossing into experimental-accuracy territory
  - No model addressed AlphaFold2's documented limitations at CASP14: poor performance on obligate oligomeric assemblies, flexible/disordered regions, and membrane proteins
  - No model mentioned that the AlphaFold2 Nature paper was published in 2021, after the 2020 competition

**partial_coverage:**
  - {"models": ["qwen/qwen3-8b"], "point": "Noted the distinction between GDT_TS (92.4) and GDT_HA (78%) metrics, explaining why different sources report different scores"}
  - {"models": ["z-ai/glm-4.7-flash"], "point": "Provided the summed z-score comparison: AlphaFold2 scored 244.0 vs 90.8 for the next-best group, quantifying the margin of victory"}
  - {"models": ["qwen/qwen3-8b", "z-ai/glm-4.7-flash"], "point": "Mentioned CASP14 ran from May to September 2020, with results announced November 30, 2020"}
  - {"models": ["z-ai/glm-4.7-flash"], "point": "Noted the scientific consensus that the structure prediction problem for single protein chains was effectively solved"}

### C6_echo
_контроль: эхо-камера_  
panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507 | cost=$0.0295 | 1248.2s | ptok=6576 ctok=634 | retries=0

**consensus:**
  - DeepMind's AlphaFold2 won the CASP competition in 2020 during the 14th edition (CASP14)
  - AlphaFold2 achieved a median GDT score of 92.4 across all targets

**contradictions:**
  _(пусто)_

**unique_insights:**
  _(пусто)_

**blind_spots:**
  - None of the models clarified that the 92.4 GDT score refers specifically to GDT_TS (Global Distance Test Total Score), the variant used by CASP
  - No model mentioned that the performance was particularly groundbreaking for Free Modeling (FM) targets, where AlphaFold2 achieved a median score of 87.0 GDT
  - No model noted that the success of AlphaFold2 represented a paradigm shift, being the first to achieve near-experimental accuracy consistently across diverse protein types
  - No mention of the broader scientific impact, such as enabling high-accuracy predictions for proteins that are difficult to crystallize, like membrane proteins
  - Absence of discussion on AlphaFold2's ability to provide per-residue confidence estimates (pLDDT), a key innovation that enhances usability

**partial_coverage:**
  _(пусто)_

### C3_cn_small
_всё мелкое_  
panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b | cost=$0.0213 | 317.0s | ptok=8080 ctok=1015 | retries=1

**consensus:**
  - DeepMind's AlphaFold2 achieved a median GDT score of 92.4 at CASP14 in 2020.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "qwen/qwen3-32b", "insight": "Notes that 'GDT-TS' is an alternate normalization of GDT, but both terms refer to the 92.4 score"}

**blind_spots:**
  - No analysis of competing models (e.g., ColabFold or other CASP participants) in 2020
  - No discussion of post-CASP14 developments (AlphaFold3, experimental validation rates)
  - No exploration of CASP's classical methodology constraints vs. AlphaFold's ML approach

**partial_coverage:**
  - {"models": ["qwen/qwen3-32b"], "point": "References specific sources (DeepMind blog, Semanticscholar) for CASP14 details"}


---
## BASELINE (одиночная модель, без fusion)

### B_cn  (model=deepseek-v4-pro | cost=$0.0009 | 20.3s)
DeepMind's AlphaFold2 won the **2020** edition of CASP, known as **CASP14** (the 14th Critical Assessment of Structure Prediction). It achieved a **median GDT_TS score of 92.4** across all targets.

### B_west  (model=gpt-5.2 | cost=$0.0029 | 6.0s)
AlphaFold2 won the CASP protein-structure-prediction competition in **2020**, at **CASP14** (the **14th Critical Assessment of Structure Prediction**). It achieved a **median GDT_TS score of ~92.4** across the targets in that edition.
