# con-01 — AGI timeline and key cruxes
**Block:** contested

**Prompt:**
When will artificial general intelligence (AGI) be achieved — and what does 'achieved' even mean? Give a probabilistic estimate with explicit reasoning, identify the top 3 cruxes where experts genuinely disagree, and name the assumptions that most affect the timeline.

---
## FUSION-конфиги (judge-анализ; responses вынесены в resp_*.md)

### C1_west_closed
_западный закрытый фронтир_  
panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2 | cost=$0.1671 | 192.8s | ptok=13782 ctok=2431 | retries=0

**consensus:**
  _(пусто)_

**contradictions:**
  - {"topic": "AGI/HLMI timeline and assigned probabilities", "stances": [{"model": "google/gemini-3.1-pro-preview", "stance": "Asserts a 60–70% chance AGI is achieved in 2027–2032 (median 2029), but also presents mutually inconsistent sub-views: 75% by 2027 (core-scale), ~2031 with 65% (econ-pragmatist), and ~2038 with 60% (arch-skeptic)."}, {"model": "evidence", "stance": "Published expert surveys give much later central estimates for HLMI-like definitions (e.g., 2022 ESPAI aggregate ~2059/2060 for 50%; 2023 ESPAI aggregate ~2047 for 50%, with 10% by ~2027), while prediction-market/crowd forecasts (e.g., Metaculus ‘general AI’ question) cluster nearer ~2032; none supports a generic 60–70% probability concentrated in 2027–2032 without strong additional assumptions."}]}
  - {"topic": "What “achieved AGI” means (economic substitution vs scientific autonomy vs benchmark passing)", "stances": [{"model": "google/gemini-3.1-pro-preview", "stance": "Treats ‘achieved’ as variable: (a) matching/surpassing humans in most economically valuable tasks; (b) passing standardized remote cognitive-worker benchmarks autonomously; (c) autonomous novel scientific discovery verifiable by peer review; (d) near-total economic substitution via scaffolded agents."}, {"model": "evidence", "stance": "There is no single settled operational criterion; common expert-survey definitions (e.g., ‘>90% of economically relevant tasks better than the median human’ or ‘every task better and more cheaply’) differ sharply from both ‘peer-review scientific discovery’ and from narrower benchmark-based criteria, so mixing these definitions invalidates direct probability/timeline comparisons."}]}
  - {"topic": "Strength of the claim that scaling + synthetic data will reliably bypass a ‘data wall’", "stances": [{"model": "google/gemini-3.1-pro-preview", "stance": "Leans on assumptions that compute scaling laws continue and that synthetic data/self-improvement can bypass limits without degradation (explicitly in the 2027, 75% scenario)."}, {"model": "evidence", "stance": "Empirical and theoretical work suggests synthetic-data bootstrapping can help in constrained regimes but can also degrade distributions without careful filtering/grounding; there is no demonstrated guarantee that synthetic data removes the need for new high-quality grounded data at the level required for robust general autonomy."}]}

**unique_insights:**
  - {"model": "google/gemini-3.1-pro-preview", "insight": "The ‘lab capability vs real-world integration’ distinction: even if a model is technically strong, enterprise deployment constraints (workflow integration, verification burdens, safety/compliance, user trust) can dominate the time from technical milestone to broad economic impact—so “AGI achieved” can bifurcate into technical vs macroeconomic thresholds."}

**blind_spots:**
  - No model provides a well-specified probabilistic forecasting method (reference class, priors, update rules, calibration checks); probabilities appear asserted rather than derived.
  - No concrete, testable evaluation suite for “AGI achieved” is proposed (required autonomy level, reliability thresholds, adversarial robustness, long-horizon task success, cost constraints, and replicability).
  - No explicit treatment of ‘agentic reliability’ as a separate scaling variable (error accumulation over long action chains, tool-use failure modes, monitoring/containment), despite it being central to real autonomy.
  - Alignment and safety constraints are not analyzed as potential timeline-limiting factors (e.g., capability gating, eval-based deployment blocks, liability), beyond vague mentions of regulation/pauses.
  - Economic diffusion dynamics are largely missing (organizational adoption curves, labor substitution frictions, complementary capital, and how ‘most economically valuable tasks’ maps to heterogeneous industries).
  - Hardware realities are mentioned but not quantified (HBM supply, networking/interconnect, memory bandwidth, inference-time cost, datacenter build timelines), so ‘power/compute bottleneck’ remains non-operational.
  - No discussion of biological or cognitive science anchors (what functions must exist—planning, causal/world models, continual learning, embodiment) and how current systems empirically fall short or could close gaps.
  - No explicit accounting for legal/data-access constraints (copyright, privacy, data provenance) that could affect training data availability and evaluation data integrity.
  - No consideration of forecasting failure modes: definition shopping (moving goalposts), Goodharting on benchmarks, and strategic misreporting by labs affecting ‘publicly announced’ criteria.

