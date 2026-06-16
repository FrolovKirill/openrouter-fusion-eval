# sci-01 — Battery energy density claim
**Block:** scientific

**Prompt:**
A startup claims their lithium-sulfur battery achieves 800 Wh/kg at room temperature with <10% capacity loss over 1000 cycles. Evaluate: (1) Is this plausible given the current state of the field? (2) What are the most likely ways this claim is misleading or cherry-picked? (3) What key evidence is missing before taking this seriously?

---
## FUSION-конфиги (judge-анализ; responses вынесены в resp_*.md)

### C1_west_closed
_западный закрытый фронтир_  
panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2 | cost=$0.2178 | 215.5s | ptok=23947 ctok=1412 | retries=0

**consensus:**
  The panel overwhelmingly agrees that the claim of simultaneously achieving 800 Wh/kg and 1,000 cycles with <10% capacity loss at room temperature is highly implausible given the current state of lithium-sulfur (Li-S) battery technology. The claim appears to rely on inherently contradictory electrochemical and engineering requirements that have not been reconciled in any known literature or commercial cell.

**contradictions:**
  There are no significant contradictions among the responses. All models recognize the fundamental implausibility of the claim. Minor variances exist only in their analytical focus, with some highlighting the electrochemical limitations of Li-S systems and others emphasizing deceptive startup marketing and metric manipulation.

**unique_insights:**
  - Startups frequently engage in 'metric mixing', reporting the energy density from a highly-loaded, single-use cell while citing the cycle life from a separate, heavily 'flooded' low-loading coin cell.
  - Energy density claims of 800 Wh/kg are almost certainly calculated at the active-material level (theoretical sulfur capacity) rather than the packaged cell level, ignoring the critical mass of electrolytes, current collectors, and casing.
  - The inherent tradeoff in Li-S systems is dictated by the Electrolyte-to-Sulfur (E/S) and negative-to-positive (N/P) ratios; high energy density requires 'lean' ratios, which immediately trigger rapid cell death due to electrolyte depletion and polysulfide shuttling.

**blind_spots:**
  - None of the models can definitively rule out a proprietary, paradigm-shifting breakthrough (e.g., a completely novel solid-state architecture that perfectly halts the shuttle effect) since the specific startup's technology is unknown.
  - The analysis does not deeply explore volumetric energy density (Wh/L), which is historically a massive commercial bottleneck for Li-S viability due to the low density of sulfur.

**partial_coverage:**
  The models correctly identify missing testing parameters but only partially cover the impact of applied C-rates, missing the possibility that the startup might have run the 1,000-cycle test at commercially useless, ultra-slow current densities (e.g., C/50) to artificially prevent degradation.

### C2_cn_open
_открытый китайский фронтир (умн+умн)_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507 | cost=$0.2327 | 505.3s | ptok=39947 ctok=9814 | retries=0

**consensus:**
  - The claim of 800 Wh/kg with <10% capacity loss over 1000 cycles is not plausible given the current state of the field, as the highest verified pouch-cell energy density with cycling data is 441 Wh/kg, and cells approaching 800 Wh/kg have only been cycled for 5 cycles.
  - The combination of high energy density and long cycle life in lithium-sulfur batteries remains mutually exclusive due to fundamental trade-offs involving electrolyte-to-sulfur (E/S) ratio, sulfur loading, and polysulfide shuttle.
  - Energy density claims near 800 Wh/kg often exclude the mass of pouch film, tabs, or other inactive components, inflating the figure beyond realistic cell-level performance.
  - Independent third-party validation and full component mass accounting are essential before taking such claims seriously.

