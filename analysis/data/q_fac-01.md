# fac-01 — Monty Hall probability
**Block:** factual  |  **difficulty:** easy

**Prompt:**
You're on a game show: 3 doors, one hides a car, two hide goats. You pick door 1. The host (who knows what's behind each door) opens door 3, revealing a goat. You're offered the chance to switch to door 2. Should you switch? What is the exact probability of winning if you switch vs. if you stay? Explain the reasoning.

**Expected answer (эталон):**
Switch. P(win | switch) = 2/3. P(win | stay) = 1/3.

---
## FUSION-конфиги (judge-анализ; responses вынесены в resp_*.md)

### C1_west_closed
_западный закрытый фронтир_  
panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2 | cost=$0.0618 | 133.4s | ptok=11298 ctok=1840 | retries=0

**consensus:**
  - Under the standard Monty Hall assumptions (host knows locations, always opens an unchosen goat door, always offers a switch; if the host has a choice of goat doors, the choice is not correlated with the car location), switching is optimal.
  - With those assumptions, the exact probabilities are P(win|stay)=1/3 and P(win|switch)=2/3.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "x-ai/grok-4.3", "insight": "Suggests empirical verification via simulation (e.g., ~1000 trials) to observe switching winning about 66.7% of the time."}

**blind_spots:**
  - None of the responses explicitly state the key hidden assumption needed to make the 2/3 result determinate from the prompt as written: the host’s door-opening policy must be fixed and not depend on where the car is (beyond never revealing it) and the host must always offer the switch. If the host’s choice of which goat door to open is biased in a way correlated with the car location, P(win|switch) conditional on observing 'door 3 opened' can differ from 2/3.
  - No response gives a fully explicit conditional-probability/Bayes table for the exact observed event (host opened door 3) that makes the dependence on host policy mathematically transparent.
  - No response discusses common variant edge cases: host sometimes does not offer a switch, host sometimes opens a door uniformly at random without knowledge, or host may preferentially open a specific door when multiple goat doors are available—each changes the posterior.

**partial_coverage:**
  - {"models": ["openai/gpt-5.2"], "point": "Explicitly notes the tie-breaking case: if the contestant initially picked the car, the host can open either remaining goat door; switching then loses in that 1/3 branch."}
  - {"models": ["x-ai/grok-4.3"], "point": "Mentions that the result can be derived via Bayes’ rule or by enumerating equally likely car locations (without giving the full Bayes calculation)."}

### C2_cn_open
_открытый китайский фронтир (умн+умн)_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507 | cost=$0.0441 | 247.9s | ptok=18982 ctok=3851 | retries=0

**consensus:**
  - You should switch doors.
  - The probability of winning if you stay with door 1 is 1/3.
  - The probability of winning if you switch to door 2 is 2/3.
  - The host knows what is behind the doors and always reveals a goat.
  - The host always offers the chance to switch.
  - The initial probability that the car is behind the chosen door is 1/3.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "z-ai/glm-5.1", "insight": "The 100-door analogy powerfully illustrates how the host's deterministic, information-revealing behavior concentrates the initial 99/100 probability of having chosen wrongly onto the single unopened, unchosen door, making it clear that switching is optimal. This scales down intuitively to the 3-door case."}

**blind_spots:**
  - No model addresses the game-theoretic perspective where the host is not a neutral referee but a strategic adversary whose behavior may depend on the contestant's choices and whose incentives (e.g., to prolong suspense or minimize prize payout) could alter optimal strategy.
  - No model considers the possibility that the host may not always offer the switch, which could signal information about the contestant's chosen door (e.g., offering a switch only when the contestant initially picked the car), thereby turning it into a signaling game.
  - None analyze the epistemic conditions under which the contestant can justifiably assume the host's behavior follows the standard protocol, especially in real-world game shows where rules may be bent for entertainment.
  - The models do not discuss that the 'standard' assumptions (e.g., uniform random choice by host when indifferent) are not logically entailed by the problem statement and require justification, not just assumption.
  - No model explores the distinction between unconditional probability of winning by always-switching (2/3) and the conditional probability given the specific door opened, which can vary if the host has a systematic bias (e.g., preferring higher-numbered doors) even under correct overall strategy.

