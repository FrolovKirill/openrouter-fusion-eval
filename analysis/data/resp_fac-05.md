# fac-05 — AlphaFold2 CASP competition  (raw panel responses + judge-синтез)
**Prompt:** In which year did DeepMind's AlphaFold2 win the CASP competition? What was the edition called, and what median GDT score did it achieve?

> ВНИМАНИЕ: responses релеятся caller'ом (qwen3-235b), не verbatim — атрибуция модели местами заменена ролью ('Panel Model A'); текст ответа реальный.


======================================================================
## C1_west_closed  (panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - AlphaFold2’s CASP win was in 2020 (CASP14 took place May–Dec 2020, with results presented Nov 30–Dec 4, 2020).
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

### RAW PANEL RESPONSES (что панель реально сказала):

**[openai/gpt-5.2]:**
AlphaFold2 won **in 2020**, in the **14th CASP competition (CASP14; “the 14th CASP assessment”)**, achieving an **overall median GDT score of 92.4**.

**[google/gemini-3.1-pro-preview]:**
{
  "consensus": "All models agree that DeepMind's AlphaFold2 won the CASP competition in 2020, during the CASP14 edition, achieving a median GDT score of 92.4.",
  "contradictions": "There are no contradictions between the models; all provide consistent dates, edition names, and median GDT scores.",
  "unique_insights": "Some models provide the additional context that the 92.4 GDT score is considered comparable to experimental accuracy (such as X-ray crystallography), representing a historic milestone for the 50-year-old protein folding problem.",
  "blind_spots": "The models do not explain how the GDT (Global Distance Test) score is calculated or the distinction between GDT_TS (Total Score) and GDT_HA (High Accuracy), simply providing the raw score.",
  "partial_coverage": "One model explicitly uses the exact GDT_TS metric abbreviation, while others just refer to it generally as the GDT score.",
  "responses": [
    "DeepMind's AlphaFold2 won the Critical Assessment of Structure Prediction (CASP) competition in 2020. This edition of the competition was called CASP14. AlphaFold2 achieved a stunning median Global Distance Test (GDT) score of 92.4, representing a breakthrough in accurately predicting 3D protein structures.",
    "AlphaFold2 won the CASP competition in 2020. It competed in the 14th edition, known as CASP14. In that competition, it achieved a median GDT score of 92.4 out of 100, reaching an accuracy level comparable to experimental methods.",
    "In the year 2020, DeepMind's AlphaFold2 won the CASP14 edition of the protein folding competition. It achieved an outstanding median GDT_TS score of 92.4, significantly outperforming all other computational approaches."
  ]
}

**[x-ai/grok-4.3]:**
{
  "consensus": "AlphaFold2 won CASP14 (2020) with median GDT score of 92.4",
  "contradictions": [],
  "unique_insights": [
    "DeepMind blog states median GDT 92.4 overall and 87.0 for hardest targets",
    "CASP14 results released confirming AlphaFold2 as top performer"
  ],
  "blind_spots": [
    "Exact calendar year 2020 is implied but not always stated directly in excerpts"
  ],
  "partial_coverage": [
    "Some sources focus on GDT-HA metric (78%) instead of standard GDT-TS"
  ],
  "responses": [
    {
      "model": "web_search",
      "answer": "CASP14 (2020); median GDT 92.4"
    }
  ]
}

======================================================================
## C2_cn_open  (panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - DeepMind's AlphaFold2 won the CASP competition in 2020.
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

### RAW PANEL RESPONSES (что панель реально сказала):

**[deepseek/deepseek-v4-pro]:**
```json
{
  "year": 2020,
  "edition": "CASP14 (14th Critical Assessment of Structure Prediction)",
  "median_gdt_score": 92.4
}
```

**[z-ai/glm-5.1]:**
DeepMind's **AlphaFold2** won the CASP competition in **2020**. The edition was called **CASP14** (the 14th Critical Assessment of protein Structure Prediction). It achieved a median **GDT_TS score of 92.4** across all targets — a score above 90 being informally considered competitive with experimental methods. For the hardest "free-modelling" targets (those without useful structural templates), it still achieved a median GDT of 87.0, a full 25 points above the next-best team.

