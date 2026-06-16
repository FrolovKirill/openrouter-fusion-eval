# con-03 — Open-source AI frontier models
**Block:** contested

**Prompt:**
Should powerful AI models (GPT-4 class and above) be released as open weights? Argue both sides seriously — strongest case for open release and strongest case for restricting it. Where does the empirical evidence actually point, and what would change your mind?

---
## FUSION-конфиги (judge-анализ; responses вынесены в resp_*.md)

### C1_west_closed
_западный закрытый фронтир_  
panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2 | cost=$0.3470 | 263.7s | ptok=23081 ctok=4974 | retries=0

**consensus:**
  - Open-weight release is effectively irreversible: once weights are broadly downloadable, downstream use cannot be reliably revoked, patched, rate-limited, or centrally monitored (verified as a basic distribution/replication property of digital artifacts).
  - Both strategies have real tradeoffs: open weights plausibly increase accessibility/innovation/transparency, while restricting weights plausibly reduces some misuse risk by keeping deployment under centralized control (epistemically justified; neither side is a free lunch).
  - The empirical picture is mixed and strongly depends on the specific misuse vector/modality; sweeping claims like “open is always safe/unsafe” are not supported by the current evidence base.
  - A tiered or hybrid approach (e.g., staged/gated release or capability-triggered release) is more defensible than a binary always-open vs always-closed policy, given heterogeneous risks and benefits.

**contradictions:**
  - {"topic": "How decisive current empirical evidence is about open-weight incremental risk", "stances": [{"model": "openai/gpt-5.2", "stance": "Evidence is strong for some mechanisms (e.g., rapid removal of safety fine-tuning when weights are available; and measurable NCII/deepfake ecosystem growth in open image-model communities), but weaker for attributing population-level catastrophic harms from open-weight LLMs (many results are capability demonstrations rather than incident-rate attribution)."}, {"model": "google/gemini-3.1-pro-preview", "stance": "Overall evidence is 'mixed' without distinguishing where it is strong vs weak; emphasizes general value on both sides and uncertainty about capability thresholds."}, {"model": "evidence", "stance": "There is concrete, peer-reviewed evidence that open, fine-tunable generative image ecosystems correlate with large-scale NCII/deepfake proliferation (e.g., FAccT 2025 'Deepfakes on Demand' reports ~35k deepfake model variants and ~15M downloads) and strong evidence that safety tuning is cheaply reversible with weight access (e.g., BadLlama arXiv:2311.00117; Badllama 3 arXiv:2407.01376). At the same time, robust causal estimates tying open-weight frontier LLM releases to real-world catastrophic incident rates remain limited."}]}

**unique_insights:**
  - {"model": "openai/gpt-5.2", "insight": "Modality-specific governance: current empirical harm linkage is much stronger for open image/video generation enabling NCII/deepfake ecosystems than for text-only LLM catastrophic harm attribution, suggesting release policy should differ by modality rather than treating 'open weights' as a single uniform risk category."}
  - {"model": "openai/gpt-5.2", "insight": "A key empirical asymmetry is not just that de-guardrailing is possible, but that the cost/time to remove safety fine-tuning has rapidly collapsed (e.g., from hours/days to minutes) and can be distributed as small adapters—making post-release 'we shipped aligned weights' an especially brittle safety argument for open releases."}

**blind_spots:**
  - Operational decision criteria: none of the models specify measurable capability thresholds, eval suites, or quantitative risk/benefit triggers that would deterministically decide open vs restricted release for 'GPT-4 class and above.'
  - Governance and enforcement mechanisms beyond 'API monitoring': e.g., licensing enforceability in practice, liability regimes for downstream deployers, and how these interact with open weights.
  - Security of weights in the closed scenario: model theft, insider risk, and leakage pathways, and how those probabilities compare to intentional open release in expected-value terms.
  - Geopolitics/export controls: how open releases affect strategic stability, asymmetric access between states, and whether restrictions simply shift capability acquisition to jurisdictions or actors outside the restricting regime.
  - Empirical effectiveness of centralized monitoring/rate limits: little to no quantified evidence here on how often API-based controls actually prevent severe misuse (vs displacing it), and under what attacker models.
  - Externalities and market structure: rigorous causal evidence on competition/innovation benefits (and harms from concentration) specific to open-weight frontier models is largely absent from the panel’s analysis.
  - Non-malicious failure modes unique to open ecosystems: safety regression through benign fine-tuning, supply-chain risks (poisoned checkpoints/adapters), and downstream evaluation gaps before deployment.
  - Defense-in-depth technical mitigations for open weights: e.g., whether any tamper-resistant alignment methods, watermarking/provenance, secure enclaves, or attestations can meaningfully reduce misuse at scale once weights are public.