**contradictions:**
  - {"topic": "Definition of cell-level energy density", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "800 Wh/kg may be calculated excluding pouch film and tabs, which is misleading for real-world applications."}, {"model": "z-ai/glm-5.1", "stance": "Reporting 800 Wh/kg while excluding inert components like packaging is a common misleading practice and invalid for commercial relevance."}, {"model": "moonshotai/kimi-k2.6", "stance": "Whether the ADEKA SPAN result (~800 Wh/kg excluding pouch/tabs) counts as valid cell-level energy density is a matter of definitional dispute."}, {"model": "evidence", "stance": "Per the 2025 Nature Communications benchmarking study, true cell-level energy density must include all components; the 800 Wh/kg figure is only achieved when excluding pouch film and tabs, making such claims non-comparable to practical cells."}]}
  - {"topic": "Feasibility of combining high energy and long cycle life", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "The trade-off is so severe that no published work reconciles 800 Wh/kg with 1000 cycles; the claim is an extreme outlier."}, {"model": "z-ai/glm-5.1", "stance": "Energy density and durability operate on orthogonal design axes; pushing one compromises the other, making the claim implausible."}, {"model": "moonshotai/kimi-k2.6", "stance": "At very low C-rates needed for 800 Wh/kg, transport-driven degradation (shuttle) is worse due to longer cycle duration, making 1000 cycles harder to achieve."}, {"model": "evidence", "stance": "The 2025 Nature Communications analysis of 866 plots from 184 studies confirms a strong inverse correlation (r = -0.8) between E/S ratio and specific energy, and that high sulfur loading (>6 mg/cm²) reduces reversible capacity, making simultaneous optimization unattainable with current architectures."}]}

**unique_insights:**
  - {"model": "moonshotai/kimi-k2.6", "insight": "At very low C-rates required for 800 Wh/kg, transport-driven degradation (polysulfide shuttle) accumulates more per cycle due to longer duration, meaning 1000 cycles is actually harder to achieve than at moderate C-rates — contrary to the intuition that slower cycling is gentler."}
  - {"model": "z-ai/glm-5.1", "insight": "The E/S ratio is the strongest predictor of specific energy (r = -0.8), and sulfur loading above ~6 mg/cm² sharply reduces reversible capacity due to transport limitations, making 800 Wh/kg with high cycle life structurally improbable."}
  - {"model": "deepseek/deepseek-v4-pro", "insight": "Startups may use SPAN cathodes to achieve long cycle life while separately reporting high energy density from a different cell configuration, then present them as concurrent achievements without disclosing the incompatibility."}

**blind_spots:**
  - None of the models addressed recent advances in thermoresponsive SEI designs that may improve both safety and cycle life, as demonstrated in a 2025 Energy & Environmental Science study showing 78% retention after 160 cycles in 523 Wh/kg pouch cells.
  - No model considered all-solid-state lithium-sulfur batteries using Li8VSy nanocomposites, which theoretically offer 515 Wh/kg but degrade rapidly (~80% retention after 10 cycles), highlighting a different technological pathway that still falls short of the claim.
  - The role of manufacturing scalability and cost, particularly for exotic materials like N-doped aerogels or fluorinated electrolytes, was not fully explored as a constraint on commercial viability.
  - No model explicitly referenced or contextualized the 2025 Nature Communications benchmarking study’s median of 298 Wh/kg for practical cells, despite its centrality to the state-of-the-art assessment.

**partial_coverage:**
  - {"models": ["deepseek/deepseek-v4-pro"], "point": "The use of SPAN cathodes may enable longer cycle life by eliminating polysulfide shuttle, but at the cost of lower energy density, making their combination with 800 Wh/kg implausible."}
  - {"models": ["moonshotai/kimi-k2.6"], "point": "Low C-rates needed for high energy density actually exacerbate transport-driven degradation like polysulfide shuttle because each cycle lasts longer, increasing time for diffusion and loss."}
  - {"models": ["z-ai/glm-5.1"], "point": "Coin cell results with excessive electrolyte and low sulfur loading do not translate to pouch cells, and using them to infer commercial viability is invalid."}

### C5_smartpanel_dumbjudge
_умная панель + глупый судья_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b | cost=$0.2240 | 408.2s | ptok=27171 ctok=6202 | retries=0

