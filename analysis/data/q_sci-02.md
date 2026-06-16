# sci-02 — Direct air capture cost claim
**Block:** scientific

**Prompt:**
A research team claims they've developed a direct air capture material that removes CO₂ at $50/ton with 95% efficiency using only solar energy, scalable to gigatons/year. Critically evaluate: what would need to be true for this to hold, what are the most likely failure modes, and what questions would you ask before believing it?

---
## FUSION-конфиги (judge-анализ; responses вынесены в resp_*.md)

### C1_west_closed
_западный закрытый фронтир_  
panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2 | cost=$0.2085 | 345.6s | ptok=20267 ctok=4285 | retries=0

**consensus:**
  - DAC at ~420 ppm requires processing very large air volumes per tCO2 captured (order ~10^3–10^4 tonnes of air per tonne CO2), so contactor pressure drop/fan energy and mass-transfer limits are first-order constraints at scale (verified by NASEM NETs 2018 energy breakdowns and multiple DAC engineering analyses).
  - "Solar-only" energy supply introduces intermittency; without storage or major oversizing it reduces capacity factor and tends to raise levelized $/t because CAPEX is amortized over fewer operating hours (consistent with standard project-finance/TEA practice and renewable capacity factors).
  - Gigaton-scale deployment is constrained by more than the capture material itself: it implies massive buildout of hardware, energy supply, and CO2 handling infrastructure (compression, transport, and durable storage), each of which can dominate cost and schedule (consistent with IEA/NASEM framing of DACCS system requirements).
  - Lab or prototype performance is unlikely to extrapolate directly: durability under real air (humidity swings, contaminants, particulates), maintenance, and replacement rates can dominate long-run cost and performance (supported by known sorbent degradation/fouling challenges discussed broadly in DAC literature and field experience).

**contradictions:**
  - {"topic": "Whether the claim would require violating/surpassing thermodynamic (second-law) limits", "stances": [{"model": "google/gemini-3.1-pro-preview", "stance": "Frames the claim as highly improbable under current thermodynamic paradigms and implies thermodynamic constraints are near-binding for $500/t at high capture."}, {"model": "x-ai/grok-4.3", "stance": "States the claim would require thermodynamic limits to be surpassed or ignored in practice."}, {"model": "evidence", "stance": "Thermodynamics sets a lower bound but does not rule out low dollar costs in principle: minimum work is ~0.45–0.5 GJ/tCO2 (~125–140 kWh/t) for typical capture specs (e.g., NASEM reports ~20 kJ/mol), so the barrier is practical irreversibility, CAPEX, and system integration—not violating the second law."}]}
  - {"topic": "Magnitude/character of the energy penalty for pushing capture fraction toward ~95%", "stances": [{"model": "google/gemini-3.1-pro-preview", "stance": "Suggests energy/cost rises sharply (described as effectively ‘exponential’) as capture approaches very high fraction due to reduced driving force."}, {"model": "x-ai/grok-4.3", "stance": "Does not quantify; generally treats high efficiency as thermodynamically problematic."}, {"model": "evidence", "stance": "Minimum work increases roughly logarithmically with separation ratio and depends on outlet specs; practical energy can increase strongly because of kinetics/pressure drop/heat management, but calling it ‘exponential thermodynamic energy’ is not generally correct (separation work scales with ln terms; irreversibility and equipment sizing drive steep practical penalties)."}]}
  - {"topic": "Implied fan/air-handling burden at gigaton scale (order-of-magnitude claims)", "stances": [{"model": "google/gemini-3.1-pro-preview", "stance": "Claims ~2–3 trillion tons of air must be moved per gigaton CO2 and that fan power would be ‘astronomical’."}, {"model": "x-ai/grok-4.3", "stance": "Agrees air-moving burden is immense but provides no numbers."}, {"model": "evidence", "stance": "Air mass per tCO2 is ~1/CO2 mass fraction ≈ 1/(~0.0006–0.0007) ≈ 1,500–1,700 t air per tCO2, i.e., ~1.5–1.7 trillion tons of air per GtCO2 (same order, but 2–3T is high); fan energy depends on pressure drop and can be large but is not necessarily ‘astronomical’ relative to global energy (NASEM gives mid-range fan electricity on the order of ~0.55–1.12 GJ/tCO2 for solid sorbents)."}]}
  - {"topic": "Whether $50/t is being treated as total system cost vs marginal/operating cost", "stances": [{"model": "google/gemini-3.1-pro-preview", "stance": "Argues $50/t likely reflects lab-scale marginal operating cost and omits CAPEX, degradation, and compression."}, {"model": "x-ai/grok-4.3", "stance": "States cost claims are rarely validated beyond lab scale but does not distinguish CAPEX vs OPEX explicitly."}, {"model": "evidence", "stance": "Current public market pricing and many TEAs place DACCS far above $50/t today (often hundreds of $/t); however, it is not logically impossible for OPEX-alone to approach $50/t under optimistic energy and efficiency assumptions—so any evaluation must clarify accounting boundaries (gross vs net removal, CAPEX included, financing assumptions, storage included)."}]}