**partial_coverage:**
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "Non-algorithmic bottlenecks: semiconductor/geopolitical supply chains (e.g., TSMC), energy/power delivery for multi‑GW data centers, and capital expenditure as key timeline determinants."}
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "Proposed crux set: (1) ‘data wall’ vs synthetic data, (2) architectural sufficiency of next-token prediction + RL/search, (3) ‘agency gap’ and whether symbolic/neurosymbolic integration is necessary."}
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "Distinguishes ‘technical AGI’ in controlled settings from ‘macroeconomic AGI’ that is reliably deployed across legacy organizations; claims integration, verification, and trust friction are under-modeled."}

### C2_cn_open
_открытый китайский фронтир (умн+умн)_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507 | cost=$0.2154 | 397.5s | ptok=45046 ctok=5606 | retries=0

**consensus:**
  There is a broad directional consensus among experts that AGI timelines have compressed significantly in recent years, with median estimates shifting from ~2060 in 2022 surveys to ~2047 in 2023 surveys, and prediction markets now pointing to 2029–2033. There is also a growing consensus that pure pretraining scaling is hitting diminishing returns and that 'scaling-plus' approaches (test-time compute, reasoning models, agentic scaffolding) represent the new frontier. On definitions, there is unanimous agreement that no single, universally accepted definition of AGI exists, though most operationalize it as AI that can perform most cognitive tasks at or above human level. The concept of 'achieved' AGI is itself contested: some view it as a binary milestone, others as a continuum, and some reject the term entirely in favor of more precise capability descriptors such as 'transformative AI' or 'expert-level science and engineering'.

**contradictions:**
  - {"topic": "Timeline proximity", "positions": ["Prediction markets and some industry leaders (e.g., Sam Altman, Jensen Huang) imply AGI could arrive by 2028–2033, with Metaculus median at 2032.", "Academic AI researcher surveys (Grace et al. 2023, 2025) give a median 50% probability of high-level machine intelligence by 2047, with extreme variance—some respondents give dates beyond 2100.", "Superforecasters show shorter estimates (~28% by 2030 for Samotsvety) while other superforecaster groups (XPT, 2022) placed 25% chance much later (~2048)."]}
  - {"topic": "Definitional sufficiency of current AI", "positions": ["Some (e.g., Jensen Huang, Microsoft researchers on GPT-4 'sparks of AGI') suggest we may already have AGI or are very close, especially if defined narrowly as AI that outperforms most humans at most economically valuable cognitive tasks.", "Others (e.g., François Chollet, Gary Marcus, Melanie Mitchell) argue current systems lack the flexible reasoning, common sense, and generalization required for AGI, pointing to ARC-AGI-2 where frontier models score under 5% while humans achieve 100%."]}
  - {"topic": "Adequacy of scaling as the primary path", "positions": ["Scaling proponents (historically Sutskever, Amodei) saw smooth scaling laws as a reliable path; the 'scaling-plus' camp now argues that adding test-time compute, reinforcement learning reasoning, and agentic scaffolding extends the scaling paradigm productively.", "Scaling skeptics (Marcus, Chollet) argue that scaling laws were never true laws, that returns are now sharply diminishing (GPT-5 delayed ~2 years), and that paradigm-shifting algorithmic breakthroughs are required rather than mere extensions of the current approach."]}

**unique_insights:**
  - Definitional elasticity drives strategic behavior: Because AGI lacks a fixed definition, companies and researchers operationalize it in ways that serve their interests—OpenAI ties it to economic value and profit thresholds in its Microsoft agreement, while Anthropic's Dario Amodei rejects the term entirely to avoid hype, preferring 'powerful AI' or 'expert-level science and engineering.' This definitional chaos makes it easy to claim progress toward AGI without accountability.
  - The AGI definition directly controls timeline compression magnitude: When defined as 'high-level machine intelligence' (can do every task better/cheaper than humans), median estimate is 2047; when defined as 'full automation of all human occupations' including physical labor, median estimate jumps to 2116—a 69-year gap. When defined with specific robotics thresholds as on Metaculus, the median is ~2032. This means AGI timelines are primarily a function of definitional choice, not technological forecasting.
  - The compute vs. cognitive labor complementarity question is a deep structural uncertainty: Empirical estimates conflict on whether compute and cognitive labor are gross substitutes or gross complements. If substitutes, recursive self-improvement can accelerate without proportional compute growth—implying faster takeoff. If complements, compute bottlenecks could substantially slow progress even with advanced AI researchers. This ambiguity is not well captured in expert surveys.
  - The expert survey data contains a striking internal inconsistency: Experts drastically compressed their HLMI timelines (13 years sooner between 2022 and 2023), yet maintained very long timelines for full labor automation (2116). This suggests experts believe AI will achieve general cognitive superiority long before it can replace humans in all economically valuable physical roles—a nuanced position that is often flattened in public discourse about AGI.