**partial_coverage:**
  - {"models": ["z-ai/glm-5.1"], "point": "The host's action is not random—it is constrained by the rules and injects information that breaks symmetry between the doors."}
  - {"models": ["z-ai/glm-5.1"], "point": "The 100-door analogy makes the advantage of switching more intuitive: switching wins with probability (N-1)/N when the host opens N-2 losing doors."}
  - {"models": ["z-ai/glm-5.1"], "point": "Switching wins if the initial choice was wrong (probability 2/3), loses if it was right (probability 1/3), so the win probability when switching equals the prior probability that the initial choice was wrong."}

### C5_smartpanel_dumbjudge
_умная панель + глупый судья_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b | cost=$0.0394 | 248.7s | ptok=18666 ctok=3681 | retries=0

**consensus:**
  - Switching doors gives a 2/3 chance of winning, staying gives 1/3
  - Host's knowledge and constrained actions influence probabilities
  - Bayesian reasoning and case analysis validate the 2/3 probability

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "z-ai/glm-5.1", "insight": "Grouping intuition explaining how initial probabilities transfer to the remaining door"}
  - {"model": "moonshotai/kimi-k2.6", "insight": "Explicit joint probability table with Bayesian calculation steps"}

**blind_spots:**
  - Assumption that host always offers switch and reveals a goat
  - Psychological counterintuitive nature of the problem
  - Historical context of the problem's popularization and misinterpretations

**partial_coverage:**
  - {"models": ["deepseek/deepseek-v4-pro", "z-ai/glm-5.1"], "point": "Discussion of real game show variations where host behavior might alter probabilities"}

### C5inv_dumbpanel_smartjudge
_глупая панель + умный судья (qwen-2.5-7b → gemma-3-12b-it)_  
panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1 | cost=$0.0218 | 309.4s | ptok=18946 ctok=3781 | retries=0

**consensus:**
  - Switching doors yields a 2/3 probability of winning; staying yields 1/3 — verified correct under the standard Monty Hall assumptions.
  - The host's knowledge of the car's location and deliberate action of revealing a goat is the mechanism that creates the asymmetry; it is not a random elimination.
  - The intuitive 50/50 reasoning after one door is opened is a fallacy under standard assumptions, because it ignores the information conveyed by the host's constrained choice.

**contradictions:**
  - {"topic": "Probability after host reveals a goat", "stances": [{"model": "z-ai/glm-4.7-flash Model B (The Skeptic)", "stance": "Probability resets to 50/50 because only two doors remain; the host's knowledge does not transfer probability."}, {"model": "All other sub-models across all three responses", "stance": "Probability remains 1/3 for staying and 2/3 for switching; the host's constrained action concentrates the 2/3 probability onto the remaining unopened door."}]}

**unique_insights:**
  - {"model": "z-ai/glm-4.7-flash Model C", "insight": "Framing the problem explicitly through the lens of information theory — the host's reveal as an information-conveying act that shifts the probability distribution, rather than merely a passive elimination."}
  - {"model": "z-ai/glm-4.7-flash Model A", "insight": "Exhaustive sample-space enumeration (Car-Goat-Goat, Goat-Car, Goat-Goat-Car) to prove the 2/3 result, rather than relying solely on the probability-concentration intuition."}

**blind_spots:**
  - No model explicitly uses Bayes' theorem or formal conditional probability notation to derive the result, which would be the most rigorous proof method.
  - No model addresses the critical epistemic ambiguity: if the host randomly chose between doors 2 and 3 and happened to reveal a goat (rather than being constrained to always reveal a goat), the probability of winning by switching would be 1/2, not 2/3. The problem statement does not explicitly state the host's protocol — only what happened in this instance.
  - No model discusses the asymmetry in host behavior when the car is behind different doors: if the car is behind door 2, the host MUST open door 3; if the car is behind door 1, the host has a choice between doors 2 and 3. This asymmetry is the structural reason the probabilities differ from 50/50.
  - No model generalizes to n doors (where the host opens n−2 goat doors), which powerfully demonstrates why switching is advantageous.
  - No model mentions the historical Marilyn vos Savant controversy, which empirically demonstrated how even trained mathematicians fall for the 50/50 fallacy.

**partial_coverage:**
  - {"models": ["qwen/qwen3-8b"], "point": "Assumptions about host behavior (e.g., always opening a goat door, always offering a switch) are critical to the solution and may not be explicitly stated in all formulations."}
  - {"models": ["z-ai/glm-4.7-flash Model A"], "point": "Explicit enumeration of the three equally likely sample-space scenarios (Car-Goat-Goat, Goat-Car-Goat, Goat-Goat-Car) to demonstrate switching wins in 2 of 3 cases."}
  - {"models": ["z-ai/glm-4.7-flash Model C"], "point": "Framing the advantage of switching as 'information gain' — the host's forced choice to reveal a goat provides new information that shifts probability."}
  - {"models": ["google/gemma-3-12b-it Model B"], "point": "Brief mention of psychological bias toward sticking with an initial decision."}