**unique_insights:**
  - {"model": "google/gemini-3.1-pro-preview", "insight": "Treating “95% capture efficiency” as a red flag because high single-pass capture can be economically suboptimal in dilute separations; optimizing $/t can favor lower capture fractions with smaller contactors and lower pressure drop."}

**blind_spots:**
  - Ambiguity of “95% efficiency”: efficiency of what (single-pass capture fraction, sorbent utilization, energy efficiency vs thermodynamic minimum, or net CO2 removed after lifecycle emissions)? None of the models force a precise definition or propose a measurement protocol.
  - Net-removal accounting and MRV: how the team proves net-negative removal including PV manufacture, sorbent manufacture, replacements, maintenance logistics, and end-of-life disposal; panel gestures at LCA but does not specify required data/standards.
  - Heat vs electricity form-factor: many DAC concepts need substantial low-grade heat; “solar-only” could mean PV electricity, solar thermal, or both, with very different efficiencies/costs and storage options—this is not interrogated.
  - Financing and cost of capital: $/t at gigaton scale is highly sensitive to WACC, plant lifetime, uptime, and learning curves; models mention CAPEX qualitatively but do not ask for specific financing assumptions or bankability evidence.
  - Storage permanence and capacity: geologic storage site availability, injectivity limits, monitoring for leakage, and the pace of Class VI permitting/buildout; models mention “storage” but not the hard deployment constraint at Gt/yr.
  - System-level integration constraints at Gt/yr: supply chains for fans, contactors, compressors, pipelines, wells; workforce and construction rates; grid interconnection (even for solar-only, to build and operate auxiliaries).
  - Performance under realistic atmospheric contaminants: ozone, SOx/NOx, aerosols, organics, sea salt; models mention poisoning in passing but do not specify test conditions, acceptable degradation rates, or mitigation costs.
  - Spatial/temporal mismatch: where high solar resource coincides (or not) with viable storage basins and water availability; transport distances and their cost/energy are not analyzed.
  - Opportunity cost of solar energy: whether using scarce clean electricity/land for DAC is optimal compared with direct decarbonization, and how that affects real-world adoption at scale.

**partial_coverage:**
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "Notes that very high single-pass capture (e.g., 95%) may be economically non-optimal versus lower capture fractions due to mass-transfer/energy tradeoffs."}
  - {"models": ["google/gemini-3.1-pro-preview", "x-ai/grok-4.3"], "point": "Highlights sorbent supply-chain and scaling bottlenecks (availability of precursor chemicals/metals, manufacturing scale, and embodied impacts)."}
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "Calls out downstream CO2 compression/transport/storage as potentially adding large additional cost beyond capture."}
  - {"models": ["google/gemini-3.1-pro-preview", "x-ai/grok-4.3"], "point": "Mentions land-use, permitting, and regulatory constraints as important for gigaton deployment, but without detailed quantification."}
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "Raises water/humidity interactions (co-adsorption of water, stripping loads) and dust fouling risk for desert solar siting."}