**[moonshotai/kimi-k2.6]:**
DeepMind's AlphaFold2 won the CASP competition in **2020**. The edition was called **CASP14** (the 14th Critical Assessment of protein Structure Prediction), and it achieved a **median GDT score of 92.4**.

======================================================================
## C5_smartpanel_dumbjudge  (panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - DeepMind's AlphaFold2 won the CASP competition in 2020. The edition was called CASP14, and the median GDT score achieved was 92.4.
**contradictions:** 
  _(пусто)_
**unique_insights:** 
  - {"model": "deepseek/deepseek-v4-pro", "insight": "Median GDT scores sourced from DeepMind blog post with publication date (November 30, 2020)"}
  - {"model": "z-ai/glm-5.1", "insight": "Comparison of AlphaFold2's 244.0 z-score vs Baker's 90.8 z-score"}
**blind_spots:** 
  - Potential disputes/amendments to results
  - Broader implications beyond CASP competition

### RAW PANEL RESPONSES (что панель реально сказала):

**[deepseek/deepseek-v4-pro]:**
```json
{
  "consensus": "DeepMind's AlphaFold2 won the CASP competition in 2020. The edition was called CASP14, and the median GDT score achieved was 92.4 overall across all targets.",
  "contradictions": [],
  "unique_insights": "The median GDT scores are specifically sourced from the official DeepMind blog post, confirming 'the 14th CASP assessment' (CASP14), the year 2020 via the publication date (November 30, 2020), and the score of 92.4.",
  "blind_spots": "There is no coverage of potential later disputes or amendments to these results.",
  "partial_coverage": "Some sources only mention the year or the score, but the DeepMind blog provides all three details together.",
  "responses": {
    "Panel 1": "Based on the provided information, DeepMind's AlphaFold2 won the CASP competition in 2020. The competition was the 14th edition, known as CASP14. The median GDT score achieved was 92.4."
  }
}
```

**[z-ai/glm-5.1]:**
## AlphaFold2 at CASP14

DeepMind's **AlphaFold2** won the **CASP14** competition in **2020** (the assessment ran from May–July 2020, with results released in November 2020).

- **Edition:** **CASP14** (the 14th Critical Assessment of protein Structure Prediction)
- **Median GDT score:** **92.4 GDT** (GDT_TS) across all targets

This was a landmark result. A GDT score of ~90 is informally considered competitive with experimentally determined structures, and AlphaFold2's median of 92.4 far exceeded the next-best group (Baker, with a summed z-score of 90.8 compared to AlphaFold2's 244.0). Even on the hardest "Free Modeling" (FM) targets, AlphaFold2 still achieved a median score of **87.0 GDT**.

**[moonshotai/kimi-k2.6]:**
DeepMind's AlphaFold2 won the CASP competition in **2020**. The edition was **CASP14** (the 14th Critical Assessment of protein Structure Prediction). It achieved a median **GDT score of 92.4** overall across all targets.

======================================================================
## C5inv_dumbpanel_smartjudge  (panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - AlphaFold2 won CASP14 in 2020, achieving a median GDT_TS score of 92.4.
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

### RAW PANEL RESPONSES (что панель реально сказала):

**[qwen/qwen3-8b]:**
{
  "consensus": "DeepMind's AlphaFold2 won the CASP14 competition in 2020, achieving a median GDT score of 92.4.",
  "contradictions": "Some sources mention a median GDT_HA score of 78% (Wiley article), while others cite 92.4 GDT as the overall median score (Guinness World Records, Chemistry World). The discrepancy may arise from different metrics (GDT vs. GDT_HA) or target categories.",
  "unique_insights": "AlphaFold2's performance in CASP14 marked a significant breakthrough, with scores surpassing experimental accuracy for many targets. The competition ran from May to September 2020.",
  "blind_spots": "Uncertainty about whether the 92.4 GDT score refers to all targets or specific categories (e.g., Free Modelling).",
  "partial_coverage": "The Wiley article focuses on GDT_HA metrics, while other sources highlight overall GDT scores. The exact edition name (CASP14) is consistently mentioned but not explicitly tied to the year in all sources.",
  "responses": [
    "AlphaFold2 won CASP14 in 2020, achieving a median GDT score of 92.4 (Guinness World Records, Chemistry World).",
    "The Wiley article notes a median GDT_HA score of 78% for AlphaFold2 in CASP14, but this may differ from overall GDT metrics.",
    "CASP14 was held in 2020, with AlphaFold2's 92.4 GDT score setting a new benchmark (Guinness World Records).",
    "AlphaFold2's CASP14 results included a median GDT_HA of ~80%, with significant improvements over previous editions (Wiley article).",
    "The PubMed abstract confirms AlphaFold2's breakthrough in CASP14 but does not specify the exact GDT score."
  ]
}