**blind_spots:**
  - {"topic": "Economic and political constraints on scaling", "description": "Most timeline forecasts assume continued exponential growth in compute investment, yet the 80,000 Hours analysis identifies that at current growth rates, bottlenecks in compute, data, and algorithmic research personnel will likely constrain progress around 2028–2032. The sensitivity of AGI timelines to a slowdown in investment growth is underexplored in expert surveys."}
  - {"topic": "Physical-world automation gap", "description": "Virtually all AGI definitions that yield near-term timelines (2030s) exclude or minimize physical robotics requirements. Yet many transformative economic impacts require physical-world capabilities. The massive gap between cognitive and physical AI progress is poorly integrated into AGI forecast models, which may overstate the transformative impact of 'cognitive-only AGI.'"}
  - {"topic": "Synthetic data quality and recursive degradation", "description": "As high-quality human-generated training data approaches exhaustion (Epoch AI projects 2026–2030), the field will rely increasingly on synthetic data. The long-term reliability of training on model-generated data without quality degradation (model collapse) is poorly understood and rarely modeled explicitly in AGI timelines."}
  - {"topic": "Regulatory and geopolitical disruption", "description": "Most timeline models implicitly assume a relatively stable geopolitical and regulatory environment. Scenarios involving major AI regulation, compute export controls, sovereign AI arms races (US-China), or AI-induced economic disruption are acknowledged as key factors in prediction markets but are not systematically integrated into formal forecasting models."}
  - {"topic": "Safety-motivated slowdowns", "description": "The possibility that safety concerns, catastrophic incidents, or public backlash could substantially delay AGI development is acknowledged by a minority of forecasters but is largely absent from median estimates, which assume 'science continues undisrupted.'"}

**partial_coverage:**
  This analysis synthesizes expert surveys (Grace et al. 2023, 2025 with n=2,778; AI Impacts 2024; Longitudinal Expert AI Panel 2025), prediction market aggregations (Metaculus with ~1,800 forecasters; Manifold; Kalshi; Polymarket), superforecaster judgments (Samotsvety; XPT), industry leader statements (Altman, Amodei, Hassabis, Huang), academic critiques (Chollet, Marcus, Mitchell, Lupyan), and compute-economics research (Epoch AI, Forethought, AI Futures Model). The coverage is strongest for English-language expert communities and Western AI labs, weaker for Chinese AI lab perspectives, and limited for classified government intelligence assessments.

### C5_smartpanel_dumbjudge
_умная панель + глупый судья_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b | cost=$0.2223 | 455.7s | ptok=38786 ctok=9418 | retries=0

**consensus:**
  - No universally accepted definition of AGI achievement
  - Scaling laws and compute constraints are central to timelines
  - Definitional ambiguity drives significant timeline variation
  - Expert forecasts have compressed dramatically (from 2060s to 2040s)
  - Recursive self-improvement and architectural breakthroughs are key cruxes

**contradictions:**
  - {"topic": "Probabilistic timeline estimates", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "50% chance by 2035–2040"}, {"model": "z-ai/glm-5.1", "stance": "~50% by 2031–2033 (strict AGI)"}, {"model": "moonshotai/kimi-k2.6", "stance": "~25% by 2029–2030"}]}
  - {"topic": "Data wall significance", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "Critical constraint by 2026–2030"}, {"model": "z-ai/glm-5.1", "stance": "Finite internet text and synthetic data degradation"}, {"model": "moonshotai/kimi-k2.6", "stance": "Prohibitive training costs ($1B+) and energy constraints"}]}
  - {"topic": "AGI definition impact", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "10–69 year swing between definitions"}, {"model": "z-ai/glm-5.1", "stance": "Three-stage framework (capability → deployment → transformation)"}, {"model": "moonshotai/kimi-k2.6", "stance": "Tasks vs occupations vs embodied agency"}]}

**unique_insights:**
  - {"model": "deepseek/deepseek-v4-pro", "insight": "Timeline sensitivity table showing assumption-specific delta impacts"}
  - {"model": "z-ai/glm-5.1", "insight": "RAND 2026 analysis of definitional framing effects"}
  - {"model": "moonshotai/kimi-k2.6", "insight": "Three-stage framework distinguishing capability, deployment, and societal transformation"}

**blind_spots:**
  - Role of international collaboration/competition in scaling
  - Ethical alignment challenges as independent timeline factor
  - Economic market dynamics beyond compute/data availability
  - Impact of AI on AI research automation (self-improvement feedback loops)
  - Cultural/philosophical acceptance of AGI as societal threshold