**consensus:**
  - The claim of 800 Wh/kg with <10% capacity loss over 1000 cycles is not plausible given current peer-reviewed benchmarks
  - Non-standard weight accounting (e.g., excluding cell components) is a common misleading practice
  - High energy density and long cycle life are fundamentally at odds in Li-S systems due to polysulfide shuttle and electrolyte depletion

**contradictions:**
  - {"topic": "Peer-reviewed benchmarks", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "ADEKA's 761 Wh/kg (2024) is best documented"}, {"model": "glm-5.1", "stance": "Nature Communications 2025 study shows 441 Wh/kg as highest verified"}, {"model": "moonshotai/kimi-k2.6", "stance": "Stanford/Nature Energy modeling shows 800 Wh/kg requires unachieved parameters"}]}
  - {"topic": "Cycle life metrics", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "1000 cycles at >700 Wh/kg is 6× longer than documented"}, {"model": "glm-5.1", "stance": "Nature Communications 2025 shows 215–394 cycles at similar densities"}, {"model": "moonshotai/kimi-k2.6", "stance": "1000 cycles at 498 Wh/kg is achievable in small cells"}]}

**unique_insights:**
  - {"model": "deepseek/deepseek-v4-pro", "insight": "Detailed table comparing claimed metrics against peer-reviewed benchmarks with quantified gaps"}
  - {"model": "moonshotai/kimi-k2.6", "insight": "Identifies specific mathematical modeling requirements for 800 Wh/kg (E/S ≤1.2 µL mg⁻¹, N/P ≤1.2)"}

**blind_spots:**
  - Recent 2025–2026 breakthroughs in polysulfide confinement materials
  - Economic feasibility and manufacturing scalability of claimed parameters
  - Environmental impact and recycling challenges of lithium-sulfur systems

**partial_coverage:**
  - {"models": ["glm-5.1"], "point": "Mentions 2026 study showing practical energy densities drop dramatically when electrolyte included"}
  - {"models": ["moonshotai/kimi-k2.6"], "point": "Discusses 'four high four low' criteria for practical Li-S systems"}

### C5inv_dumbpanel_smartjudge
_глупая панель + умный судья (qwen-2.5-7b → gemma-3-12b-it)_  
panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1 | cost=$0.1294 | 311.1s | ptok=24111 ctok=5217 | retries=0

**consensus:**
  - Simultaneously achieving 800 Wh/kg AND <10% capacity loss over 1000 cycles is highly implausible given the fundamental tradeoff between energy density and cycle life in Li-S batteries.
  - The polysulfide shuttle effect remains a primary degradation mechanism in conventional Li-S cells, and any claim of long cycle life must address how it is suppressed.
  - Electrolyte-to-sulfur (E/S) ratio is a critical parameter: lean electrolyte (<5 µL/mg) is required for high gravimetric energy density, but degrades cycling performance.
  - The claim likely involves cherry-picking or combining metrics from different cell configurations rather than a single achievable design point.
  - Third-party independent verification under realistic conditions is essential before taking the claim seriously.
  - Sulfur volume expansion (~80%) during cycling is a fundamental mechanical challenge that any long-cycle-life design must address.