### C2_cn_open
_открытый китайский фронтир (умн+умн)_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507 | cost=$0.1658 | 329.7s | ptok=38159 ctok=3154 | retries=0

**consensus:**
  The claim of a DAC material capturing CO₂ at $50/ton with 95% efficiency using solar energy and scalable to Gt/year is extraordinarily ambitious. Current DAC costs range from $200–$600/ton, with the thermodynamic minimum energy alone costing ~$2–$5/ton at ideal efficiency, yet real systems operate at 5–10× the thermodynamic limit. The $50/ton figure is not thermodynamically impossible but would require a revolutionary material and process that operates far closer to theoretical limits than any demonstrated gas separation system. Recent company announcements (e.g., Prometheus Fuels) have made similar $50/ton claims using electrochemical approaches that bypass traditional thermal regeneration, but these remain unvalidated at scale and lack peer-reviewed detail. The consensus from available literature is that while solar-powered DAC is a promising direction, achieving $50/ton at Gt/year scale requires solving multiple compounding challenges simultaneously—energy efficiency, sorbent durability, manufacturing scale, and system integration—each of which has historically proven far more difficult than initial lab results suggest.

**contradictions:**
  - The claim of 95% efficiency conflicts with thermodynamic analysis showing that deeper CO₂ scrubbing increases irreversibility and energy demand per ton captured; most DAC designs optimize at 50–75% capture fraction to minimize levelized cost.
  - The $50/ton claim contradicts peer-reviewed estimates placing DAC costs at $100–$1,000/ton even with optimistic learning curves, and is 4–12× lower than operational DAC plants today.
  - Scaling to Gt/year using only solar energy implies either a direct photochemical process (bypassing electricity generation) or massive overbuild of solar capacity with storage, creating tension with the low cost claim given solar intermittency.
  - The implied material stability contrasts sharply with published degradation studies showing amine-based sorbents losing 40–94% capacity under realistic cycling conditions with oxygen, CO₂-induced urea formation, and trace impurities.

**unique_insights:**
  - A $50/ton DAC system that genuinely works would have an energy budget of roughly $10–15/ton for solar electricity (assuming ~500–700 kWh/ton at $0.02–0.03/kWh), leaving $35–40/ton for capital, labor, maintenance, and sorbent replacement. This implies either an energy consumption near 200–300 kWh/ton (within 2–3× of thermodynamic minimum) or a direct solar-thermal/photochemical process that avoids electricity conversion losses entirely.
  - The '95% efficiency' figure is ambiguous and strategically potent: if it refers to one-pass CO₂ capture efficiency rather than overall energy efficiency, the energy penalty could still be severe. High capture fractions exponentially increase contactor size and pressure drop costs.
  - If the material uses a moisture-swing or photo-base mechanism (as suggested by recent Nature Chemistry 2025 work on light-driven DAC), it could theoretically decouple regeneration from high-grade heat, but introduces new failure modes around humidity dependence and photon utilization efficiency.
  - The Gt/year scalability claim is the most fragile: producing enough sorbent material at that scale could require precursor chemicals at volumes exceeding current global production of certain amines, silica precursors, or specialty polymers.