### C6_echo
_контроль: эхо-камера_  
panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507 | cost=$0.0217 | 77.8s | ptok=7586 ctok=1011 | retries=0

**consensus:**
  All models agree that the contestant should switch to door 2. They unanimously state that the probability of winning the car by switching is 2/3, while the probability of winning by staying with door 1 is 1/3. The reasoning centers on the initial probability distribution and the host's informed action.

**contradictions:**
  _(пусто)_

**unique_insights:**
  _(пусто)_

**blind_spots:**
  _(пусто)_

**partial_coverage:**
  _(пусто)_

### C3_cn_small
_всё мелкое_  
panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b | cost=$0.0224 | 252.8s | ptok=13094 ctok=2283 | retries=0

**consensus:**
  - Switching to door 2 gives a 2/3 probability of winning, while staying with door 1 gives a 1/3 probability. This is verified against the standard solution to the Monty Hall problem.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "qwen/qwen3.6-27b", "insight": "Used a '100 doors' analogy and frequency analysis to demonstrate the probabilistic advantage of switching in an intuitive, non-formal way."}

**blind_spots:**
  - No model explicitly addressed the epistemological basis for rejecting the '50/50' intuition, such as clarifying that the host’s constrained knowledge-based action increases the conditional probability for the unchosen door, not just random elimination.

**partial_coverage:**
  - {"models": ["qwen/qwen3-32b"], "point": "The problem’s solution hinges on the assumption that the host’s behavior is strictly constrained (e.g., always opening a goat door and never the contestant’s initial choice). Other models did not explicitly mention this dependency."}


---
## BASELINE (одиночная модель, без fusion)

### B_cn  (model=deepseek-v4-pro | cost=$0.0013 | 18.1s)
This is the classic **Monty Hall problem**.  

---

### **Should you switch?**  
**Yes, you should switch.**  

---

### **Exact probabilities**
- **Probability of winning if you stay** with door 1: \( \frac{1}{3} \)  
- **Probability of winning if you switch** to door 2: \( \frac{2}{3} \)  

---

### **Reasoning**
1. **Initial choice**:  
   When you first pick door 1, there’s a \( \frac{1}{3} \) chance the car is behind it, and a \( \frac{2}{3} \) chance the car is behind one of the other two doors (doors 2 or 3).

2. **Host’s action**:  
   The host, who knows where the car is, always opens a door with a goat from the two you didn’t pick.  
   - If your initial pick was wrong (probability \( \frac{2}{3} \)), the car is behind one of the other two doors. The host reveals the goat behind the other losing door, meaning the remaining unopened door must have the car.  
   - If your initial pick was correct (probability \( \frac{1}{3} \)), the host randomly opens one of the other two goat doors, and switching would make you lose.

3. **Conclusion**:  
   Switching wins exactly when your initial guess was wrong, which happens with probability \( \frac{2}{3} \). Staying wins only when your initial guess was right, which happens with probability \( \frac{1}{3} \).

### B_west  (model=gpt-5.2 | cost=$0.0053 | 6.5s)
Yes—you should switch.

### Probabilities
- **If you stay with door 1:** probability of winning the car = **1/3**
- **If you switch to door 2:** probability of winning the car = **2/3**

### Why (reasoning)
When you first pick **door 1**, there are two mutually exclusive cases:

1. **You initially picked the car** (probability **1/3**).  
   - Then doors 2 and 3 both have goats.  
   - The host opens one goat door (here, door 3).  
   - If you **switch**, you move off the car and **lose**.  
   - If you **stay**, you **win**.

2. **You initially picked a goat** (probability **2/3**).  
   - Then the car is behind either door 2 or door 3.  
   - The host **must** open the other goat door (he can’t reveal the car).  
   - Since he opened door 3 and showed a goat, the car must be behind the only unopened door you didn’t pick: **door 2**.  
   - If you **switch**, you **win**.  
   - If you **stay**, you **lose**.

So:
- Switching wins in case (2), which happens **2/3** of the time.
- Staying wins only in case (1), which happens **1/3** of the time.

### Key insight
The host’s action is **not random**: he uses his knowledge to always reveal a goat. That “filters” the two-door situation so that the entire **2/3** probability mass of “you initially chose wrong” transfers to the remaining unopened door.