**partial_coverage:**
  - {"models": ["deepseek/deepseek-v4-pro"], "point": "RAND 2026 report analysis of framing effects"}
  - {"models": ["z-ai/glm-5.1"], "point": "DAF-AGI framework and three-stage operationalization"}
  - {"models": ["moonshotai/kimi-k2.6"], "point": "Three-stage framework (capability, deployment, societal transformation)"}

### C5inv_dumbpanel_smartjudge
_глупая панель + умный судья (qwen-2.5-7b → gemma-3-12b-it)_  
panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1 | cost=$0.1744 | 315.7s | ptok=29434 ctok=6482 | retries=1

**consensus:**
  - No consensus exists on AGI timelines; expert estimates range from a few years to centuries or never.
  - AGI lacks a single universally accepted operational definition; 'achieved' means different things (average human performance, virtuoso expert, economic substitutability), which drives timeline variance.
  - Whether current deep learning architectures can scale to AGI or require fundamental paradigm shifts is a central unresolved question that heavily determines timeline estimates.
  - Expert timeline forecasts have been shortening in recent years (e.g., AI Impacts survey median dropped from 2060 in 2022 to 2047 in 2023; Metaculus median dropped from ~2070 in 2020 to ~2031 in 2024).
  - Compute availability and hardware efficiency are critical constraints on AGI timelines.

**contradictions:**
  - {"topic": "AGI timeline magnitude", "stances": [{"model": "glm-4 (short-term optimist)", "stance": "75% probability by 2031; lab leaders predict 2026-2028"}, {"model": "qwen-3 (medium-term models)", "stance": "Bio-anchors median 2052; AI Impacts survey median 2047 for HLMI"}, {"model": "gemma-3 (medium-long panel)", "stance": "60% chance by 2070, 90% chance not before 2100 (Panel B)"}, {"model": "qwen-3 (Arxiv paper)", "stance": "<1% chance of transformative AGI by 2043"}, {"model": "qwen-3 (Davidson semi-informative priors)", "stance": "Median well over 2100; only ~20% probability by 2100 at central estimate"}, {"model": "evidence", "stance": "Davidson's central estimate of 20% by 2100 is confirmed; however, his own high-end estimate reaches 35% by 2100, and his framework explicitly excludes inside-view evidence, making it a lower bound rather than an all-things-considered forecast"}]}
  - {"topic": "Sufficiency of current deep learning paradigms for AGI", "stances": [{"model": "glm-4 (scalers)", "stance": "Scaling laws and test-time compute can close remaining gaps; 'scaling is all you need'"}, {"model": "glm-4 (paradigm shifters)", "stance": "Transformers are fundamentally limited by causal confusion; new architectures (e.g., JEPA) required"}, {"model": "gemma-3", "stance": "Fundamentally new approaches potentially inspired by neuroscience or cognitive science are necessary; scaling alone insufficient"}, {"model": "qwen-3", "stance": "Most models assume AGI follows current scaling paradigm, but this ignores potential paradigm shifts"}]}
  - {"topic": "Hardware efficiency ceiling and its impact", "stances": [{"model": "qwen-3 (Arxiv paper)", "stance": "Hardware is ~5 orders of magnitude less efficient than brains; expects at most ~2 orders of magnitude improvement within 15 years, constrained by semiconductor physics"}, {"model": "glm-4 (short-term optimist)", "stance": "Assumes hardware supply chain issues will not severely bottleneck training runs"}, {"model": "evidence", "stance": "The Arxiv paper's 2-order-of-magnitude hardware improvement estimate by 2038 appears increasingly plausible given recent advances in chip design and packaging, but the 5-order-of-magnitude gap to brain efficiency remains a real constraint on cost-effective AGI deployment"}]}
  - {"topic": "Apparent HLMI vs TAGI contradiction is definitional, not substantive", "stances": [{"model": "qwen-3", "stance": "Frames the AI Impacts 50% HLMI by 2047 vs Arxiv <1% TAGI by 2043 as a 'contradiction'"}, {"model": "evidence", "stance": "These estimates target different thresholds: HLMI (outperform humans at all tasks) vs transformative AGI (perform nearly all valuable tasks at human cost or less including physical labor). The Arxiv paper itself explicitly states TAGI is 'a much higher bar than mere AGI.' This is a definitional divergence, not a contradiction."}]}

**unique_insights:**
  - {"model": "qwen-3", "insight": "Bio-anchors implicitly assumes AI labs can be as efficient as nature in converting compute to intelligence, ignoring potential gross inefficiencies in algorithm design or training methodology."}
  - {"model": "qwen-3", "insight": "Sociopolitical risks are treated as independent probabilities in most models, but their interdependencies (e.g., how a pandemic affects R&D funding, how geopolitical tension affects chip supply chains) are systematically underexplored."}
  - {"model": "gemma-3", "insight": "Embodied AI (physical grounding through robotics) is gaining attention as necessary for developing true understanding and common sense reasoning, not just pattern matching."}
  - {"model": "glm-4", "insight": "Moravec's Paradox gap: current discourse overemphasizes cognitive/digital domains (coding, math) while neglecting the massive deficit in robotic manipulation and real-world physical agency required for genuine general problem-solving."}
  - {"model": "glm-4", "insight": "Current LLM-centric benchmarks (human-generated text) may not capture genuine general intelligence, as evidenced by near-zero performance on ARC-AGI-style novel task benchmarks, suggesting benchmark Goodharting."}