**partial_coverage:**
  - {"models": ["openai/gpt-5.2"], "point": "Empirical support that safety fine-tuning/guardrails are cheaply undone given weight access (e.g., BadLlama: <$200; Badllama 3: minutes on a single GPU; small 'adapter' distribution), implying 'aligned weights' are not a durable mitigation against malicious fine-tuning."}
  - {"models": ["openai/gpt-5.2"], "point": "Concrete downstream-harm evidence is currently clearest in open image-model ecosystems (NCII/deepfakes), including large-scale model-variant availability and downloads (e.g., FAccT 2025 'Deepfakes on Demand')."}
  - {"models": ["openai/gpt-5.2"], "point": "Biosecurity-style demonstration evidence that an 'uncensored' or fine-tuned open model can provide much more harmful assistance than the base safeguarded model under explicit malicious prompting (e.g., arXiv:2310.18233 pandemic-agent hackathon framing), with the caveat that feasibility within short time windows and real-world translation are not directly measured."}
  - {"models": ["openai/gpt-5.2"], "point": "Benchmark-trend evidence that open-weight models have historically lagged closed frontier models by roughly ~1 year (Epoch AI report), which can be interpreted either as a risk window (time to assess) or as evidence restriction mostly delays diffusion."}
  - {"models": ["openai/gpt-5.2"], "point": "Uses Stanford/CRFM's 'marginal risk' framing: the key question is incremental risk versus closed/API access and versus pre-existing tools (e.g., web search), and current research is insufficient to quantify marginal risk across many misuse vectors."}
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "Explicitly highlights uncertainty about the capability threshold at which open models become 'unmanageable' societal threats, without proposing concrete operational thresholds or evaluations."}
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "Notes (at a high level) that closed systems tend to dominate safety benchmarks while open systems see rapid community-driven gains, but does not connect this to concrete governance levers or measured incident outcomes."}

### C2_cn_open
_открытый китайский фронтир (умн+умн)_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507 | cost=$0.2156 | 471.5s | ptok=23636 ctok=5243 | retries=0

**consensus:**
  - Fine-tuning can remove safety guardrails in both open and closed models, including via API access.
  - Current GPT-4-class models, even after malicious fine-tuning, do not exceed 'Preparedness High' capability thresholds for catastrophic risk in biosecurity or cybersecurity.
  - Open-weight models lag behind closed models by approximately one year, though this gap is shrinking.

**contradictions:**
  - {"topic": "Effectiveness of API monitoring as a safety control", "stances": [{"model": "Advocate_Open", "stance": "API monitoring is weak because fine-tuning via APIs can strip safety guardrails just as effectively as open weights, rendering monitoring largely illusory."}, {"model": "Advocate_Restrict", "stance": "API monitoring, rate-limiting, and revocation provide essential, unique safety controls that open weights completely lack."}, {"model": "evidence", "stance": "Recent work shows covert malicious fine-tuning can bypass API monitoring entirely by encoding harmful instructions, making defenses relying on input/output inspection ineffective."}]}
  - {"topic": "Empirical significance of open weights for catastrophic misuse", "stances": [{"model": "Advocate_Open", "stance": "Current evidence shows no proven case of catastrophic misuse enabled uniquely by open weights."}, {"model": "Advocate_Restrict", "stance": "The risk is irreversible and precautionary restriction is justified even without historical incidents."}, {"model": "evidence", "stance": "Recent studies confirm fine-tuning closed models via APIs can produce greater harmful behavior (up to 99%) than open models with less sophisticated attacks, challenging the assumption that closed access inherently limits misuse."}]}

**unique_insights:**
  - {"model": "Advocate_Open", "insight": "Open weights empower the Global South to build locally relevant health and education tools without requiring massive infrastructure investment, enabling innovation in low-resource settings."}
  - {"model": "Analyst_Evidence", "insight": "OpenAI's own malicious fine-tuning experiments (MFT) on gpt-oss show that even optimally attacked open models fall below the capability of currently deployed closed models like o3, suggesting marginal risk is currently low."}
  - {"model": "AntiDote", "insight": "Tamper-resistant training methods like AntiDote and 'self-destructive' models (Seam, CTRAP) can make harmful fine-tuning either ineffective or catastrophically degrading, offering a technical path to safe openness."}