**contradictions:**
  - {"topic": "Current practical energy density of Li-S pouch cells", "stances": [{"model": "qwen/qwen3-8b", "stance": "Practical values are 150-300 Wh/kg — badly outdated; real pouch cells have achieved 456 Wh/kg in 10Ah cells (Li-S Energy, Oct 2024) and 713 Wh/kg (ADEKA, Nov 2024) at 0.1C."}, {"model": "evidence", "stance": "Li-S Energy (Oct 2024) demonstrated 456 Wh/kg in 10Ah pouch cells after formation; ADEKA (Nov 2024) achieved 713 Wh/kg (total cell mass) at 0.1C in pouch cells."}]}
  - {"topic": "Whether 800 Wh/kg is beyond current capabilities", "stances": [{"model": "google/gemma-3-12b", "stance": "800 Wh/kg is 'far beyond current capabilities' and 'orders of magnitude better than realistically achievable' — overstated."}, {"model": "z-ai/glm-4.7-flash", "stance": "700-750 Wh/kg has been achieved in pouch cells, making 800 Wh/kg ambitious but not 'far beyond' — more accurate."}, {"model": "evidence", "stance": "ADEKA achieved 761 Wh/kg (total cell) and 800 Wh/kg (excluding pouch film and tabs) in a real pouch cell at 0.05C (Nov 2024), showing the energy density alone is near the boundary of demonstrated performance, not orders of magnitude away."}]}
  - {"topic": "Current achievable cycle life in Li-S cells", "stances": [{"model": "qwen/qwen3-8b", "stance": "Most studies report cycle life <200 cycles — incomplete and misleading."}, {"model": "evidence", "stance": "Zhang et al. (2024, Energy Environ. Sci.) achieved 1000 cycles with 99% capacity retention in SPAN‖Gr pouch cells, and 1031 cycles with 82% retention in Ah-level pouch cells. However, this used a graphite anode, not Li metal, which fundamentally changes the energy density tradeoff."}]}
  - {"topic": "Whether <10% capacity loss over 1000 cycles is near current capabilities", "stances": [{"model": "z-ai/glm-4.7-flash", "stance": "<10% loss over 1000 cycles is 'at the upper end of current capabilities' — misleadingly implies this is achievable alongside high energy density."}, {"model": "evidence", "stance": "The only Li-S pouch cell achieving ~1000 cycles with <10% loss used a graphite anode (not Li metal) and SPAN cathode chemistry, resulting in much lower energy density. No Li-metal-based Li-S cell has demonstrated this combination."}]}

**unique_insights:**
  - {"model": "qwen/qwen3-8b", "insight": "Selenium-sulfur (Se-S) chemistry as a potential novel approach to suppress the polysulfide shuttle while maintaining high energy density."}
  - {"model": "google/gemma-3-12b", "insight": "The polysulfide shuttle and lithium dendrite formation are coupled problems — polysulfide corrosion of the Li anode creates uneven surfaces that promote dendrites, which in turn expose fresh Li to further polysulfide attack, creating a self-accelerating degradation loop."}
  - {"model": "z-ai/glm-4.7-flash", "insight": "Achieving 800 Wh/kg would require simultaneous breakthroughs in four separate domains (polysulfide suppression, sulfur utilization >90%, E/S ratio <10 µL/mg, and dendrite elimination), making the probability of all converging in one design extremely low."}

**blind_spots:**
  - No model mentions the ADEKA ALIS-PC result (Nov 2024): 761 Wh/kg (total cell mass) in a real pouch cell at 0.05C — the closest demonstrated precedent to the 800 Wh/kg claim, which critically shows that near-800 Wh/kg is achievable only at extremely low C-rates with very limited cycle life.
  - No model identifies C-rate as the most likely cherry-picking parameter: the ADEKA ultra-high-energy-density cell operates at only 0.05C, making it functionally impractical. The startup's claim omits C-rate entirely.
  - No model mentions the 2024 SPAN‖Gr pouch cell (Zhang et al.) achieving 1000 cycles with 99% retention — the key counterexample showing that long cycling in Li-S chemistry requires switching from Li-metal to graphite anodes, which eliminates the energy density advantage. This is the exact tradeoff the startup's claim violates.
  - No model discusses SPAN (sulfurized polyacrylonitrile) chemistry as a specific category: it eliminates the polysulfide shuttle but has lower specific capacity than elemental sulfur, meaning SPAN-based cells cannot simultaneously achieve 800 Wh/kg.
  - No model identifies that 800 Wh/kg excluding pouch film and metal tabs (a specific cherry-picking method actually used in published literature, per ADEKA paper) is a likely way the startup's claim is inflated.
  - No model discusses the cell-level vs. pack-level energy density distinction: even 800 Wh/kg at cell level may translate to <500 Wh/kg at pack level due to BMS, thermal management, and structural packaging.
  - No model addresses the depth-of-discharge (DOD) manipulation: cycling only between partial DOD windows (e.g., 20-80%) dramatically extends cycle life but misrepresents usable capacity and energy density.
  - No model mentions the excess lithium factor: the N/P ratio (capacity ratio of anode to cathode) is often hidden, and excess Li adds dead weight that reduces true cell-level energy density while enabling longer cycling.