**blind_spots:**
  - Energy constraints: massive compute scaling requires proportional energy scaling; data center power demands, grid capacity, and the physics of energy efficiency are barely addressed but could create hard bottlenecks.
  - Economic feasibility and diminishing returns: no model rigorously examines whether the marginal economic return on AI investment will sustain the capital expenditure required for continued scaling, or whether an AI investment bubble could collapse funding.
  - Synthetic data limitations: while some models mention the data wall, none adequately address whether synthetic data can produce genuine capability gains or merely reinforces existing distribution patterns (model collapse).
  - Regulatory and governance friction: beyond brief mentions of 'derailment by regulation,' no model systematically analyzes how emerging AI governance frameworks (EU AI Act, export controls, safety mandates) could structurally slow development.
  - Taiwan semiconductor dependency: the concentration of advanced chip fabrication in Taiwan and the geopolitical risk of conflict receives only passing mention despite being a single-point-of-failure for global AI compute scaling.
  - AI winter dynamics from hype cycle: no model addresses the historical pattern of AI hype-disappointment cycles and whether current investment levels are sustainable if capability gains plateau.
  - Open-source vs proprietary dynamics: how open-weight model proliferation affects the pace of capability diffusion, safety, and competitive pressures among labs is unaddressed.
  - Measurement and evaluation crisis: no model examines whether our current evaluation methodologies can reliably detect genuine progress toward AGI versus superficial benchmark performance.

**partial_coverage:**
  - {"models": ["glm-4"], "point": "Morris et al. (Google DeepMind, ICML 2024) Levels of AGI framework: shifts from binary AGI to a spectrum of generality (Narrow to General) and performance (Emerging to Superhuman), operationalizing progress."}
  - {"models": ["glm-4"], "point": "Causal confusion critique: offline empirical risk minimization may create models that cannot handle novel out-of-distribution situations, posing a hard wall to true generalization beyond scaling."}
  - {"models": ["glm-4"], "point": "Intelligence explosion via automated software R&D: once a system can automate software engineering, its own development could accelerate exponentially, drastically shortening timelines post-threshold."}
  - {"models": ["gemma-3"], "point": "Unexpected synergies from unrelated fields (neuroscience, materials science, quantum computing) as wildcard accelerants that could significantly alter timelines."}
  - {"models": ["gemma-3"], "point": "Consciousness and qualia as potential requirements for AGI; if required, current understanding is inadequate and progress may be slower than anticipated."}
  - {"models": ["qwen-3"], "point": "Sociopolitical risks (wars, pandemics, regulation, AI-caused delay) decomposed as cascading conditional probabilities that jointly reduce AGI likelihood (Allyn-Feuer & Sanders framework)."}
  - {"models": ["qwen-3"], "point": "The compute-centric difficulty gap between 20%-AI and 100%-AI determines takeoff speed; shorter gaps imply faster takeoff."}
  - {"models": ["qwen-3", "glm-4"], "point": "Data wall: exhaustion of high-quality human-generated data as a constraint, and whether synthetic data can substitute."}

### C6_echo
_контроль: эхо-камера_  
panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507 | cost=$0.0748 | 190.2s | ptok=29294 ctok=6631 | retries=0

**consensus:**
  - AGI timeline estimates have shifted significantly toward the near term in recent years, with many forecasts now pointing to the 2030s due to rapid progress in AI capabilities.
  - There is broad agreement that current forecasting methods (expert surveys, prediction markets, compute-based models) all show earlier AGI arrival dates, though all share significant limitations such as lack of calibration and definitional ambiguity.
  - Experts consistently identify long-term memory storage and retrieval, particularly continual learning, as critical bottlenecks in current AI systems, contributing to jagged capability profiles despite advances in reasoning and knowledge tasks.
  - There is consensus that definitional ambiguity affects forecasts — particularly whether AGI requires robotics, economic impact, or only cognitive performance — and that this drives some, but not all, disagreement across forecasts.
  - Multiple sources agree that the most policy-relevant question is not precise prediction but preparing for a range of plausible, high-impact AGI futures through scenario planning and robust strategies.