**[google/gemma-3-12b-it]:**
```json
{
  "consensus": "DeepMind's AlphaFold2 achieved a breakthrough victory at CASP14 in 2020, demonstrating unprecedented accuracy in protein structure prediction. It achieved a median GDT score of 92.4.",
  "contradictions": [],
  "unique_insights": [
    "AlphaFold2's victory in CASP14 was described as a 'watershed moment' and a 'scientific breakthrough' due to its remarkable improvement over previous methods.",
    "The median GDT score of 92.4 signifies nearly perfect prediction accuracy, as a GDT score of 100 represents a perfect match.",
    "The team achieved this performance using an end-to-end neural network trained on a massive dataset of known protein structures."
  ],
  "blind_spots": [
    "The analysis doesn't delve into the specific technical innovations of AlphaFold2 beyond mentioning its neural network architecture.",
    "There's no discussion of the limitations of AlphaFold2, such as its performance on intrinsically disordered proteins or membrane proteins.",
    "The impact of AlphaFold2 on drug discovery and other fields is not explored."
  ],
  "partial_coverage": [
    "While the competition year (2020) and edition (CASP14) are specified, the significance of CASP itself and its role in evaluating protein structure prediction methods is not elaborated upon.",
    "The concept of GDT score is mentioned, but a deeper explanation of what GDT represents and how it's calculated would provide more context."
  ],
  "responses": [
    {
      "panel": "GPT-3.5",
      "answer": "DeepMind's AlphaFold2 famously won the CASP competition in 2020, specifically at CASP14. It achieved a median GDT score of approximately 92.4, a remarkable result that significantly surpassed previous predictions. This victory was hailed as a major breakthrough in the field of structural biology."
    },
    {
      "panel": "Claude-3-opus",
      "answer": "DeepMind's AlphaFold2 achieved a monumental victory at CASP14, which took place in 2020. The median GDT score AlphaFold2 achieved was 92.4. This was a watershed moment in the field of protein structure prediction."
    },
    {
      "panel": "Gemini-1.5-Pro",
      "answer": "DeepMind's AlphaFold2 won the CASP competition in 2020, at the 14th edition (CASP14).  It achieved a median GDT score of 92.4 during the competition, which was a significant achievement in protein structure prediction."
    }
  ]
}
```

**[z-ai/glm-4.7-flash]:**
```json
{
  "consensus": {
    "year": "2020",
    "edition": "CASP14",
    "median_gdt_score": "92.4 GDT"
  },
  "contradictions": [],
  "unique_insights": [
    "AlphaFold2 achieved a median GDT score of 92.4 GDT across all targets, which was considered competitive with experimental methods.",
    "The CASP14 competition ran from May to September 2020, with results announced on November 30, 2020.",
    "AlphaFold2 was the clear winner, achieving a score of 244.0 in the summed z-scores ranking compared to 90.8 for the next best group.",
    "The performance was so impressive that it led to a consensus in the scientific community that the structure prediction problem for single protein chains had been solved."
  ],
  "blind_spots": [
    "The search results don't provide specific details about the exact date when AlphaFold2 was announced as the winner.",
    "There's no information about the specific targets or categories within CASP14 where AlphaFold2 achieved its best performance.",
    "The search results don't mention the specific methodology improvements that led to AlphaFold2's superior performance compared to AlphaFold in CASP13."
  ],
  "partial_coverage": [
    "The information about the year and edition is complete and consistent across sources.",
    "The median GDT score is well-documented, but there might be additional details about other metrics (like GDT-HA) that weren't fully explored.",
    "The search results don't provide comprehensive information about the broader impact of AlphaFold2's performance on the field of protein structure prediction."
  ],
  "responses": [
    {
      "model": "web_search",
      "answer": "AlphaFold2 won the CASP14 competition in 2020, which ran from May to September 2020. It achieved a median GDT score of 92.4 GDT across all targets, which was considered competitive with experimental methods. This performance was so impressive that it led to a consensus in the scientific community that the structure prediction problem for single protein chains had been solved."
    }
  ]
}
```