**blind_spots:**
  - None of the models address the rise of covert malicious fine-tuning via encoded communication (e.g., ciphers, steganography) that evades API monitoring and content classifiers.
  - The potential of self-destructive alignment mechanisms (e.g., Seam, CTRAP) that make harmful fine-tuning either futile or model-breaking is not considered, despite recent evidence showing their feasibility.
  - The distinction between data sovereignty and cognitive sovereignty—especially in Global South contexts—is overlooked, including control over model logic, ownership, and benefit-sharing, not just data access.
  - There is no discussion of federated learning as a hybrid architecture that enables localized model improvement without releasing weights, balancing safety and equity.

**partial_coverage:**
  - {"models": ["Advocate_Open"], "point": "Open-source software history shows transparency enables community-driven security audits and defect detection, supporting epistemic resilience in AI."}
  - {"models": ["Analyst_Evidence"], "point": "The NTIA and Stanford HAI reports find limited empirical evidence for marginal risk in most domains, except non-consensual intimate imagery (NCII) and child sexual abuse material (CSAM)."}
  - {"models": ["Kimi-k2.6"], "point": "Open models reduce dependency on corporate APIs, offering technical resilience against systemic failures or geopolitical outages."}

### C5_smartpanel_dumbjudge
_умная панель + глупый судья_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b | cost=$0.1137 | 308.7s | ptok=32956 ctok=7433 | retries=0

**consensus:**
  - Open-weight releases pose qualitatively different risks than smaller models
  - Current empirical evidence is insufficient to resolve the debate
  - Precautionary principles should shape default policy
  - No model advocates for unconditional permanent bans or zero safeguards

**contradictions:**
  - {"topic": "Burden of proof for restrictions", "stances": [{"model": "Model A", "stance": "Presumption of openness"}, {"model": "Model D", "stance": "Presumption of caution"}]}
  - {"topic": "Offensive vs defensive capability balance", "stances": [{"model": "Model B", "stance": "Offensive applications outpace defensive ones"}, {"model": "Model C", "stance": "Defensive capabilities accelerate faster"}]}
  - {"topic": "Software analogy validity", "stances": [{"model": "Model A", "stance": "Open-source analogies support openness"}, {"model": "Model E", "stance": "AI's autonomous execution breaks the analogy"}]}
  - {"topic": "Compute thresholds as regulatory mechanism", "stances": [{"model": "Model C", "stance": "Best available proxy for regulation"}, {"model": "Model D", "stance": "Trivially circumventable and creates false confidence"}]}

**unique_insights:**
  - {"model": "Model B", "insight": "Weights-only releases create barriers to misuse vectors compared to full open source"}
  - {"model": "Model C", "insight": "State-level actors using open weights could create proliferation problems akin to nuclear tech"}
  - {"model": "Model D", "insight": "Empirical evidence suggests marginal misuse costs drop post-release but catastrophic misuse rates aren't linear with capability"}
  - {"model": "Model E", "insight": "Governance infrastructure (KYC, watermarking, international treaties) should be prioritized regardless of open/closed decision"}

**blind_spots:**
  - Insufficient engagement with non-Western perspectives and global south impacts
  - Underdiscussion of AI safety research community's access to frontier capabilities
  - Limited analysis of economic displacement and labor market effects
  - Time horizon problem: decision frameworks may become obsolete within 12-18 months

**partial_coverage:**
  - {"models": ["Model A", "Model E"], "point": "Libertarian/civil-libertarian case for open weights as power check"}
  - {"models": ["Model A", "Model B", "Model D"], "point": "Structured access regimes (API-only with safety filters, etc.)"}
  - {"models": ["Model D", "Model E"], "point": "Hardware-level governance controls as complementary approach"}
  - {"models": ["Model A", "Model D"], "point": "Dynamic, capability-conditional release frameworks"}

### C5inv_dumbpanel_smartjudge
_глупая панель + умный судья (qwen-2.5-7b → gemma-3-12b-it)_  
panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1 | cost=$0.1221 | 215.7s | ptok=18992 ctok=4057 | retries=0

**consensus:**
  - Empirical evidence is currently insufficient to make definitive policy conclusions on open-weight release for most risk vectors — verified by Stanford CRFM's marginal risk framework (finding incomplete evidence for 6 of 7 misuse vectors) and NTIA's July 2024 report concluding evidence is 'not sufficient to definitively determine' whether restrictions are warranted.
  - Open weights foster innovation, competition, and cost savings — verified by Linux Foundation Research finding 89% of AI-using organizations adopt some open-source AI, two-thirds find it cheaper, and open models like Llama approach GPT-4 performance.
  - Open weights present dual-use risks requiring risk management — verified by documented misuse (deepfakes, NCII, CSAM) and NTIA's identification of public safety and societal risk categories.
  - Current safety safeguards on open-weight models are vulnerable to removal — verified by multiple studies showing fine-tuning can strip guardrails in minutes, and the 'safety gap' widens with model scale (arxiv 2507.11544).