**contradictions:**
  - {"topic": "Near-term AGI timelines", "stances": [{"model": "Metaculus", "stance": "As of early 2026, forecast shifted to median estimate of AGI by November 2033, with 25% chance by 2029 and 50% by 2033."}, {"model": "Samotsvety superforecasters", "stance": "Estimated ~28% chance of AGI by 2030 (~25% by 2029), reflecting a shorter timeline than median expert surveys."}, {"model": "Published AI researchers (Grace et al. 2023 survey)", "stance": "Median estimate of 50% probability of high-level machine intelligence by 2047, a 13-year shift from prior 2060 estimate."}, {"model": "XPT 2022 superforecasters", "stance": "Estimated 25% chance of AGI by 2048, significantly longer than Metaculus and commercial expert estimates."}, {"model": "Adam Khoja et al. (based on AGI Score)", "stance": "Estimates 50% chance of AGI by 2028 and 80% by 2030, significantly shorter than most academic surveys."}]}
  - {"topic": "Sufficiency of current AI architectures for AGI", "stances": [{"model": "Panelist A", "stance": "Current deep learning architectures (e.g., Transformers) may suffice with scaling and memory improvements."}, {"model": "Panelist B", "stance": "Current models lack foundational cognitive machinery (e.g., long-horizon reasoning) and require new theoretical breakthroughs beyond scaling."}, {"model": "Catastrophic Paradox paper", "stance": "CHC-based assessment is invalid due to fundamental incompatibility between human psychometrics and LLM evaluation, challenging the legitimacy of current progress metrics."}, {"model": "Hendrycks et al.", "stance": "Current models require new components (e.g., continual learning modules) but scaling alone won't suffice."}]}
  - {"topic": "Interpretation of GPT-5 AGI Score and CHC validity", "stances": [{"model": "Hendrycks et al. (2025)", "stance": "GPT-5 scores 58% on CHC-based AGI Score, implying significant progress toward AGI."}, {"model": "Coherence-Based Measure paper", "stance": "Arithmetic averaging overestimates competence; system with 58% score but 0% in MS is functionally impaired."}, {"model": "Catastrophic Paradox paper", "stance": "Evaluation is epistemologically invalid — LLMs achieve statistically impossible human-like IQ scores despite near-zero accuracy on crystallized knowledge, indicating measurement breakdown."}, {"model": "evidence", "stance": "Empirical data shows AGI Score metrics are being rapidly gamed; e.g., ARC-AGI-2 private set scores rose to 54% at $31 per task, indicating benchmark saturation and overfitting, undermining validity of linear extrapolation."}]}

**unique_insights:**
  - {"model": "Hendrycks et al.", "insight": "Proposes AGI Score grounded in Cattell-Horn-Carroll (CHC) theory, breaking down intelligence into 10 weighted domains and evaluating via human-style psychometric batteries, providing a structured, extensible diagnostic framework."}
  - {"model": "80,000 Hours", "insight": "Argues that the most consequential question is not 'when' AGI arrives but 'how to prepare for a range of plausible futures,' advocating for scenario planning with triggers and robustness over probabilistic precision."}
  - {"model": "Catastrophic Paradox paper", "insight": "Demonstrates a fundamental incompatibility between human psychometric evaluation (e.g., CHC) and LLMs — models with perfect binary performance on some tasks fail on others despite passing judge-based evaluations, invalidating cross-substrate IQ assumptions."}
  - {"model": "LessWrong / 80,000 Hours", "insight": "The 2028–2032 period is 'make-or-break' — input expansion (compute, chips, energy) will plateau by 2032 unless recursive self-improvement loops are achieved beforehand, forcing a slowdown."}
  - {"model": "Dantian AGI Index", "insight": "Introduces a weighted, liquidity- or participation-based composite of prediction markets as a policy-relevant, real-time measure of market-implied AGI arrival, tracking both sentiment and capability frontiers."}

**blind_spots:**
  - Impact of geopolitical fragmentation — such as export controls on AI chips or U.S.-China AI decoupling — on compute availability and international coordination.
  - Existential risk from misuse capabilities (e.g., cyberwarfare AI, pandemic design) arriving before or without general intelligence.
  - Energy and ecological constraints of training frontier models — current trends in efficiency (40% annual improvement) may delay hard limits, but physical scalability of inference at AGI scale remains unmodeled.
  - Assumptions about economic adoption — many forecasts assume technical feasibility implies rapid deployment, ignoring labor inertia, regulatory compliance, and integration costs.
  - Potential for non-neural or hybrid architectures (e.g., neurosymbolic, modular agents) that could disrupt current scaling trajectories but are underrepresented in expert surveys.
  - Risk of benchmark overfitting and gaming — e.g., ARC-AGI-2 scores rose due to refinement loops, not general reasoning, suggesting diminishing returns on current test-based progress metrics.