**partial_coverage:**
  - {"models": ["qwen/qwen3-8b"], "point": "E/S ratio must be <3 µL/mg to achieve high practical energy density, and electrolyte can constitute >70% of cell mass at high E/S ratios."}
  - {"models": ["google/gemma-3-12b"], "point": "Non-standard testing protocols (e.g., very slow C-rates, shallow cycling, excluding packaging mass) can artificially inflate reported performance metrics."}
  - {"models": ["z-ai/glm-4.7-flash"], "point": "Distinction between coin cells and full-sized pouch cells is critical; coin cell results rarely translate to pouch cell performance."}
  - {"models": ["qwen/qwen3-8b", "z-ai/glm-4.7-flash"], "point": "Excess lithium anode thickness and N/P ratio as hidden weight factors that can be manipulated in energy density calculations."}

### C6_echo
_контроль: эхо-камера_  
panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507 | cost=$0.0586 | 145.8s | ptok=42747 ctok=3250 | retries=0

**consensus:**
  - The startup claim of achieving 800 Wh/kg at room temperature with <10% capacity loss over 1000 cycles in lithium-sulfur (Li-S) batteries is considered implausible based on the current state of the field.
  - The practical gravimetric energy density for Li-S batteries is currently around 400-500 Wh/kg, with 700 Wh/kg being an optimistic theoretical benchmark for pouch cells; 800 Wh/kg has not been substantiated in commercially relevant configurations.
  - <10% capacity loss over 1000 cycles in real-world pouch cell conditions has not been demonstrated in the literature; reported stable cycling is generally below hundreds of cycles or under idealized coin-cell conditions.
  - Common ways such a claim might be misleading include testing in coin cells (vs. commercially relevant pouch cells), using low sulfur loading, high electrolyte to sulfur (E/S) ratios, and excessive lithium anodes.
  - Critical missing evidence includes results from Ah-level pouch cells, lean electrolyte conditions (E/S < 5 μL mg⁻¹), areal sulfur loading >5 mg cm⁻², and proper accounting of all cell components in energy density calculations.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - Some solid-state Li-S systems using modified sulfides (e.g., sulfur iodide) report room-temperature energy densities above 800 mAh/g and >99% Coulombic efficiency over 400 cycles, though at very low active material loading (40 wt.%), which does not translate to >800 Wh/kg at the cell level.
  - Quasi-solid-state or lean-electrolyte pouch cells have demonstrated energy densities around 400–450 Wh/kg, but with significantly higher capacity fade than the claimed <10% over 1000 cycles.
  - While a 417 Wh/kg pouch cell was reported with over 400 cycles and a stable Coulombic efficiency of 99.55%, this does not reach the claimed energy density, cycle life, or capacity retention thresholds.

**blind_spots:**
  _(пусто)_

**partial_coverage:**
  - The evidence from academic reviews and recent publications consistently confirms limitations related to the shuttle effect, dendrite growth, electrolyte volume, and cell format but does not report any successful 1000-cycle demonstration meeting both the 800 Wh/kg and <10% degradation targets.
  - The reviews emphasize the large performance gap between coin cells and pouch cells, underscoring that coin cell performance cannot be extrapolated to real-world applications.

### C3_cn_small
_всё мелкое_  
panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b | cost=$0.0693 | 445.7s | ptok=21691 ctok=4506 | retries=0