**blind_spots:**
  - The research team's claim lacks specificity about the capture mechanism—is this solid sorbent, liquid solvent, electrochemical, or photochemical? Each has fundamentally different cost structures and failure modes.
  - No mention of water consumption, which is significant for many DAC processes (both as a reactant in moisture-swing systems and for sorbent washing/recovery).
  - The claim omits any discussion of CO₂ compression, purification, and storage/transport costs, which typically add $10–30/ton for geological storage and more for utilization pathways.
  - The land footprint for Gt/year scale is not addressed: even optimistic DAC areal productivities of 100–1000 tCO₂/km²/year would require 1–10 million km² (equivalent to 10–100% of the Sahara Desert) for 1 Gt/year.
  - No lifecycle assessment or net carbon removal calculation is provided—embedded emissions from sorbent manufacturing, solar panel production, and construction could significantly erode the claimed 95% net efficiency.
  - The claim does not distinguish between lab-scale proof-of-concept (mg or g quantities, idealized conditions) and field-pilot performance under real ambient air with humidity, temperature swings, and trace contaminants.

**partial_coverage:**
  - The $50/ton figure appears independently in a commercial announcement by Prometheus Fuels, but their system captures CO₂ into water for immediate electrochemical fuel synthesis, fundamentally different from standalone DAC materials—and notably, their claim lacks peer review and independent replication.
  - Solar-powered DAC is well-studied conceptually (techno-economic assessments exist for both solar-thermal calcination and PV-driven systems), but no published study achieves $50/ton; the lowest modeled costs cluster around $100–250/ton under aggressive assumptions.
  - Sorbent degradation mechanisms (oxidation, urea formation, SOx/NOx poisoning) are well-characterized for amine-based systems, but novel materials (COFs, MOFs, photobases) have far less long-term cycling data, creating an evidence gap the claim could exploit.
  - The Gt/year scalability literature focuses primarily on energy and land constraints, but the materials supply chain (e.g., global amine production capacity, silica precursor availability) is underexplored and could be the binding constraint.

### C5_smartpanel_dumbjudge
_умная панель + глупый судья_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b | cost=$0.2006 | 346.2s | ptok=39739 ctok=9166 | retries=0

**consensus:**
  - The $50/ton cost is 10–20× below current state-of-the-art DAC costs
  - 95% efficiency requires unprecedented sorbent performance and contradicts thermodynamic realities
  - Solar-only energy introduces intermittency and storage challenges
  - Gigaton-scale deployment faces material supply chain, land, and infrastructure barriers
  - All models agree the claim requires simultaneous breakthroughs in multiple domains

**contradictions:**
  - {"topic": "Feasibility of 95% efficiency with low energy", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "Thermodynamically punitive; requires unrealistic air-contactor design"}, {"model": "z-ai/glm-5.1", "stance": "Material breakthroughs could enable switchable affinity mechanisms"}, {"model": "moonshotai/kimi-k2.6", "stance": "Single-pass capture efficiency is fundamentally limited by mass-transfer kinetics"}]}
  - {"topic": "Inclusion of all costs in $50/ton", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "Likely excludes CO₂ transport/storage, water, and capital costs"}, {"model": "z-ai/glm-5.1", "stance": "Costs must include solar infrastructure, storage, and land"}, {"model": "moonshotai/kimi-k2.6", "stance": "Claim likely omits CAPEX, OPEX, and lifecycle emissions"}]}
  - {"topic": "Solar intermittency impact", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "Requires massive overbuilding and storage, inflating costs"}, {"model": "z-ai/glm-5.1", "stance": "Solar-to-CO₂ efficiency must exceed 25% capacity factor"}, {"model": "moonshotai/kimi-k2.6", "stance": "Low utilization makes $50/ton thermodynamically implausible"}]}

**unique_insights:**
  - {"model": "z-ai/glm-5.1", "insight": "The 'thermodynamic minimum' energy (120 kWh/ton) is a red herring; real systems require 3–5× this with no known material approaching it"}
  - {"model": "moonshotai/kimi-k2.6", "insight": "Gigaton-scale DAC would require 1,400–4,200 TWh/year of energy—comparable to U.S. utility-scale generation"}
  - {"model": "deepseek/deepseek-v4-pro", "insight": "Evaporative carbonate crystallization reduces air-handling costs but requires energy-intensive electrochemical regeneration"}