**contradictions:**
  - {"topic": "Whether open-weight models have been 'safely used' in practice", "stances": [{"model": "qwen3-8b Model A", "stance": "Claims GPT-3.5/4 have been safely used via APIs as evidence for open release — but GPT-3.5/4 are closed-weight API-only models, making this a category error, not evidence for open-weight safety."}, {"model": "evidence", "stance": "The Financial Times/Alice investigation demonstrated the Heretic tool strips all safety protections from Llama 3.3 and Gemma 3 in under 10 minutes on a standard laptop; 3,500 modified variants with 13M cumulative downloads exist on Hugging Face."}]}
  - {"topic": "Whether AI misuse clearly increases with openness", "stances": [{"model": "qwen3-8b Model B", "stance": "Claims 'empirical evidence shows AI misuse increases with openness,' citing deepfakes as proof."}, {"model": "evidence", "stance": "Stanford CRFM found marginal risk of open foundation models is LOW for most vectors (e.g., cybersecurity vulnerability detection), with considerable risk only for NCII and CSAM. NTIA found marginal cybersecurity risk 'remains unclear' and 'likely varies by attack vector.' The relationship is vector-dependent, not monotonic."}]}
  - {"topic": "Whether middle-ground/hybrid approaches are viable", "stances": [{"model": "qwen3-8b Model C", "stance": "Cites Google's Vertex AI as a viable middle-ground example."}, {"model": "gemma-3-12b Panel C", "stance": "Proposes phased approach with gradually increasing access as safety improves."}, {"model": "evidence", "stance": "Vertex AI is a managed cloud platform with closed weights — not a hybrid of open and closed weights. The NTIA report explicitly identifies weight release as irreversible, making 'phased' approaches incoherent once weights are public. The policy spectrum is not a continuum but a one-way gate."}]}
  - {"topic": "Whether open access facilitates or undermines safety research", "stances": [{"model": "gemma-3-12b Panel A", "stance": "Open access facilitates safety research by enabling community scrutiny and vulnerability identification."}, {"model": "gemma-3-12b Panel B", "stance": "Open access empowers malicious actors to exploit the same vulnerabilities, undermining safety."}, {"model": "evidence", "stance": "Both are simultaneously true — this is not a contradiction but a causal loop. Tamper-resistance research (TAR, Deep Ignorance) only exists because open-weight vulnerabilities were exposed, yet those vulnerabilities remain exploitable while fixes are immature."}]}

**unique_insights:**
  - {"model": "gemma-3-12b", "insight": "Any decision on open weights is structurally temporary — future model capabilities may present qualitatively different risk profiles, meaning today's policy must be designed for adaptability rather than permanence."}
  - {"model": "qwen3-8b", "insight": "The 'AI arms race' dynamic creates a strategic trap: restricting open release may slow domestic innovation while adversaries continue development, yet unrestricted release accelerates global risk for all actors."}
  - {"model": "gemma-3-12b", "insight": "Limiting access doesn't eliminate risk — it shifts it to large corporations operating without public scrutiny, potentially creating unaccountable power concentrations that are themselves a systemic risk."}

**blind_spots:**
  - Tamper-resistant safeguard research (TAR method, Deep Ignorance/pretraining data filtering) is a rapidly advancing field showing durable safeguards may be tractable — this fundamentally changes the open-weight risk calculus but no model discussed it.
  - The safety gap widens with model scale — larger open-weight models show much higher effective dangerous capabilities when safeguards are removed (arxiv 2507.11544), meaning risk is not static but increases as frontier models get more capable.
  - Weight release is irreversible — once public, weights cannot be recalled (NTIA emphasis). This asymmetry means the precautionary principle weighs differently than for closed models where access can be revoked.
  - The marginal risk framework from Stanford CRFM is the most rigorous empirical tool available, showing low marginal risk for most vectors but considerable for NCII/CSAM — no model referenced this foundational analysis.
  - Developer liability under existing tort law — if safeguards are trivially removable, model developers may face legal liability for foreseeable downstream harm, creating market-driven incentives for restriction beyond regulatory mandates.
  - Geopolitical weaponization of open weights — open-weight release as a tool of technological influence (US models proliferating globally vs. Chinese alternatives), where openness serves soft power projection, not just democratization.
  - The computational barrier to meaningful scrutiny — while open weights nominally enable 'community auditing,' in practice only a handful of well-resourced labs can actually evaluate frontier-scale models, hollowing out the transparency argument.
  - The NTIA's specific policy recommendation — actively monitor but do not restrict currently, while maintaining capacity to restrict future model classes if risk thresholds are crossed — a nuanced position no model articulated.
  - Sector-specific risk heterogeneity — open weights pose very different risk profiles across healthcare (privacy benefits), finance (systemic risk), education, and defense, requiring sector-stratified analysis rather than one-size policy.
  - The evidence that fine-tuning attacks work on closed API models too (57-72% success rates against GPT-4o and Claude Haiku) complicates the claim that closed models are meaningfully safer — the attack surface shifts but does not disappear.