**consensus:**
  - The claim of 800 Wh/kg energy density with <10% capacity loss over 1000 cycles in a lithium-sulfur battery is highly implausible for practical full cells under real-world conditions, despite isolated lab demonstrations achieving parts of the claim under non-scalable parameters.
  - There is a well-known tradeoff in Li-S technology between high energy density and long cycle life, making simultaneous achievement of both metrics a major unsolved challenge.
  - Startup claims of this nature often rely on non-representative testing conditions such as half-cell configurations, excessive electrolyte volumes, low C-rates, or selective reporting of active-material-only energy density.

**contradictions:**
  - {"topic": "Plausibility of the claim under lab vs practical conditions", "stances": [{"model": "qwen/qwen3.6-27b", "stance": "The claim is implausible in practical cells but possible in isolated lab studies with unrealistic conditions (e.g., 0.05C rates, excluded packaging)."}, {"model": "qwen/qwen3-32b", "stance": "Claims cite 2023 studies (e.g., Li3PS4 electrolytes) achieving 1004.6 mAh/g retention over 800 cycles, implying plausibility if similar approaches are scaled."}, {"model": "evidence", "stance": "Recent 2024-2025 field data (e.g., ADEKA) confirms Li-S struggles to maintain 800 Wh/kg beyond ~10 cycles with practical cell design."}]}
  - {"topic": "Achievability of 1,000 cycles with <10% loss", "stances": [{"model": "z-ai/glm-4.7-flash", "stance": "Requires >0.02% per-cycle fade rate, but typical Li-S cells degrade 0.1% per cycle (0.1% * 1000 = 100% loss)."}, {"model": "qwen/qwen3-32b", "stance": "Recent fluorinated electrolyte systems (F4DMB-S6MILE) show 4.3% degradation over 15 cycles, suggesting theoretical feasibility under controlled lab conditions."}]}

**unique_insights:**
  - {"model": "z-ai/glm-4.7-flash", "insight": "The industry's 0.02% per-cycle fade rate requirement vs. typical 0.1% degradation highlights a ~5x performance gap in cycle life for Li-S adoption."}
  - {"model": "qwen/qwen3-32b", "insight": "Fluorinated electrolytes (F4DMB-S6MILE) enable 1526 mAh/g retention at 60°C but degrade precipitously to ~500 mAh/g under practical C-rates (>0.1C), suggesting claims are rate-dependent."}

**blind_spots:**
  - Lack of analysis on calendar life (non-cycling capacity fade) as a killer metric for Li-S systems after prolonged storage at room temperature.
  - Failure to address third-party verification hurdles like independent Coulombic efficiency testing for lithium anode degradation tracking.
  - No models examine safety risks of lithium-sulfur (e.g., dendrite growth in lean electrolyte conditions) when optimizing for high energy density.

**partial_coverage:**
  - {"models": ["qwen/qwen3.6-27b", "z-ai/glm-4.7-flash"], "point": "Need for third-party verification of critical parameters: sulfur loading (>6 mg/cm²), electrolyte-to-sulfur ratio (<5 µL/mg), and statistical significance of cycle life data beyond initial 100 cycles."}
  - {"models": ["qwen/qwen3-32b"], "point": "New electrolyte design (moderate LiPS solubility at 50-200 mM) as a potential path to balance energy density and cycle stability via suppressed polysulfide shuttling."}


---
## BASELINE (одиночная модель, без fusion)

### B_cn  (model=deepseek-v4-pro | cost=$0.0049 | 23.7s)
_(пустой ответ)_

### B_west  (model=gpt-5.2 | cost=$0.0211 | 29.4s)
## (1) Plausibility vs. current state of the field

**As stated (800 Wh/kg at room temperature *and* <10% capacity loss over 1000 cycles), it is not plausible for a *practical, cell-level* lithium–sulfur battery in 2025–2026 without extraordinary, independently verified evidence.**