======================================================================
## C6_echo  (panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - DeepMind's AlphaFold2 won the CASP competition in 2020 during the 14th edition (CASP14)
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

### RAW PANEL RESPONSES (что панель реально сказала):

**[qwen/qwen3-235b-a22b-2507]:**
DeepMind's AlphaFold2 won the CASP competition in 2020, during the 14th edition (CASP14). It achieved a median Global Distance Test (GDT) score of 92.4 across all targets.

**[qwen/qwen3-235b-a22b-2507]:**
DeepMind's AlphaFold2 won the CASP competition in 2020 during the 14th edition, known as CASP14. It achieved a median GDT score of 92.4.

**[qwen/qwen3-235b-a22b-2507]:**
DeepMind's AlphaFold2 won the CASP competition in 2020, during the 14th edition (CASP14), achieving a median GDT score of 92.4.

======================================================================
## C3_cn_small  (panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - DeepMind's AlphaFold2 achieved a median GDT score of 92.4 at CASP14 in 2020.
**contradictions:** 
  _(пусто)_
**unique_insights:** 
  - {"model": "qwen/qwen3-32b", "insight": "Notes that 'GDT-TS' is an alternate normalization of GDT, but both terms refer to the 92.4 score"}
**blind_spots:** 
  - No analysis of competing models (e.g., ColabFold or other CASP participants) in 2020
  - No discussion of post-CASP14 developments (AlphaFold3, experimental validation rates)
  - No exploration of CASP's classical methodology constraints vs. AlphaFold's ML approach

### RAW PANEL RESPONSES (что панель реально сказала):

**[qwen/qwen3.6-27b]:**
DeepMind's AlphaFold2 won the **CASP14** (Critical Assessment of Structure Prediction 14) competition in **2020**.

It achieved a median Global Distance Test (GDT) score of **92.4** across all targets, a level of accuracy widely considered comparable to experimental methods and a breakthrough in solving the 50-year-old protein folding problem.

**[z-ai/glm-4.7-flash]:**
Based on the search results, here are the details about AlphaFold2's CASP performance:

**Year:** 2020 (CASP14, which ran from May to September 2020)

**Edition name:** CASP14

**Median GDT score:** 92.4 GDT overall across all targets

AlphaFold2 achieved a median GDT score of 92.4, which represents an average error of approximately 1.6 Ångströms—comparable to the width of an atom. This performance was described as "competitive with results obtained from experimental methods" and marked a transformative advance in protein structure prediction.

**[qwen/qwen3-32b]:**
ool_call>{
  "consensus": "AlphaFold2 won the CASP14 competition in 2020, achieving a median GDT score of 92.4.",
  "contradictions": [],
  "unique_insights": [
    "The CASP14 edition was held in 2020, as noted in the DeepMind blog and the Semanticscholar PDF.",
    "The term 'GDT-TS' is sometimes used alongside 'GDT', but both references confirm the 92.4 score."
  ],
  "blind_spots": [
    "The web search results do not mention alternative metrics or competing models in CASP14 beyond AlphaFold2's performance."
  ],
  "partial_coverage": [],
  "responses": {
    "response_1": "In the 14th CASP assessment (CASP14, held in 2020), DeepMind's AlphaFold2 achieved a median GDT score of 92.4, as documented in the DeepMind blog post and the Semanticscholar PDF.",
    "response_2": "The CASP14 edition (2020) recognized AlphaFold2 with a median GDT-TS score of 92.4, confirming its transformative performance in protein structure prediction.",
    "response_3": "Confirmed in the DeepMind blog and CASP14 data, AlphaFold2's 92.4 GDT score in 2020 marked a breakthrough in CASP history."
  }
}