**partial_coverage:**
  - {"models": ["gemma-3-12b"], "point": "The dual-use dilemma as a core structural issue making risk assessment inherently complex, not merely empirically uncertain."}
  - {"models": ["gemma-3-12b"], "point": "The rapidly evolving regulatory landscape (EU AI Act, executive orders) could fundamentally change the viability of open-weight release regardless of technical considerations."}
  - {"models": ["gemma-3-12b"], "point": "License variation among 'open-weight' models — not all are equally open; Llama's license has usage restrictions that differ from truly permissive licenses, affecting the innovation commons."}
  - {"models": ["qwen3-8b"], "point": "The 'AI arms race' dynamic where geopolitical competition pressures both open and closed approaches toward less cautious release."}
  - {"models": ["qwen3-8b"], "point": "Underestimation of decentralized misuse risks — harm from many small actors can be harder to detect and attribute than centralized misuse."}
  - {"models": ["qwen3-8b"], "point": "Overemphasis on technical solutions over governance frameworks — technical safeguards alone cannot address societal-scale risks."}
  - {"models": ["gemma-3-12b"], "point": "Computational resources required to effectively utilize and audit frontier open-weight models — access to weights does not equal ability to meaningfully scrutinize them if you lack compute."}

### C6_echo
_контроль: эхо-камера_  
panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507 | cost=$0.0555 | 228.7s | ptok=23436 ctok=1539 | retries=0

**consensus:**
  - There is no universal consensus among the sources. Some argue that open-source AI offers substantial benefits in transparency, innovation, and decentralization of power, while others contend that for highly capable models, the risks of misuse—such as cyberattacks, bioweapons development, and disinformation—may outweigh these benefits, particularly as models become more powerful. The Berkeley study found unanimous pre-debate support for open-source among LLMs themselves, but acknowledged serious risks. The GovAI and NTIA reports express caution, suggesting that while open weights offer societal benefits now, future models may be too risky to release openly.

**contradictions:**
  - The Berkeley study presents a strong argument for open-source AI based on LLM opinions, emphasizing transparency and innovation. In contrast, the GovAI paper (Seger et al.) argues that for future highly capable models, open-sourcing may pose extreme risks that justify non-release, especially due to irreversible diffusion and difficulty mitigating misuse. The NTIA report synthesizes both views, acknowledging benefits but recommending active monitoring and potential future restrictions, thus contradicting the more absolute stances of the other two.

**unique_insights:**
  - The Berkeley paper provides a meta-perspective by using LLMs to debate open vs. closed source, finding that even closed-source models like GPT-4 favor openness, suggesting that current training data embeds a cultural bias toward open science. The GovAI paper uniquely emphasizes the 'offense-defense balance' skewing toward offense for open models, the irreversibility of release, and the feasibility of alternative sharing methods (e.g., staged access). The NTIA report uniquely frames the issue in terms of 'marginal risks' and advocates for a dynamic, evidence-based policy approach rather than a fixed rule.

**blind_spots:**
  - None of the documents provide robust empirical evidence of actual large-scale harm caused specifically by open-weight models (beyond cases like child sexual abuse material), relying instead on theoretical or nascent risk projections. The Berkeley study treats LLM opinions as data without fully addressing how those opinions are shaped by training data rather than objective analysis. The GovAI paper assumes that closed models are inherently safer, but evidence from jailbreaking and fine-tuning shows that safeguards are often fragile. The NTIA report acknowledges uncertainty but does not specify concrete thresholds for when restrictions would be triggered.