**blind_spots:**
  - Geopolitical risks of raw material supply chains for novel sorbents
  - Climate change feedback loops affecting solar availability and atmospheric CO₂ concentrations
  - Role of public-private partnerships in scaling infrastructure
  - Embodied carbon in manufacturing gigaton-scale DAC systems
  - Impact of DAC on global energy markets and fossil fuel demand

**partial_coverage:**
  - {"models": ["deepseek/deepseek-v4-pro", "z-ai/glm-5.1"], "point": "Water consumption constraints in arid solar-optimal regions"}
  - {"models": ["deepseek/deepseek-v4-pro", "moonshotai/kimi-k2.6"], "point": "Impact of atmospheric contaminants on sorbent degradation"}

### C5inv_dumbpanel_smartjudge
_глупая панель + умный судья (qwen-2.5-7b → gemma-3-12b-it)_  
panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1 | cost=$0.1018 | 209.9s | ptok=17255 ctok=3370 | retries=0

**consensus:**
  - $50/ton is far below current or projected DAC costs (current market avg ~$490/tCO2; even optimistic 2050 projections at Gt-scale are $230-$580/tCO2)
  - Solar-only energy is a critical constraint; intermittency requires storage, supplemental power, or batch operation, undermining continuous gigaton-scale throughput
  - Sorbent/material degradation and limited operational lifetime is a major failure mode (current state-of-art amine sorbents last ~3 months; extending to 1 year would cut costs 60%+ but remains unachieved)
  - Scaling from lab to gigaton/year faces monumental engineering, supply chain, and manufacturing hurdles (millions of modular units, millions of tonnes of sorbent, hundreds of GW of clean power)
  - Regeneration energy is the dominant energy demand in any cyclic DAC process (4-10 GJ/tCO2 for existing approaches vs. 1.8 GJ/tCO2 thermodynamic minimum for capture alone)

**contradictions:**
  - {"topic": "Feasibility of solar-only DAC", "stances": [{"model": "qwen3-8b (Model C)", "stance": "Solar is unlikely to replace fossil energy inputs due to energy density gaps"}, {"model": "evidence", "stance": "Solar-thermal DAC is actively researched and technically viable with design accommodations (batch operation, thermal storage, oversized solar fields), but faces cost and intermittency penalties rather than fundamental impossibility"}]}
  - {"topic": "Interpretation of '95% efficiency' claim", "stances": [{"model": "qwen3-8b", "stance": "Treats 95% as a meaningful, unified efficiency metric requiring breakthroughs"}, {"model": "google/gemma-3-12b", "stance": "Questions what 95% means and how it varies with conditions"}, {"model": "evidence", "stance": "The term is ambiguous in DAC context — could mean capture fraction (fraction of CO2 removed from air, typically 50-90% in literature), product purity (95%+ is standard for pipeline transport), or thermodynamic efficiency. The claim's meaning is undefined, making it unverifiable as stated"}]}

**unique_insights:**
  - {"model": "google/gemma-3-12b (Panel D)", "insight": "Efficiency varies with environmental conditions (temperature, humidity, CO2 concentration, dust, atmospheric pollutants) — lab performance routinely degrades under real-world field conditions, and dust/pollutant fouling is a distinct failure mode from chemical degradation"}
  - {"model": "google/gemma-3-12b (Panel B)", "insight": "Photocatalysis as a specific mechanism enabling solar-only operation (vs. thermal swing) — a fundamentally different energy pathway but one requiring extremely precise reaction control and raising selectivity concerns"}