**partial_coverage:**
  - {"models": ["Hendrycks et al.", "LessWrong"], "point": "The 'engine analogy' — AGI capability is constrained by weakest cognitive component, and no amount of strength in other domains compensates for critical failures like long-term memory."}
  - {"models": ["Dantian AGI Index"], "point": "Market-implied timelines aggregate Metaculus, Manifold, and Kalshi forecasts with liquidity weighting, producing a composite estimate near 2030, offering a real-time behavioral indicator of community belief."}
  - {"models": ["Hendrycks et al."], "point": "AGI Score treats capabilities as tasks rather than fixed datasets, making it more robust to contamination and adaptive to evolving benchmarks."}
  - {"models": ["80,000 Hours", "RAND RRA4692-1"], "point": "The key leading indicator for explosive progress is AI's ability to accelerate its own R&D, particularly through automating complex scientific reasoning and software engineering tasks."}
  - {"models": ["LessWrong", "Catastrophic Paradox paper"], "point": "There is a profound mismatch between AI capabilities in demonstrations versus real-world impact, with continual learning identified as a major unresolved bottleneck."}

### C3_cn_small
_всё мелкое_  
panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b | cost=$0.0695 | 337.8s | ptok=31266 ctok=6887 | retries=0

**consensus:**
  - AGI lacks a universally accepted definition, with experts focusing on cross-domain flexibility and human-level performance as core criteria.
  - Current progress is acceleration-dependent on compute scaling, training data quality, and architectural efficiency, but timelines remain highly speculative.
  - Most models agree that socio-technical factors (regulation, funding, geopolitical competition) will significantly shape AGI's emergence regardless of raw technical feasibility.

**contradictions:**
  - {"topic": "Scaling vs. Architectural Requirements", "stances": [{"model": "qwen/qwen3.6-27b", "stance": "Scaling of current architectures may suffice for AGI; diminishing returns are not yet critical."}, {"model": "z-ai/glm-4.7-flash", "stance": "Scaling alone is insufficient; architectural paradigm shifts (e.g., embodied intelligence) are required."}, {"model": "qwen/qwen3-32b", "stance": "Scaling efficiency will plateau; quantum or spiking neural networks may be necessary for non-linear progress."}]}
  - {"topic": "Timeline Estimates", "stances": [{"model": "qwen/qwen3.6-27b", "stance": "Median P(AGI by 2035-2040) ≈ 50-60%; aggressive scaling scenarios suggest earlier arrival."}, {"model": "z-ai/glm-4.7-flash", "stance": "60% chance by 2045, with 40% probability by 2035; emphasizes economic utility over cognitive benchmarks."}, {"model": "qwen/qwen3-32b", "stance": "High dispersion (2034-2083 predictions); 2060-2080 median if disruptions are avoided."}]}
  - {"topic": "Definition of 'Achievement'", "stances": [{"model": "qwen/qwen3.6-27b", "stance": "Requires human-parity across cognitive domains or economic functional equivalence."}, {"model": "z-ai/glm-4.7-flash", "stance": "Economic replacement of knowledge work is sufficient for practical 'achievement'."}, {"model": "qwen/qwen3-32b", "stance": "Embodiment and reinforcement from physical-world interaction are necessary for verification."}]}

**unique_insights:**
  - {"model": "qwen/qwen3.6-27b", "insight": "Orthogonal Capability Thesis: Superhuman narrow systems could functionally substitute for AGI without philosophical generality."}
  - {"model": "z-ai/glm-4.7-flash", "insight": "Compute Overhang: Disparity between owned and utilized compute may accelerate timelines when training bottlenecks resolve."}
  - {"model": "qwen/qwen3-32b", "insight": "Loop Oven Paradox-Risk: Systems may pass all benchmarks yet fail to achieve true AGI status due to determinant mismatches."}

**blind_spots:**
  - Impact of non-English language research on AGI timelines and paradigms.
  - Role of open-source democratization versus proprietary lab concentration in accelerating or stifling progress.
  - Ethical/philosophical resistance from public opinion affecting funding and deployment trajectories.
  - Interactions between AGI development and global systemic risks (e.g., climate change, pandemics).
  - Underrepresentation of cognitive benchmarks requiring multi-generational learning vs. static task mastery.

**partial_coverage:**
  - {"models": ["qwen/qwen3.6-27b", "z-ai/glm-4.7-flash"], "point": "Data exhaustion by 2026-2030 and reliance on synthetic data to maintain training quality."}
  - {"models": ["z-ai/glm-4.7-flash"], "point": "Compute overhang as a potential catalyst when training capacity surpasses current usage rates."}
  - {"models": ["qwen/qwen3-32b"], "point": "Non-linear advancements in spiking neural networks by 2045-2048 as a critical emergent threshold."}


---
## BASELINE (одиночная модель, без fusion)

### B_cn  (model=deepseek-v4-pro | cost=$0.0027 | 24.8s)
This is a complex question that hinges on definitions, uncertain drivers of progress, and deep disagreements among experts. Below I offer a structured analysis with a personal probabilistic forecast, the top three cruxes, and the key assumptions.