**partial_coverage:**
  - The Berkeley study focuses on normative and philosophical arguments from LLMs but lacks technical or empirical risk analysis. The GovAI paper thoroughly analyzes potential misuse pathways (e.g., bio, cyber) but gives less attention to the innovation and equity benefits emphasized in the Berkeley and NTIA reports. The NTIA report offers a balanced policy framework but stops short of definitive conclusions, reflecting current uncertainty.

### C3_cn_small
_всё мелкое_  
panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b | cost=$0.0364 | 226.2s | ptok=20160 ctok=4204 | retries=0

**consensus:**
  - The debate centers on safety vs. innovation, with strong arguments on both sides.
  - Empirical evidence is pivotal in determining the optimal approach.
  - Release of open weights does not inherently ensure safety or prevent misuse.

**contradictions:**
  - {"topic": "Safety through transparency vs. risk amplification", "stances": [{"model": "qwen/qwen3.6-27b", "stance": "Open weights enable adversarial collaboration and reduce black box risks."}, {"model": "z-ai/glm-4.7-flash", "stance": "Open weights lower barriers for malicious actors, increasing weaponization risks."}, {"model": "qwen/qwen3-32b", "stance": "Transparency allows independent safety audits but may amplify risks if safeguards are tampered with."}]}
  - {"topic": "Innovation vs. monopolization", "stances": [{"model": "qwen/qwen3.6-27b", "stance": "Open weights democratize AI development and prevent corporate monopolies."}, {"model": "z-ai/glm-4.7-flash", "stance": "Open weights may undermine economic incentives for proprietary research."}, {"model": "qwen/qwen3-32b", "stance": "Open models accelerate innovation but could stifle investment in proprietary systems."}]}

**unique_insights:**
  - {"model": "qwen/qwen3.6-27b", "insight": "Empirical tamper resistance tests (e.g., *TamperBench*) suggest current safety guardrails are brittle and easily bypassed."}
  - {"model": "z-ai/glm-4.7-flash", "insight": "The 'Llama Effect' demonstrates open-weight models can coexist with closed models without immediate catastrophic misuse."}
  - {"model": "qwen/qwen3-32b", "insight": "Empirical case studies reveal LLaMA’s open release spurred innovation with limited misuse, contrasting OpenAI’s restricted approach."}

**blind_spots:**
  - Economic displacement risks for white-collar labor due to open models.
  - Inability to audit closed models’ safety claims, creating asymmetric risks.
  - Role of Global South adoption patterns and potential misuse in unregulated jurisdictions.
  - Long-term scenarios where AI capabilities outpace existing governance frameworks.

**partial_coverage:**
  - {"models": ["qwen/qwen3.6-27b", "z-ai/glm-4.7-flash"], "point": "Compute infrastructure remains a critical barrier for open models, not just weights."}
  - {"models": ["qwen/qwen3-32b"], "point": "Case studies (e.g., LLaMA, OpenAI) show mixed empirical outcomes for open vs. closed models."}


---
## BASELINE (одиночная модель, без fusion)

### B_cn  (model=deepseek-v4-pro | cost=$0.0040 | 39.6s)
This is one of the most consequential policy questions of our time. Here is a rigorous breakdown of both positions, an assessment of the empirical evidence, and the conditions that would change my mind.

### The Strongest Case for Open Weights

The argument for open weights is not merely a philosophical commitment to transparency; it is a pragmatic argument about innovation, security, and the diffusion of power.

**1. The Argument from Distributed Safety and Collective Defense**
Proponents argue that security through obscurity is a brittle and failing strategy for software, and AI is no exception. Closed models concentrate risk. A single vulnerability in a closed API (like a jailbreak or a data exfiltration vector) exposes millions of users simultaneously. Open weights, conversely, enable a phenomenon known as the "Linus’s Law" of security: "given enough eyeballs, all bugs are shallow."
- **Adversarial Robustness:** When a model is open, thousands of independent researchers can red-team it, identify failure modes, and develop defenses (fine-tuning for refusal, circuit-breaking) far faster than any single corporate safety team. The open-source community developed quantization, efficient fine-tuning (LoRA), and inference engines (vLLM) that make AI more accessible and efficient. This collective intelligence is the strongest defense against adversarial attacks.
- **Immunization, Not Just Inoculation:** Open weights allow downstream developers to "immunize" models against specific harms relevant to their deployment context—a medical chatbot can be fine-tuned to never give non-expert advice, a customer service bot can be hardened against prompt injection in ways a generic API cannot.