**blind_spots:**
  - Thermodynamic minimum energy floor: ~120 kWh/ton CO2 (0.43 GJ/t) theoretical minimum; real systems need 3-10x this. At even modest electricity prices ($50-100/MWh), energy cost alone is $18-120/ton before any capital, labor, or materials — making $50/ton mathematically implausible for any cyclic process without assuming near-zero-cost energy
  - Sorbent degradation timeline gap: current state-of-art amine sorbents survive ~3 months; economic viability requires tens of thousands of cycles (years of operation). This gap dominates levelized cost — a recent analysis showed extending replacement from 3 months to 1 year reduces LCOC by 60%+, yet this remains unachieved
  - CO2 sequestration/storage costs excluded from $50/ton claim: compression to 150+ bar, pipeline transport, geological injection, and MRV (monitoring, reporting, verification) add substantial cost and energy — typically $10-30/ton minimum, often more
  - Parasitic energy and capital cost from air movement alone: processing the enormous air volumes needed (CO2 at 420 ppm means ~1,800 tons of air per ton of CO2) requires massive fans and contactor infrastructure with significant capital and operating costs
  - The ambiguity of '95% efficiency' as a claim: in DAC literature this could mean capture fraction, product purity, or thermodynamic second-law efficiency — each with vastly different implications and achievement histories. The claim is ontologically undefined and therefore unfalsifiable as stated
  - Net carbon accounting: at gigaton scale, the carbon embodied in manufacturing sorbents, building infrastructure, and generating power may substantially reduce net removal — lifecycle analyses show GWP of 25-50

**partial_coverage:**
  - {"models": ["google/gemma-3-12b"], "point": "CO2 selectivity and product purity: downstream utilization/storage requires high purity (>95 mol%), adding cost and complexity beyond just capture"}
  - {"models": ["google/gemma-3-12b"], "point": "Water usage and water-solar siting tension: best solar locations are arid, but DAC processes (especially solvent-based) suffer significant water losses in hot dry environments"}
  - {"models": ["google/gemma-3-12b"], "point": "Raw material supply chain for gigaton-scale manufacturing: millions of tonnes of specialist chemicals/minerals required, far beyond current production capacity"}
  - {"models": ["qwen3-8b"], "point": "Lifecycle emissions and net-vs-gross CO2 accounting: energy and materials for building/operating the system have their own carbon footprint that must be subtracted"}
  - {"models": ["qwen3-8b"], "point": "Regulatory, geopolitical, and permitting barriers to global deployment at scale"}

### C6_echo
_контроль: эхо-камера_  
panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507 | cost=$0.0387 | 239.1s | ptok=28839 ctok=2873 | retries=0

**consensus:**
  - Current direct air capture (DAC) technologies are not yet economically viable at scale, with estimated costs ranging from $100–1,000 per ton of CO₂ removed, significantly above the claimed $50/ton.
  - Energy consumption is a major cost driver in DAC, accounting for up to 50% of operational costs, particularly for liquid-based systems.
  - Solar energy integration—especially via concentrating solar power (CSP) or photobases—can reduce carbon intensity and potentially lower costs in optimal locations with high solar irradiance.
  - No current DAC system operates at gigaton scale; existing plants capture less than 0.01 Mt CO₂/year collectively.
  - Achieving low costs requires co-location with low-cost renewable energy, favorable climate conditions, low cost of capital, and access to CO₂ storage.

**contradictions:**
  - Some studies suggest solar-powered DAC could reach $150–200/ton under favorable conditions, while others project long-term costs of $100–600/ton, but none independently support $50/ton as stated.
  - One source suggests solar-powered DAC could be more cost-effective than conventional DAC, while another emphasizes that pairing electricity-driven DAC with intermittent solar without grid support increases net removal cost due to low capacity factor.

**unique_insights:**
  - Photochemically driven DAC using photobases (e.g., PyDIG) enables ambient-temperature CO₂ capture and release using light-induced pH swings, avoiding high-temperature regeneration—but currently demonstrated over only six cycles with limited capacity.
  - Solar thermal energy can provide >1000°C heat necessary for sorbent regeneration in solid DAC systems, but thermal storage for continuous operation remains challenging.
  - Battery storage improves efficiency in solar-electrochemical DAC but increases cost; hydrogen co-production may be more cost-effective for long-duration storage.

