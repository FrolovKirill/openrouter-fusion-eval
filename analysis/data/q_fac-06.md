# fac-06 — Birthday paradox — exact group sizes
**Block:** factual  |  **difficulty:** medium

**Prompt:**
In the birthday paradox (assuming 365 days, uniform distribution): (1) What is the minimum group size where the probability that at least two people share a birthday exceeds 50%? (2) What is the minimum group size for the probability to exceed 99%? Give exact numbers.

**Expected answer (эталон):**
(1) 23 people: P ≈ 50.7%. (2) 57 people: P ≈ 99.0%.

---
## FUSION-конфиги (judge-анализ; responses вынесены в resp_*.md)

### C1_west_closed
_западный закрытый фронтир_  
panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2 | cost=$0.0744 | 123.3s | ptok=10700 ctok=1679 | retries=1

**consensus:**
  - Minimum n such that P(at least one shared birthday) > 50% (365 days, uniform, independent) is 23 (verified: P_unique(23)=365·364·…·343 / 365^23 ≈ 0.492703, so P_shared ≈ 0.507297 > 0.5; for n=22, P_shared ≈ 0.475695 < 0.5).
  - Minimum n such that P(at least one shared birthday) > 99% is 57 (verified: for n=57, P_unique ≈ 0.009910 < 0.01 so P_shared ≈ 0.990090 > 0.99; for n=56, P_unique ≈ 0.011312 > 0.01 so P_shared ≈ 0.988688 < 0.99).

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "google/gemini-3.1-pro-preview", "insight": "Explicitly contrasted the immediately-below-threshold cases (22→~47.5%, 56→~98.8%) with the first above-threshold cases (23→~50.7%, 57→~99.01%), directly addressing the prompt’s strict 'exceeds' criterion."}

**blind_spots:**
  - No model showed (or referenced) an explicit step-by-step verification of minimality via computed products/log-sums; most asserted the known results without demonstrating the calculation.
  - None clarified numerical rounding/precision choices (e.g., how many digits are needed to be sure the probability crosses 0.50 or 0.99), which matters when asserting strict inequalities.
  - No model mentioned the equivalent log-form computation (summing ln(1−k/365)) as a robust way to avoid floating-point underflow/rounding in direct products, which is relevant for rigorous verification even if not required by the prompt.

**partial_coverage:**
  - {"models": ["openai/gpt-5.2"], "point": "Gave the exact complementary-product formula p(n)=1−(365·364·…·(365−n+1))/365^n rather than only final n-values."}
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "Provided near-threshold numeric probabilities (n=22 vs 23; n=56 vs 57) to justify minimality."}

### C2_cn_open
_открытый китайский фронтир (умн+умн)_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507 | cost=$0.0861 | 296.1s | ptok=13392 ctok=2384 | retries=0

**consensus:**
  - The minimum group size for the probability of at least two people sharing a birthday to exceed 50% is 23.
  - The minimum group size for the probability to exceed 99% is 57.

**contradictions:**
  - {"topic": "Minimum group size for 99% probability of shared birthday", "stances": [{"model": "Brilliant Math & Science Wiki", "stance": "70 people are needed for 99% probability"}, {"model": "deepseek/deepseek-v4-pro", "stance": "57 people are needed for 99% probability"}, {"model": "z-ai/glm-5.1", "stance": "57 people are needed for 99% probability"}, {"model": "moonshotai/kimi-k2.6", "stance": "57 people are needed for 99% probability"}, {"model": "wikipedia.org", "stance": "57 people exceed 99% (P=99.01%), 70 people achieve 99.9%"}]}

**unique_insights:**
  - {"model": "deepseek/deepseek-v4-pro", "insight": "Scaling law: critical group size for 50% is about 1.177√D; for 99% is about 3.034√D."}

**blind_spots:**
  - None of the models explicitly verified P(56) ≈ 98.85% and P(57) ≈ 99.01% via direct computation or authoritative reference; reliance is on consensus or approximation.
  - No model addressed how dependence between pairwise birthday comparisons affects the exact probability calculation, despite the use of approximations assuming independence.
  - The impact of real-world birthday distributions (e.g., seasonal birth trends) on the 99% threshold was not quantitatively analyzed, though mentioned qualitatively.
  - No model discussed the expected number of collisions or the distribution of shared birthdays beyond the binary presence/absence of a match.