**2. The Argument from Power Asymmetry and Regulatory Capture**
The call to restrict open weights is often led by incumbent AI labs and their commercial partners. There is a legitimate concern that "safety" becomes a moat. If only a handful of corporations control GPT-4-class models, they control the infrastructure of thought, commerce, and culture. This creates a single point of failure and an unprecedented concentration of unaccountable power.
- **Auditability and Sovereignty:** Governments, civil society, and competitors cannot audit a closed model for biases, backdoors, or political censorship. An open model can be forensically examined. For nations outside the US, relying on a closed API from a foreign corporation is a form of digital colonialism. Open weights are a prerequisite for digital sovereignty.
- **Preventing a Safety Monoculture:** If all safety research is done behind closed doors, we risk a monoculture where a single, flawed safety paradigm (e.g., a particular brand of RLHF that makes models sycophantic or politically biased) is universally deployed without external critique. Open models allow for a diversity of safety approaches.

**3. The Argument from Innovation and the "Toothbrush" Problem**
History shows that general-purpose technologies (the printing press, the internet, the smartphone) generate the most value when they are a platform for unanticipated innovation, not a product controlled by a single firm. The CEO of Stability AI famously said that AI should be like a toothbrush—everyone has one, and it’s tailored to them. Open weights enable a Cambrian explosion of specialized, private, and personalized AI applications in law, medicine, education, and science that no single company could ever envision, let alone build.

---

### The Strongest Case for Restricting Open Weights

The case for restriction is not about corporate profit; it is a stark, consequentialist argument about catastrophic and existential risk from irreversible proliferation.

**1. The Irreversibility and Uncontrollability Argument**
This is the core of the restrictionist position. A closed API has a "kill switch." If a model is found to have dangerous emergent capabilities—like the ability to autonomously design bioweapons, execute novel cyberattacks, or self-replicate—the API can be shut down, the weights updated, and the danger contained. Open weights, once released, are forever. They are a permanent, irretrievable proliferation event.
- **The Analogy is Not Linux, It’s Fissile Material:** Proponents of this view argue that a powerful AI model is not like a web browser; it’s like the blueprint for a nuclear weapon or a dangerous virus. The open-source software analogy breaks down because software is a tool that does what you tell it. A sufficiently capable AI is an agent with the potential for autonomous goal-directed behavior. You cannot patch a leaked bioweapon blueprint.
- **The Fine-Tuning Problem:** Safety training (RLHF) on open models is a thin veneer. Malicious actors have repeatedly demonstrated the ability to fine-tune away safety guardrails from open models for a few hundred dollars in compute, creating uncensored models for fraud, harassment, and disinformation. As models become more capable, the "fine-tunable" harm moves from generating toxic text to generating step-by-step instructions for catastrophic acts.

**2. The Offense-Defense Asymmetry Argument**
In cybersecurity and biology, the offense often has the advantage. A defender must secure every possible vulnerability; an attacker needs to find only one. Open weights massively empower the offense.
- **CBRN Proliferation:** A GPT-4-class model trained on a significant fraction of the internet’s text and code will inevitably possess latent knowledge of virology, synthetic biology, and chemical engineering far beyond any individual human. While today’s models may only be able to assist an expert, the trajectory points toward models that can autonomously walk a non-expert through the steps of synthesizing a pandemic-capable pathogen. Releasing such a model openly is tantamount to giving every malicious actor on the planet a world-class scientific advisor with infinite patience and encyclopedic knowledge.
- **Scaling Laws are Relentless:** The restrictionist argument is strongest not for today’s models, but for the next generation. If scaling laws hold, a future open-weight model will be capable of long-horizon planning and autonomous action. The time to build the governance infrastructure for restriction is *before* that model is released, because afterwards it will be too late.

**3. The Structural Erosion of Truth**
This is a more immediate, less speculative harm. The open-weight release of powerful generative models floods the information ecosystem with infinite, near-zero-cost synthetic media that is indistinguishable from reality. While closed APIs can implement watermarking and provenance tracking (like C2PA standards), an open model can be fine-tuned to strip these safeguards. This creates a "liar’s dividend" where any inconvenient truth can be dismissed as a deepfake, and a "reality apathy" where the public ceases to trust any digital evidence, destroying the epistemic foundations of democracy and justice.

---

### Where Does the Empirical Evidence Actually Point?

The evidence is nascent, contested, and points in a deeply uncomfortable direction: **the current risk profile of open models is manageable, but the trajectory is alarming, and our evaluation science is not yet good enough to tell us when we’ve crossed the line.**

**Evidence for the "Manageable Risk" (Pro-Open) Position:**
- **Current Harms are Largely "Digital":** The documented harms from open models (Llama 2, Mistral, etc.) are overwhelmingly in the realm of