**blind_spots:**
  - No source addresses materials durability, degradation, or replacement costs over decades of outdoor solar exposure.
  - There is limited data on water usage and thermal management in arid, high-irradiance regions where solar DAC would be deployed.
  - None of the sources provide verified lifecycle data on net CO₂ removal at gigaton scale, including indirect emissions from manufacturing and construction.

**partial_coverage:**
  - Several analyses cover techno-economic feasibility but lack environmental lifecycle assessments, especially for novel photobase or solid adsorbent materials.
  - Most studies assume favorable conditions (e.g., optimal solar irradiance, low WACC, proximity to storage), but few evaluate systemic constraints like land use, supply chain scalability, or grid interconnection needs.

### C3_cn_small
_всё мелкое_  
panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b | cost=$0.0534 | 399.2s | ptok=17295 ctok=3476 | retries=1

**consensus:**
  - Current DAC systems ($600–$1,000/ton) require significant technological breakthroughs for $50/ton viability.
  - Energy efficiency (900–1,000 kWh/ton CO₂) and material durability are critical challenges.
  - Scale-up to gigatons/year requires radical cost reductions in sorbent materials and contactor infrastructure.
  - The 'fan problem' (air-moving infrastructure costs) remains unresolved in existing DAC designs.

**contradictions:**
  - {"topic": "Feasibility of 'solar-only' thermodynamic efficiency", "stances": [{"model": "z-ai/glm-4.7-flash", "stance": "Photochemical mechanisms could bypass thermal penalties"}, {"model": "qwen/qwen3.6-27b", "stance": "95% thermodynamic efficiency with solar is 'chemically very difficult' in real-world conditions"}]}
  - {"topic": "Primary bottleneck for $50/ton cost", "stances": [{"model": "qwen/qwen3.6-27b", "stance": "Energy and contactor infrastructure must both approach zero marginal cost"}, {"model": "z-ai/glm-4.7-flash", "stance": "Material synthesis cost may dominate over energy costs at scale"}]}

**unique_insights:**
  - {"model": "z-ai/glm-4.7-flash", "insight": "Decentralized manufacturing of sorbent material as a 'utility' could enable gigaton-scale economics through modularity"}
  - {"model": "qwen/qwen3.6-27b", "insight": "Moisture/Climate Paradox: Solar-powered DAC may face inherent tradeoffs between operational efficiency in high-solar vs. high-humidity regions"}

**blind_spots:**
  - Quantification of intermittency penalties for solar-powered DAC (e.g., energy storage requirements for 24/7 operation)
  - Social/geostrategic constraints for material sourcing (e.g., land use for solar farms vs. mining for sorbent precursors)
  - Policy/regulatory feasibility for gigaton-scale CO₂ storage infrastructure linkage
  - Biodiversity impacts of massive air contactor deployment in global ecosystems

**partial_coverage:**
  - {"models": ["z-ai/glm-4.7-flash"], "point": "Dehydration costs for CO₂ purity represent a potential 'energy tax' not explicitly addressed in Qwen analysis"}
  - {"models": ["qwen/qwen3.6-27b"], "point": "Supply chain constraints for novel sorbents (e.g., MOFs) may block gigaton-scale production without precursor revolution"}


---
## BASELINE (одиночная модель, без fusion)

### B_cn  (model=deepseek-v4-pro | cost=$0.0027 | 33.7s)
_(пустой ответ)_

### B_west  (model=gpt-5.2 | cost=$0.0211 | 32.6s)
Below is what would have to be true for the claim to be credible, where such claims most often fail, and the specific due‑diligence questions that would decide whether it’s real or “lab‑optimism.”

---

## 1) What would need to be true for “$50/ton, 95% efficient, solar‑only, gigaton‑scale” to hold