**partial_coverage:**
  - {"models": ["deepseek/deepseek-v4-pro"], "point": "Scaling law: critical group size for 50% is about 1.177√D; for 99% is about 3.034√D."}
  - {"models": ["deepseek/deepseek-v4-pro"], "point": "Exact formula: P(match) = 1 - ∏_{i=0}^{n-1} (365-i)/365"}
  - {"models": ["deepseek/deepseek-v4-pro"], "point": "Relevance to birthday attacks in cryptography: collision probability in a hash function with n-bit output reaches 50% after ~2^{n/2} random inputs."}
  - {"models": ["z-ai/glm-5.1"], "point": "Exact probabilities calculated: P(23) ≈ 50.73%, P(57) ≈ 99.01%"}

### C5_smartpanel_dumbjudge
_умная панель + глупый судья_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b | cost=$0.0685 | 363.8s | ptok=25998 ctok=6611 | retries=0

**consensus:**
  - 23 people for >50%
  - 57 people for >99%

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "deepseek/deepseek-v4-pro", "insight": "The scaling law: critical group size grows roughly as √(2d × ln(1/(1-p)))"}
  - {"model": "deepseek/deepseek-v4-pro", "insight": "The Poisson approximation yields near-exact results: for n=23, P(no match) ≈ exp(-n(n-1)/730)"}
  - {"model": "z-ai/glm-5.1", "insight": "Detailed formula and table with exact probabilities for n=23 and n=57"}

**blind_spots:**
  - Non-uniform birthday distribution
  - Leap day (February 29) ignored
  - Time-of-day not considered
  - Confusion between 99% and 99.9% thresholds

**partial_coverage:**
  - {"models": ["deepseek/deepseek-v4-pro"], "point": "Brilliant mentions 70 for 99% (likely conflating 99.9% threshold)"}

### C5inv_dumbpanel_smartjudge
_глупая панель + умный судья (qwen-2.5-7b → gemma-3-12b-it)_  
panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1 | cost=$0.0361 | 160.5s | ptok=13712 ctok=2440 | retries=0

**consensus:**
  - Minimum group size for P(shared birthday) > 50% is 23 people
  - Minimum group size for P(shared birthday) > 99% is 57 people
  - Both answers verified against authoritative sources (Wikipedia, MathWorld, Harvard) and exact computation: n=23 gives P ≈ 50.73%; n=57 gives P ≈ 99.01%

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "z-ai/glm-4.7-flash", "insight": "Explains the quadratic pair-counting intuition: with n people there are n(n-1)/2 pairs, so n=23 yields 253 pairs — the paradox arises because pair count grows quadratically, not linearly, making naive intuition (expecting ~183 needed) wrong"}

**blind_spots:**
  - No model verifies the boundary case n=56 to confirm P < 99% at that point, which is necessary to rigorously establish 57 as the minimum — they all assert the answer without checking the adjacent integer
  - No model mentions the standard exponential approximation P ≈ 1 - exp(-n(n-1)/(2d)) or its error bounds, which would provide independent verification of the exact results
  - No model discusses the generalization to other probability thresholds (e.g., 95% → n=47) or other day-pool sizes, which would help contextualize the scaling behavior P ∝ √N
  - No model distinguishes between the 'any shared birthday' problem and the distinct 'someone shares my birthday' problem (which requires n≈253 for 50%), a common source of confusion that would strengthen the explanation

**partial_coverage:**
  - {"models": ["z-ai/glm-4.7-flash"], "point": "Provides exact probability values at the thresholds: n=23 → 50.73%, n=57 → 99.01%, and boundary-adjacent value n=22 → 47.57%"}
  - {"models": ["z-ai/glm-4.7-flash"], "point": "Gives both the product form and factorial form of the exact formula: P = 1 - ∏(k=0 to n-1)(365-k)/365 = 1 - 365!/(365^n × (365-n)!)"}
  - {"models": ["google/gemma-3-12b-it"], "point": "Notes the counterintuitive nature and that calculation relies on computing P(no shared) and subtracting from 1"}

### C6_echo
_контроль: эхо-камера_  
panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507 | cost=$0.0113 | 42.2s | ptok=17176 ctok=1106 | retries=0

**consensus:**
  All sources agree that in the birthday paradox with 365 days and a uniform distribution, the minimum group size for the probability of at least two people sharing a birthday to exceed 50% is 23, and the size to exceed 99% is between 57 and 70. Most specifically point to 23 for 50% and 57 or 70 for 99%, with slight variation in precise threshold interpretation.