Why:

- **Cell-level specific energy:**  
  Li–S has a very high *theoretical* specific energy (often quoted using sulfur active material only), but **real cells are dominated by inactive mass** (electrolyte, current collectors, separator, binder, conductive carbon, tabs, pouch/can, and—critically—excess lithium metal and electrolyte needed to manage shuttle and kinetics).  
  Publicly demonstrated **pouch-cell** Li–S results that are credible tend to cluster roughly in the **300–500 Wh/kg** range under conditions that still don’t simultaneously meet long life, lean electrolyte, high areal loading, and realistic N/P ratios. **800 Wh/kg at the cell level is beyond what’s generally considered demonstrated**.

- **Cycle life at high energy is the hard part:**  
  Li–S degradation mechanisms (polysulfide shuttle, lithium metal corrosion/dendrites, cathode structural changes, electrolyte consumption) make **long cycle life especially difficult under “high-energy” conditions** (high sulfur loading, lean electrolyte, limited lithium excess).  
  **1000 cycles with <10% loss is more reminiscent of Li-ion-class durability**, and for Li–S would represent a step-change breakthrough that would likely be widely visible in peer-reviewed and third-party testing.

Net: **It’s not impossible in principle**, but **it’s far outside normal verified performance envelopes** when all metrics are made practical and comparable.

---

## (2) Most likely ways the claim is misleading / cherry-picked

These claims most often hinge on **how “Wh/kg” and “cycle life” are defined** and the **test conditions**:

### A. “800 Wh/kg” is not at the *cell* level
Common reframes:
- **Cathode-only** (sulfur + host) specific energy, ignoring lithium, electrolyte, current collectors, separator, packaging.
- **Stack-only** (electrode stack without pouch/can, tabs, safety hardware).
- **“Projected” cell energy** from modeled assumptions (future lean-electrolyte design), not measured.

### B. Unrealistic electrolyte and lithium excess
Li–S can look great in the lab with:
- **High electrolyte-to-sulfur ratio (E/S)** (e.g., 10–20 µL/mg S), which inflates capacity and stability but **crushes practical Wh/kg**.
- **Very high N/P ratio** (lots of excess lithium metal), which stabilizes cycling but is **dead weight** and often unsafe/unscalable.

### C. Low areal loading / low areal capacity (coin-cell trap)
You can get long cycle life if the cathode is thin:
- Sulfur loading like **~1 mg/cm²** (or similarly low), giving low areal capacity.
- Results look excellent in % retention, but **don’t translate** to practical energy density or manufacturing-relevant electrodes.

### D. Gentle cycling conditions that hide failure modes
- Very low C-rate (e.g., C/20), narrow voltage windows, low depth-of-discharge.
- Cycling at low utilization (not accessing high-capacity regions where shuttle is worse).
- Results reported only at one “sweet spot” condition.

### E. “<10% loss over 1000 cycles” uses a favorable baseline
Common tricks:
- Using **capacity after formation/activation** as the reference, not initial.
- Reporting **best cell** out of many (survivorship bias).
- Reporting **capacity retention** while ignoring **coulombic efficiency**, self-discharge, or increasing impedance (energy efficiency collapse).

### F. They quote gravimetric energy but ignore volumetric energy and swelling
Li–S often has:
- **Electrode expansion**, electrolyte uptake, and stack swelling.  
  You can claim high Wh/kg but deliver poor Wh/L, poor mechanical stability, and short calendar life.

---

## (3) Key evidence missing before taking it seriously

To evaluate this credibly, you’d want **cell-level, independently reproducible data with full design and test transparency**:

### A. Clear definition of “800 Wh/kg”
Require:
- **Measured, not projected**, and explicitly stating whether it is:
  - full cell including packaging (preferred),
  - stack level,
  - or cathode-only.
- A **mass breakdown** (electrolyte mass, lithium mass, current collectors, separator, pouch/can, tabs).

### B. Practical electrode and