### A. The cost boundary must be full‑system and still ~$50/t
For DAC, $50/t is unusually low unless **all** of the following are included and still pencil out:

- **Air contactor hardware** (fans/blowers if used, ducts, structures), not just sorbent.
- **Sorbent make‑up** (replacement due to degradation) and consumables.
- **Regeneration equipment** (vacuum pumps, heaters, heat exchangers, valves).
- **CO₂ conditioning**: drying (if needed), **compression to pipeline** (often ~80–150 bar), and delivery.
- **Operations & maintenance**, labor, instrumentation, controls.
- **Financing assumptions**: realistic WACC, plant life, capacity factor.
- Ideally also: **CO₂ transport + storage** costs (or clearly stated as excluded). Many “$X/ton” numbers quietly exclude storage, which can be material.

If they’re quoting $50/t for only the sorbent or only the capture step (excluding compression, intermittency, contactor CAPEX), it’s not the number people mean by “DAC cost.”

### B. Energy requirements must be both low and solar-compatible
DAC is energy‑intensive because CO₂ is dilute (~420 ppm). For the claim to work:

- **Total energy per ton** (heat + electricity equivalents) must be very low *in practice*, not just “regeneration enthalpy.”
- The process must handle **solar intermittency** without major efficiency/cost penalties:
  - Either (i) it runs with **thermal storage** / batteries, or  
  - (ii) it can **cycle flexibly** without sorbent or equipment damage and without losing capture fraction.
- The solar system (PV/solar thermal) must be sized such that its **installed cost per delivered kWh** makes $50/t feasible at the assumed capacity factor.

A useful reality check: even **1 GJ/tCO₂** (quite aggressive for full DAC + compression) implies **1 EJ/year** for 1 Gt/year. If real energy is more like a few GJ/t all‑in, you rapidly get into **multi‑EJ/year**, meaning **hundreds of GW average power** and very large solar build‑out and land.

### C. “95% efficiency” must be defined in the way that matters
They must specify which “efficiency” they mean, because it’s often misused:

- **Per-pass capture fraction** (removing 95% of CO₂ from air that passes through) is not the same as…
- **System capture efficiency** (how much CO₂ is removed compared to what could be removed given airflow), and neither is…
- **Net CO₂ removal efficiency** after lifecycle emissions (manufacturing, sorbent replacement, solar build, compression, etc.).

For a credible climate claim, the key is **net removal**: “for every 1 ton captured, ≥0.95 ton is permanently stored” (or similar), with an LCA that backs it up.

### D. The sorbent must have exceptional *working* performance under real air
Lab capacity numbers are meaningless unless these hold under realistic humidity/temperature and cycling:

- High **working capacity** at ~400–450 ppm CO₂ (not at 1–10% CO₂).
- Fast **kinetics** at practical air velocities (otherwise contactor size blows up).
- High **selectivity vs water**, or a process design that handles water without huge energy penalties.
- Low degradation from **oxygen, NOx/SOx, ozone, dust**, and UV exposure (depending on configuration).
- Very long lifetime: typically **thousands to tens of thousands of cycles** with low capacity fade, or sorbent cost dominates.

### E. Gigaton scalability requires supply chains and manufacturing to be plausible
“Scalable to gigatons/year” means:

- Feedstocks are **abundant, low-cost, non-precious**, and not competing with critical uses.
- Sorbent manufacturing can scale to **millions of tons** (possibly more) with manageable embodied emissions.
- Contactor materials (steel, concrete, polymers) and solar build-out are feasible at the implied scale.
- Water use, land use, and siting constraints are addressed (DAC needs a lot of air throughput and usually lots of land and infrastructure).

### F. Permanent storage and MRV must be real, not hand-waved
At gigaton scale, the limiting step is often not capture but **storage**:

- Proven access to **geologic storage capacity**, permitting, pipelines, injection wells.
- **MRV** (measurement