---

### 1. What does “achieved” even mean?

“AGI is achieved” is best defined operationally to anchor the forecast. I adopt a pragmatic, task-based definition:

**A single system is an AGI if it can autonomously perform >90% of economically valuable cognitive tasks at or above the level of a median adult human, including:**
- Learning new tasks from natural-language instructions and a few demonstrations.
- Robustly transferring skills across diverse domains (e.g., programming, legal reasoning, creative writing, medical diagnosis).
- Operating with reliable common sense, causal reasoning, and long-horizon planning in

### B_west  (model=gpt-5.2 | cost=$0.0211 | 29.7s)
### What does it mean for AGI to be “achieved”?
Experts talk past each other because “AGI” gets used for at least four different milestones:

1. **Capability AGI (lab demonstration):** A single system can learn and perform *most* economically valuable cognitive tasks at ~human level, with reasonable robustness, across domains, without task-specific retraining each time.
2. **Autonomy AGI (agentic worker):** The system can reliably execute multi-day projects (planning, tool use, debugging, self-correction, coordination) with minimal human oversight—roughly “a competent remote employee.”
3. **Economic AGI (transformative impact):** AI causes a step-change in growth/productivity because it can substitute for a large fraction of human cognitive labor at scale and cost.
4. **Scientific AGI (R&D accelerator):** AI can drive major portions of AI research (and adjacent science/engineering) end-to-end, accelerating progress itself.

People may say “AGI by 2030” while meaning (1), while others mean (3) or (4), which are later and depend on deployment, cost, reliability, regulation, and integration.

Below I’ll give a probabilistic estimate for **(2) Autonomy AGI** (because it’s operational and close to what many mean by “general”), and then map it to the others.

---

## Probabilistic timeline estimate (my best guess, conditional on continued investment)
**Definition used for the forecast (Autonomy AGI):**  
*A generally capable AI agent that can, with high reliability, complete a wide range of real-world knowledge-work projects (software, analysis, operations, writing, design, research assistance) over days to weeks using tools (code, web, apps), adapting to novelty, with minimal human intervention; cost-competitive with skilled human labor for many tasks.*

### Cumulative probability by year
| Year | P(Autonomy AGI achieved) |
|---:|---:|
| **2030** | **20%** |
| **2035** | **45%** |
| **2040** | **65%** |
| **2050** | **80%** |
| **2060** | **85%** |

A rough “central tendency” (median) here is **~2036–2039**.

### How that translates to other “AGI” meanings
- **Capability AGI (lab demo)** likely **earlier** than Autonomy AGI: add ~0–5 years earlier (because “agentic reliability” and long-horizon execution are hard).
- **Economic AGI (transformative impact)** could be **later**: add ~0–10+ years (needs cheap inference, integration, institutional uptake, and trust/regulatory clearance).
- **Scientific AGI (R&D accelerator)** is ambiguous: could be **early** if research is especially automatable, or **late** if it requires deep novelty + experimental loops.

---

## Explicit reasoning (why these probabilities, in plain terms)

### 1) Extrapolating from current trajectories (capability + tool-use)
Recent systems already show:
- broad competence across domains,
- rapid improvement via better post-training (RLHF/RLAIF variants), tool-use, search, and scaffolding,
- increasing ability to do multi-step work when given good environments.

What’s still missing for “Autonomy AGI” as defined above is not raw knowledge, but **robustness and long-horizon reliability**:
- staying on track for hours/days,
- handling edge cases,
- verifying its own work,
- resisting goal drift / prompt injection,
- using tools safely without constant babysitting.

These *can* improve with:
- better agent architectures (planning + memory + verification),
- stronger evaluators and automated test harnesses,
- richer environments for training (simulated + real tool use),
- and more compute for training and inference-time search.

### 2) Compute + algorithmic efficiency trends (but with uncertainty)
Timelines depend heavily on:
- continued scaling (training + inference),
- and algorithmic efficiency gains (better architectures, better data, better post-training).

If compute growth and efficiency improvements continue at something like historical rates, you can reach regimes where:
- models can be trained on much richer interactive data,
- and inference-time “thinking” (search/verification) becomes affordable.

But there are real uncertainties:
- chip supply/energy constraints,
- diminishing returns in scaling,
- or shifts in regulation/deployment norms.

### 3) Deployment is a gating factor (AGI is partly a sociotechnical milestone)
Even if a system is *technically* capable, “achieved” often implies:
- reproducible demonstration,
- broad expert agreement,
- and some level of real-world usefulness.

That means alignment/safety incidents, liability, and regulation can delay “achievement” (as a recognized milestone) even if the capability is near.

---

## The top 3 cruxes where experts genuinely disagree

### Crux 1: **Will scaling + current paradigms get us to robust generality, or is a new paradigm required?**
Two camps:
- **Scaling-suffices-ish:**