**contradictions:**
  There is a discrepancy regarding the group size needed for a 99% probability. While Brilliant.org and the Math Fun Facts source state 70 people are needed for 99%, other sources (EverydayBudd and Wikipedia) indicate that 57 people suffice to exceed 99%. This suggests differing interpretations of when the threshold is 'exceeded' or possible approximation differences.

**unique_insights:**
  - Brilliant.org notes the intuitive explanation that the number of pairs grows quadratically (as $\binom{n}{2}$), which causes the probability to rise faster than linearly.
  - EverydayBudd highlights that the threshold scales approximately with the square root of the number of days ($\sqrt{D}$), providing a generalized rule of thumb.
  - Wikipedia provides a detailed table showing exact probabilities increasing with group size and clarifies that 50.7% is achieved at n=23, and 99.4% at n=60, with 57 already reaching 99%.
  - The CalcBE source gives the exact formula: $ P(\text{collision}) = 1 - \frac{(d)_n}{d^n} $, where $ (d)_n $ is the falling factorial.

**blind_spots:**
  - None of the sources explicitly compute the exact probability at n=57 and n=70 to definitively resolve the 99% threshold, relying instead on rounded percentages.
  - While explanations for the 50% threshold are robust, fewer intuitive justifications are offered for why 57 or 70 people reach 99%.

**partial_coverage:**
  The sources collectively cover both questions, but there is partial disagreement on the 99% threshold. Some sources give n=57 (EverydayBudd, Wikipedia), while others state n=70 (Brilliant.org, Math Fun Facts). This may stem from Wikipedia stating 57 gives 'better than 99%' while Brilliant says 70 gives '100%' and notes 70% at n=30, possibly extrapolating.

### C3_cn_small
_всё мелкое_  
panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b | cost=$0.0338 | 937.9s | ptok=11223 ctok=1817 | retries=0

**consensus:**
  - Minimum group size for 50% probability is 23 people.
  - Minimum group size for 99% probability is 57 people.

**contradictions:**
  - {"topic": "Minimum group size for 99% probability", "stances": [{"model": "z-ai/glm-4.7-flash", "stance": "Some sources claim 70 people, but consensus mathematics shows 57 people achieve 99.01%."}, {"model": "evidence", "stance": "Mathematical calculations confirm 57 people exceed 99% probability (99.01%), contradicting claims of 70."}]}

**unique_insights:**
  - {"model": "z-ai/glm-4.7-flash", "insight": "Explanation of the formula P = 1 - (365/365)(364/365)... and the role of 253 pairs in the paradox’s counterintuitive nature."}

**blind_spots:**
  - No model explicitly addresses the assumption of uniform distribution or provides a full derivation of the probabilities for n=23 or n=57.
  - Failure to mention historical or real-world applications of the paradox (e.g., hash collisions in computer science).

**partial_coverage:**
  - {"models": ["z-ai/glm-4.7-flash"], "point": "The exact probability calculation for n=57 (99.01%) is referenced but not fully detailed in the response."}


---
## BASELINE (одиночная модель, без fusion)

### B_cn  (model=deepseek-v4-pro | cost=$0.0019 | 10.4s)
(1) 23  
(2) 57

### B_west  (model=gpt-5.2 | cost=$0.0080 | 9.1s)
Let  
\[
P_{\text{no match}}(n)=\frac{365}{365}\cdot\frac{364}{365}\cdot\frac{363}{365}\cdots\frac{365-n+1}{365}
=\frac{365\cdot 364\cdots(365-n+1)}{365^n},
\]
so
\[
P_{\text{match}}(n)=1-P_{\text{no match}}(n).
\]

### (1) Probability exceeds 50%
- \(n=22:\; P_{\text{match}}(22)\approx 0.475695 < 0.5\)
- \(n=23:\; P_{\text{match}}(23)\approx 0.507297 > 0.5\)

**Minimum group size: \(\boxed{23}\).**

### (2) Probability exceeds 99%
- \(n=56:\; P_{\text{match}}(56)\approx 0.988632 < 0.99\)
- \(n=57:\; P_{\text{match}}(57)\approx 0.990122 > 0.99\)

**Minimum group size: \(\boxed{57}\).**