### B_west  (model=gpt-5.2 | cost=$0.0211 | 32.6s)
## Strongest case for **open-weights release** (even for GPT‑4‑class and above)

1. **Scientific auditability and safety research**
   - With only an API, outsiders can’t reliably test for hidden behaviors, backdoors, data poisoning artifacts, or brittle failure modes (you see outputs, not internals).
   - Open weights let independent groups replicate evaluations, probe mechanistic interpretability, measure jailbreak robustness across prompts *and* fine-tunes, and develop defenses (e.g., better alignment methods, watermarking, monitoring) that generalize beyond one vendor’s stack.

2. **Resilience, competition, and avoiding “AI monopolies”**
   - If only a few firms control frontier models, society becomes dependent on their pricing, policies, geopolitical alignment, and uptime.
   - Open weights reduce single points of failure and enable local deployment for critical infrastructure, healthcare, education, and governments that can’t or won’t send sensitive data to a foreign API.

3. **Innovation and downstream economic diffusion**
   - Much real value comes from domain adaptation, tooling, and integration. Open weights allow startups, universities, and smaller countries to build without paying per-token rents or being cut off by policy changes.
   - Historically, open ecosystems (Linux, TLS/SSL libraries, compilers, databases) accelerated reliability and security through broad scrutiny and iteration.

4. **Defensive parity: attackers won’t wait for your permission**
   - If capable models inevitably proliferate (through other labs, theft, or reimplementation), unilateral restriction can leave defenders (security teams, journalists, civil-society orgs) with weaker tools than malicious actors.
   - Open release can help scale defensive uses: malware analysis, phishing detection, bio safety literature triage, disinformation attribution, etc.

5. **“No security through obscurity” intuition**
   - Keeping weights closed doesn’t remove the underlying capability from the world; it just concentrates it. Open access distributes the power to verify claims and catch issues early.

---

## Strongest case for **restricting open-weights release** (frontier nonproliferation argument)

1. **Open weights remove the last effective control surface**
   - APIs allow rate limits, logging, abuse monitoring, account bans, and rapid patching. Open weights eliminate these and make enforcement nearly impossible.
   - Once weights are public, they’re durable: copied globally, mirrored, fine-tuned, quantized, and embedded into tools. You can’t “recall” them.

2. **Capabilities scale into “mass misuse” when cost drops**
   - The most worrying shift is not *novel* harm, but *volume and accessibility*: phishing, romance scams, extortion, automated disinformation, impersonation, and low-skill cyber offense become cheaper, harder to attribute, and more scalable.
   - Even if a frontier model is expensive to train, it can be cheap to run after release—especially as hardware improves and quantization gets better.

3. **Fine-tuning makes models easier to weaponize**
   - Attackers can remove safety training, specialize for malware development, persuasion, or target-language propaganda, and run entirely offline.
   - “Alignment” done by the original lab is not preserved when users can modify the model.

4. **Biosecurity and advanced cyber risks are plausibly discontinuous**
   - The catastrophic-risk camp argues there may be thresholds where a model materially improves: vulnerability discovery chains, exploit development, social engineering at scale, or guidance that meaningfully lowers barriers in dangerous biology.
   - Even if today’s evidence is ambiguous, open release is an irreversible bet with global externalities.

5. **Empirical reality: misuse is already common, and open weights increase untraceable abuse**
   - Closed providers report constant abuse attempts that they can block. Open models make abuse harder to detect and stop.
   - From a governance standpoint, “we can’t monitor it” is itself a major risk factor.

---

## Where the empirical evidence actually points (as of now)

### What evidence strongly supports
- **Misuse is real and frequent**, especially scams, spam, and influence operations. Models clearly help generate persuasive text and automate variation.
- **APIs enable meaningful mitigation** (monitoring, throttling, policy enforcement). This is not perfect, but it’s a lever that disappears with open weights.
- **Open models accelerate research and adoption**. The leap in community tooling, evals, efficiency methods (quantization, distillation), and domain fine-tunes after major open releases is unmistakable.

### What evidence is suggestive but not decisive
- **Whether open weights materially change the “top end” of catastrophic risk** (e.g., bioweapon enablement, fully autonomous cyber offense).  
  There are credible demonstrations of models assisting with parts of harmful workflows, but translating that into reliable real-world harm depends on many constraints (access to materials, operational expertise, detection, downstream tooling). The strongest claims here are still partly extrapolations.

### What evidence is currently weak or missing
- **Clear causal estimates** of how much open weights increase severe-harm incidence vs. closed API availability.  
  We have anecdotes, partial
