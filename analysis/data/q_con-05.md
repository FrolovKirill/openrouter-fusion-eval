# con-05 — Psychology replication crisis prognosis
**Block:** contested

**Prompt:**
How seriously damaged is psychology as a scientific discipline due to the replication crisis? Is the field recovering, getting worse, or is the crisis overblown? What reforms have actually worked, and what should a researcher or policymaker conclude from this?

---
## FUSION-конфиги (judge-анализ; responses вынесены в resp_*.md)

### C1_west_closed
_западный закрытый фронтир_  
panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2 | cost=$0.3498 | 215.1s | ptok=18819 ctok=2199 | retries=0

**consensus:**
  - The replication crisis exposed real, nontrivial reliability problems in parts of psychology (e.g., inflated effect sizes and some notable non-replications), driven in part by low power, selective reporting/publication bias, and flexible analyses (QRPs); large-scale replication efforts have repeatedly found substantially lower replication success and/or smaller effects than original reports (evidence: Open Science Collaboration 2015; Many Labs 2 2018).
  - Psychology has implemented and normalized multiple “open science”/metascience reforms in response (e.g., preregistration, Registered Reports, open data/materials/code, and multi-lab collaborations), and these reforms have increased transparency and enabled stronger error-detection and self-correction (evidence: documented growth of open practices and large-scale replication infrastructures; e.g., Psychological Science badge program).
  - Some reforms have demonstrably improved specific outcomes even if they do not guarantee truth: Registered Reports reduce the skew toward ‘positive’ findings (evidence: Scheel, Schijen & Lakens 2021: much lower positive-result rates in RRs than standard reports), and journal incentives like open-practices badges can materially increase data sharing (evidence: Kidwell et al. 2016: large increase in reported/actual open data at Psychological Science after badges).

**contradictions:**
  - {"topic": "Overall severity/framing: ‘seriously damaged’ discipline vs. ‘credibility revolution’ and recovery", "stances": [{"model": "google/gemini-3.1-pro-preview", "stance": "Substantial credibility damage (especially for some historically celebrated findings/subfields) but not a collapse; field is recovering and leading reforms."}, {"model": "x-ai/grok-4.3", "stance": "Primarily a positive reform story (‘credibility revolution’); field is recovering rather than irreparably damaged."}, {"model": "openai/gpt-5.2", "stance": "No substantive stance (tooling error)."}, {"model": "evidence", "stance": "Both ‘severe damage’ and ‘mostly solved’ framings are underdetermined globally: replication success varies by area/method; many reforms improve transparency, but legacy literatures remain biased and many domains (observational, measurement-heavy, hard-to-replicate) are not ‘fixed’ by procedural reforms alone."}]}
  - {"topic": "Do preregistration/‘best practices’ raise replication rates to ~86–90% in general?", "stances": [{"model": "x-ai/grok-4.3", "stance": "Claims reforms (preregistration + transparency + large samples) can yield replication rates up to ~86–90%, implying dramatic improvement."}, {"model": "google/gemini-3.1-pro-preview", "stance": "Suggests such reforms are effective and contribute to higher reliability, but does not centrally anchor on a field-wide 90% figure."}, {"model": "openai/gpt-5.2", "stance": "No substantive stance (tooling error)."}, {"model": "evidence", "stance": "The flagship 86–90% figure cited in popular summaries comes from a Nature Human Behaviour article that was retracted (Sept 2024), so it is not a secure basis for claiming that preregistration/best practices generally boost replication to ~90%; moreover, large-scale replication projects of published findings often report much lower success rates (e.g., Many Labs 2 ~50–54% by p<.05 criteria)."}]}
  - {"topic": "Primary explanation for replication failures: methodological bias/QRPs vs. context sensitivity/hidden moderators", "stances": [{"model": "google/gemini-3.1-pro-preview", "stance": "Acknowledges widespread QRPs/low power/publication bias but stresses that some failures may reflect context dependence/boundary conditions rather than simple falsity; also raises a ‘theory crisis’ angle."}, {"model": "x-ai/grok-4.3", "stance": "Emphasizes procedural reforms and tracking; mentions contextual/complexity caveats but is less focused on theory/moderator explanations."}, {"model": "openai/gpt-5.2", "stance": "No substantive stance (tooling error)."}, {"model": "evidence", "stance": "Both mechanisms matter: selective reporting/analysis flexibility and low power inflate initial claims, while heterogeneity and construct/measurement differences can also cause genuine effect variation; without strong theory specifying moderators, ‘context dependence’ can become unfalsifiable post hoc."}]}
  - {"topic": "Which reforms ‘actually worked’: preregistration vs. Registered Reports vs. other changes", "stances": [{"model": "google/gemini-3.1-pro-preview", "stance": "Highlights preregistration, Registered Reports, open data/code, and multi-lab replications as effective; also suggests shifts away from p-values/Bayesian approaches."}, {"model": "x-ai/grok-4.3", "stance": "Highlights preregistration/transparency/large-scale collaborations as key effective reforms; less emphasis on distinguishing preregistration from Registered Reports."}, {"model": "openai/gpt-5.2", "stance": "No substantive stance (tooling error)."}, {"model": "evidence", "stance": "Registered Reports have clearer empirical support for reducing publication bias and improving rigor/transparency; preregistration alone often improves transparency and planning but has mixed evidence for reducing the proportion of ‘positive’ results and is vulnerable to vagueness/nonbinding plans (evidence: Scheel et al. 2021 on RRs; comparative preregistration analyses showing no clear drop in positive-result rates despite other quality gains)."}]}

**unique_insights:**
  _(пусто)_

**blind_spots:**
  - No model provides a field-wide, decision-relevant way to quantify ‘how damaged’ psychology is (by subfield, method type, outcome type), distinguishing: (i) computational reproducibility, (ii) replicability of effects, (iii) external validity/generalizability, and (iv) construct/measurement validity.
  - Insufficient attention to measurement/construct validity as a core driver of non-replication (changing instruments, low reliability, and ambiguous operationalizations), which procedural reforms do not automatically solve.
  - Little discussion of heterogeneity across psychology: clinical/intervention research, longitudinal/observational designs, psychometrics, neuroscience, and qualitative/mixed methods have different failure modes and different feasible reforms than short online experiments.
  - No serious treatment of meta-analysis fragility under publication bias and p-hacking (e.g., small-study effects, selection models), despite policymakers often relying on meta-analyses; also no guidance on evidence-grading frameworks (risk-of-bias tools, GRADE-like approaches) for policy translation.
  - Neglect of reform side-effects and failure modes: preregistration as ‘box-checking,’ under-specified analysis plans, selective interpretation despite preregistration, and potential deterrence of exploratory work without clear exploratory/confirmatory separation.
  - No coverage of post-2020 integrity challenges such as paper mills, synthetic/fabricated data detection, and retractions as part of the reliability landscape; nor how open data/code and audits can mitigate them.
  - Policy guidance remains too coarse: missing concrete recommendations like requiring independent replication for high-stakes interventions, funding replication/implementation studies, using multi-site trials, and treating single studies as provisional regardless of prestige.

**partial_coverage:**
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "‘Theory crisis’/verbal-theory vagueness: replication reform is insufficient without stronger theory-to-prediction links and clearer boundary conditions."}
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "Institutional incentives (tenure/grants valuing novelty/volume) as a root cause; reforms may stall without incentive realignment."}
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "WEIRD sampling/generalizability problems as related to (but distinct from) replication; need diverse real-world testing."}
  - {"models": ["x-ai/grok-4.3"], "point": "Big Team Science infrastructures (e.g., Many Labs/PSA-style collaborations) as a mechanism for accelerating cumulative evidence and standardizing high-powered replications."}
  - {"models": ["google/gemini-3.1-pro-preview", "x-ai/grok-4.3"], "point": "Public trust implications are mentioned but only lightly developed (how to communicate uncertainty and reform without misleading ‘all broken’ vs ‘all fixed’ narratives)."}

### C2_cn_open
_открытый китайский фронтир (умн+умн)_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507 | cost=$0.2162 | 366.0s | ptok=31655 ctok=6974 | retries=0

**consensus:**
  - Psychology has experienced a replication crisis with initial large-scale replication projects (e.g., Open Science Collaboration, 2015) finding replication rates between 36% and 47% for seminal studies.
  - Reforms such as preregistration and Registered Reports have substantially reduced positive result rates—from ~96% in standard submissions to ~44%—indicating a reduction in publication bias.
  - Registered Reports are associated with higher ratings in methodological rigor and overall paper quality compared to standard publications, without sacrificing creativity or novelty.
  - The field is demonstrating measurable signs of recovery, including stronger reported p-values (fewer p-values between .01 and .05), larger sample sizes, and increased transparency practices since the mid-2010s.
  - Media attention and citation counts are positively associated with replication failure, suggesting a bias toward publishing surprising or novel but less replicable results.
  - The use of online data collection platforms (e.g., Mechanical Turk, Prolific) has contributed to larger sample sizes, though concerns remain about data quality (e.g., bots, inattentive participants).

**contradictions:**
  - {"topic": "Baseline replication rate and severity of the crisis", "stances": [{"model": "z-ai/glm-5.1", "stance": "The original Open Science Collaboration (OSC) study’s finding of only 36–47% replication is valid evidence of a serious crisis affecting the credibility of psychology."}, {"model": "moonshotai/kimi-k2.6", "stance": "While replication rates were low, improvements in p-value strength and methodological norms suggest the crisis prompted necessary reform rather than indicating systemic collapse."}, {"model": "evidence", "stance": "The replication rate of 36–47% is not a definitive measure of falsity: failed replications may arise from methodological deviations, theoretical boundary shifts, or contextual differences, not just false positives. Moreover, large-scale studies such as the 'Many Labs' projects and machine-learning estimates suggest variability across subfields and methodologies; thus, a single replication rate for the entire field is misleading."}]}
  - {"topic": "Effectiveness of preregistration without peer review", "stances": [{"model": "z-ai/glm-5.1", "stance": "Preregistration without peer review or detailed pre-analysis plans is often performative; it does not reliably reduce p-hacking or HARKing because preregistrations are frequently underspecified and deviations go undisclosed."}, {"model": "moonshotai/kimi-k2.6", "stance": "Combining preregistration with transparency and large samples boosts replication rates to ~86%, suggesting preregistration is effective when fully implemented."}, {"model": "evidence", "stance": "A 2023 study published in *Nature Human Behaviour* reporting an 86% replication rate among preregistered studies was retracted due to methodological concerns. The retraction undermines confidence in that high replication rate, suggesting methodological rigor in replication projects themselves must be questioned, and that not all preregistered studies are equally robust."}]}
  - {"topic": "Impact of public awareness of the replication crisis on trust", "stances": [{"model": "z-ai/glm-5.1", "stance": "Public trust in psychology decreases when laypeople are informed of replication failures, with experimental studies showing reduced trust ratings after exposure to crisis narratives."}, {"model": "moonshotai/kimi-k2.6", "stance": "The German public is largely unaware of the crisis, and those who are aware often interpret replication efforts positively—as signs of science’s self-correcting nature—suggesting no broad trust crisis exists."}, {"model": "evidence", "stance": "Trust effects are context-dependent: a study found that informing people about replication failures reduces trust, but trust can be restored or even enhanced when the message includes information about ongoing reforms. However, a 2023 European study found that even providing reform information led to lower expectations of future research, indicating complex and fragile public trust dynamics."}]}

**unique_insights:**
  - {"model": "z-ai/glm-5.1", "insight": "The crisis is better reframed as the resolution of a long period of methodological unawareness, where the field’s current self-correction represents scientific maturity rather than collapse—comparable to rain after drought, not the drought itself."}
  - {"model": "moonshotai/kimi-k2.6", "insight": "Experimental studies in psychology replicate at significantly lower rates than non-experimental studies across all subfields, which is concerning because experiments are central to psychology’s scientific standing."}

**blind_spots:**
  - The retraction of a high-profile study claiming 86% replication rates under rigorous conditions (e.g., preregistration, large samples), as reported in a 2023 Science news article, was not addressed by any model. This retraction raises concerns about the reliability of claimed reform effects and the potential for overconfidence in reform narratives.
  - None of the models accounted for the fact that the most commonly cited replication success metric—the Open Science Collaboration (2015) 36–47%—is based on a selective sample of high-impact, novel studies, not a random sample of the literature, which may bias downward estimates of overall replicability.
  - There is inadequate discussion about whether current reforms (e.g., preregistration, Registered Reports) are scalable to complex, longitudinal, or clinical research, where treatment fidelity, ethical constraints, and participant retention pose unique challenges.
  - No model addressed how machine learning models or prediction markets—used to estimate replication likelihood at scale—may introduce their own biases, especially when applied to subfields (e.g., clinical, developmental) underrepresented in training data.
  - The impact of institutional and national research funding policies on replication practices and reform adoption remains unexplored, particularly outside North America and Western Europe.

**partial_coverage:**
  - {"models": ["z-ai/glm-5.1", "moonshotai/kimi-k2.6"], "point": "Subdisciplinary differences in replication success are evident, with cognitive psychology showing higher replicability than social psychology in some studies, but clinical and developmental psychology remain understudied due to fewer manual replications, resource constraints, and ethical limitations."}
  - {"models": ["z-ai/glm-5.1"], "point": "The epistemological debate over 'exact' replication is relevant: successful replication may depend on whether theoretical boundary conditions are preserved, not just procedural fidelity, suggesting that some 'failures' may reflect theoretical nuance rather than methodological failure."}
  - {"models": ["moonshotai/kimi-k2.6"], "point": "Incentive misalignment persists at elite institutions: researchers at top-ranked universities publish work with weaker p-values, not due to poor practices, but because they conduct resource-intensive, subtle research with inherently lower statistical power, complicating the interpretation of p-values as a universal metric of robustness."}

### C5_smartpanel_dumbjudge
_умная панель + глупый судья_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b | cost=$0.2358 | 499.3s | ptok=30991 ctok=6798 | retries=0

**consensus:**
  - Psychology experienced a real replication crisis with low replication rates (36-39% in large-scale projects) and widespread questionable research practices.
  - The field has made measurable progress through reforms like preregistration, registered reports, larger samples, and open science practices.
  - The crisis is not fully resolved; current replication rates (~55%) remain below the threshold of a healthy field (~75%).
  - The 'credibility revolution' has spurred structural and cultural shifts toward transparency and rigor.

**contradictions:**
  - {"topic": "Was the crisis overblown?", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "Some argue the crisis was overblown due to misleading dichotomies in replication narratives"}, {"model": "z-ai/glm-5.1", "stance": "Gilbert et al. (2016) argued the original OSC replication rate was severely underestimated"}, {"model": "z-ai/glm-5.1", "stance": "Pashler & Harris (2012) reject the 'overblown' narrative, arguing 59.7% replication rate is still below expectations"}, {"model": "moonshotai/kimi-k2.6", "stance": "The crisis was serious but not overblown in its origins"}]}
  - {"topic": "Effectiveness of preregistration", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "Preregistration has improved replication rates (86% in recent projects)"}, {"model": "z-ai/glm-5.1", "stance": "Van den Akker et al. (2023) found no robust evidence preregistration prevents p-hacking"}, {"model": "moonshotai/kimi-k2.6", "stance": "Preregistration reduces incentive to hunt for significant findings"}]}

**unique_insights:**
  - {"model": "deepseek/deepseek-v4-pro", "insight": "The 'psychology of science' perspective: confirmation bias and anthropological oversimplification are fundamental to the crisis"}
  - {"model": "z-ai/glm-5.1", "insight": "Prediction markets (e.g., repliCATS) can predict replicability with 61-86% accuracy"}
  - {"model": "moonshotai/kimi-k2.6", "insight": "DORA (Declaration on Research Assessment) and funding infrastructure for open science"}

**blind_spots:**
  - Qualitative research challenges in open science frameworks
  - Philosophical/epistemological dimensions of the crisis
  - Cultural and geographic diversity in research participants and researchers
  - Long-term impact of open science policies on career incentives
  - Role of publication bias in shaping the crisis narrative

**partial_coverage:**
  - {"models": ["deepseek/deepseek-v4-pro"], "point": "Link between university prestige and fragile p-values persists despite improved journal standards"}
  - {"models": ["z-ai/glm-5.1"], "point": "Theoretical poverty and lack of formal frameworks as root causes of replicability issues"}
  - {"models": ["moonshotai/kimi-k2.6"], "point": "Tension between elite institutions' resource-intensive research and statistical robustness"}

### C5inv_dumbpanel_smartjudge
_глупая панель + умный судья (qwen-2.5-7b → gemma-3-12b-it)_  
panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1 | cost=$0.1171 | 357.4s | ptok=26927 ctok=5925 | retries=1

**consensus:**
  - The replication crisis significantly damaged psychology's scientific credibility, with the 2015 Open Science Collaboration finding only ~39% replication success and effect sizes roughly half the originals.
  - The field is actively recovering through structural reforms including preregistration, open data sharing, larger sample sizes, registered reports, and collaborative replication networks.
  - Recovery is uneven across subfields: cognitive psychology shows stronger replication rates while clinical and developmental psychology lag, partly due to practical constraints on sample sizes.
  - Systemic incentive misalignment persists—publication bias, career rewards for novelty over rigor, and pressure for prolific output continue to undermine reform efforts.
  - Fragile p-values (.01–.05) have measurably decreased (from ~32% to ~26% per Bogdan 2025), indicating real improvement in statistical robustness across the literature.

**contradictions:**
  - {"topic": "Effectiveness of preregistration at boosting replication", "stances": [{"model": "glm-4.7-flash", "stance": "Preregistered studies show 86% replication success, far above baseline, proving preregistration works."}, {"model": "evidence", "stance": "The Nature Human Behaviour paper reporting 86% was RETRACTED; a 2023 Behavior Research Methods study found preregistered studies did NOT show lower positive result rates or smaller effect sizes than non-preregistered ones, though they did have larger samples and more power analyses."}]}
  - {"topic": "Public trust reparability after the crisis", "stances": [{"model": "glm-4.7-flash", "stance": "Trust repair strategies show mixed effectiveness, with some studies finding no significant improvement despite transparency efforts."}, {"model": "gemma-3-12b-it", "stance": "Varies—some models suggest significant erosion of trust, others believe impact on public perception has been limited."}, {"model": "evidence", "stance": "Wuttke et al. (2020) found transparency information alone did not repair trust; but Methner et al. (2022) found comprehensive reform information DID increase trust in researchers and current findings. Effectiveness depends on depth and quality of communication, not a simple yes/no."}]}
  - {"topic": "Whether the crisis is overblown", "stances": [{"model": "qwen3-8b", "stance": "Some researchers argue the crisis is overblown, citing high-quality work in subfields like cognitive psychology."}, {"model": "gemma-3-12b-it", "stance": "The crisis isn't overblown in the sense that it's insignificant; it exposed real methodological weaknesses."}, {"model": "evidence", "stance": "The crisis is not overblown: inflated fragile p-values, ~39% replication rate in OSC 2015, and documented QRPs confirm systemic problems. However, cognitive psychology's higher replicability (~50-80% in some assessments) vs. social psychology's lower rate means severity is subfield-dependent, not uniformly overblown or uniform."}]}
  - {"topic": "PSA network size and scope", "stances": [{"model": "glm-4.7-flash", "stance": "Psychological Science Accelerator has 207 labs across 44 countries."}, {"model": "evidence", "stance": "By 2022-2023, PSA reported 2,468 members in 73 countries; by 2024, 180+ collaborators in 60+ countries for a single project. The 207/44 figure is outdated and understates current scale."}]}

**unique_insights:**
  - {"model": "glm-4.7-flash", "insight": "Fragile p-values (.01–.05) as a concrete, trackable metric for assessing field-wide research quality over time—the drop from 32% to 26% nearly matches the expected rate under 80% power, providing an objective improvement signal beyond replication rates."}
  - {"model": "glm-4.7-flash", "insight": "Top universities paradoxically publish weaker statistical results, with ~2/3 of this association explained by institutional preference for laborious, expensive, subtle research topics that inherently produce weaker p-values—revealing tension between prestige and robustness."}
  - {"model": "glm-4.7-flash", "insight": "Applied research is emerging as a pathway to legitimacy, addressing concerns about generalizability of findings from artificial laboratory settings."}
  - {"model": "gemma-3-12b-it", "insight": "Replication crisis extends beyond individual failings to reflect deeper systemic problems in academic incentive structures—the crisis is as much about institutional design as about researcher behavior."}
  - {"model": "qwen3-8b", "insight": "Global disparities in adoption of open science practices—discussions focus on North American institutions while economic pressures to publish prolifically persist in many regions, limiting reform uptake."}

**blind_spots:**
  - The Nature Human Behaviour paper reporting 86% replication for preregistered studies was RETRACTED—no model mentions this, critically undermining a key evidence claim used to support preregistration effectiveness.
  - Mixed evidence on preregistration: a 2023 Behavior Research Methods study found preregistered studies did NOT show lower positive result rates or smaller effect sizes than non-preregistered studies, complicating the reform narrative.
  - The replication crisis is not unique to psychology—economics, biomedicine, cancer biology, and other fields face similar issues, yet no model adequately discusses this comparative context or what psychology can learn from other disciplines' reforms.
  - WEIRD bias persists even in reform infrastructure: the PSA is ~2/3 Western/educated/industrialized/rich/democratic countries, meaning reform-generalizability evidence itself may be culturally narrow.
  - Recent retraction of a prominent scientific integrity paper (Protzko et al.) due to issues with pre-analysis plans shows the crisis extends into reform efforts themselves—a metacrisis no model addresses.
  - Real-world harms from irreproducible findings: insufficient discussion of how failed replications in clinical, educational, or organizational psychology may have led to harmful policy or therapeutic decisions.
  - Statistical vs. conceptual replication distinction: models conflate different replication types, yet the field debates whether strict direct replication is even the right standard for theories involving contextual variables.
  - The role of commercial interests and industry funding in shaping which findings get replicated and which get buried, particularly in clinical and applied psychology.
  - Potential for open science reforms to paradoxically increase inequity—researchers at under-resourced institutions may be unable to meet new standards for sample sizes, preregistration, and data sharing, widening the gap between wealthy and poor institutions.
  - AI and large language models as both a potential solution (automated statistical checking, data analysis transparency) and a new risk (automated p-hacking, fabricated data) for research integrity.

**partial_coverage:**
  - {"models": ["qwen3-8b", "glm-4.7-flash"], "point": "Subfield-specific differences in recovery: clinical and developmental psychology lag behind cognitive and social psychology in reducing fragile p-values and increasing sample sizes, partly due to in-person recruitment constraints."}
  - {"models": ["gemma-3-12b-it"], "point": "HARKing (Hypothesizing After the Results are Known) specifically named as a distinct questionable research practice beyond p-hacking."}
  - {"models": ["glm-4.7-flash"], "point": "Statcheck automated tool used in peer review to detect statistical inconsistencies in reported results."}
  - {"models": ["glm-4.7-flash"], "point": "Paradox that top-ranked universities tend to publish weaker results, partly explained by preference for laborious, subtle research topics that inherently produce weaker p-values."}
  - {"models": ["gemma-3-12b-it"], "point": "Bayesian statistics as an alternative to null hypothesis significance testing, offering more nuanced data analysis."}
  - {"models": ["qwen3-8b"], "point": "Funding bodies now prioritize replicability in grant decisions."}
  - {"models": ["gemma-3-12b-it"], "point": "Contextual factors (cultural, situational) can make replication legitimately difficult even with sound methods, not just due to QRPs."}

### C6_echo
_контроль: эхо-камера_  
panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507 | cost=$0.0652 | 254.3s | ptok=29343 ctok=6390 | retries=0

**consensus:**
  - Psychology experienced a significant replication crisis in the 2010s, evidenced by large-scale replication projects like the Open Science Collaboration (2015) which found only 36% of replications yielded significant results and 39% were subjectively rated as successful, exposing widespread questionable research practices such as p-hacking and publication bias.
  - The field has responded with measurable improvements: the proportion of 'fragile' p-values (0.01 ≤ p < 0.05) in psychology articles has declined from 32% (2004–2011) to nearly 26% (2024), aligning with expectations under 80% statistical power.
  - Sample sizes have increased across subfields, with a notable surge in social psychology due to online recruitment platforms like Mechanical Turk and Prolific, contributing to improved statistical power.
  - There is evidence of shifting academic incentives: articles with stronger results (fewer fragile p-values) are more likely to be published in high-impact journals and receive more citations, indicating a growing alignment between methodological rigor and academic rewards.
  - Researchers at elite institutions tend to publish studies with weaker statistical evidence, not due to lower standards but because they focus on labor-intensive, subtle, and expensive research topics (e.g., clinical, biological, developmental) that are inherently harder to power adequately.

**contradictions:**
  - {"topic": "Status of the replication crisis", "stances": [{"model": "Panel A", "stance": "The crisis has evolved into a 'credibility revolution' or 'renaissance,' marking a transformative improvement and should not be seen as a failure but as a catalyst for positive structural, procedural, and community-driven change."}, {"model": "Panel C", "stance": "It is premature to declare the crisis over; recovery is ongoing and requires continuous metascientific monitoring and evidence-based self-correction to avoid complacency."}]}
  - {"topic": "Effectiveness of reforms", "stances": [{"model": "Source 1 (Nature Communications Psychology)", "stance": "Reforms such as preregistration, Registered Reports, and Big Team Science are effective and represent a systemic transformation toward more transparent and rigorous science."}, {"model": "blind_spots", "stance": "Evidence shows mixed effectiveness: while open data practices have improved, preregistration adoption remains low (e.g., only 3% of registered studies are publicly shared as of 2024), and many open-science practices are slow to be adopted."}]}
  - {"topic": "Robustness and academic prestige", "stances": [{"model": "Source 2 (Bogdan, 2025)", "stance": "Robust research is increasingly rewarded in journals and citations, suggesting improved incentives for rigor."}, {"model": "Source 2 (Bogdan, 2025)", "stance": "Despite this, top-ranked universities still publish studies with more fragile p-values, and the gap between high- and low-ranking institutions has not meaningfully narrowed since the crisis began, indicating a misalignment between prestige and robustness."}]}

**unique_insights:**
  - {"model": "Panel A", "insight": "Meaningful reform requires alignment across structural, procedural, and community levels; focusing on one level (e.g., individual preregistration) without changing structural incentives (e.g., hiring, promotion) will lead to failure."}
  - {"model": "Panel B", "insight": "Language analysis of research articles shows that two-thirds of the association between elite institutions and fragile p-values can be explained by topic focus (e.g., clinical, neuroimaging), not lower methodological standards, due to the high cost and low scalability of such research."}
  - {"model": "Panel C", "insight": "The field must adopt a continuous 'metascientific' monitoring system—such as systematic tracking of replication rates and researcher surveys—to ensure reforms are evidence-based and self-correcting, rather than assuming progress based on optimism."}

**blind_spots:**
  - No model addresses the limited adoption of preregistration in practice; recent data (Ensinck & Lakens, 2025) show that only 3% of registered studies are publicly shared, undermining the assumed effectiveness of this reform.
  - There is insufficient discussion of how Bayesian methods and alternative statistical frameworks (e.g., estimation, equivalence testing) are being integrated to address the limitations of null hypothesis significance testing, despite growing advocacy for such shifts.
  - None of the models consider the ethical or epistemic implications of relying on online participant pools (e.g., Mechanical Turk, Prolific), which, while increasing sample sizes, may introduce new validity concerns such as bot traffic, inattentive respondents, and reduced generalizability.
  - The impact of the replication crisis on qualitative and applied psychology (e.g., clinical, counseling) is largely ignored, despite these areas facing distinct methodological challenges and different replication norms.
  - There is no meaningful engagement with the role of funding structures and global inequities (e.g., access to online platforms, open-access publishing fees) that may perpetuate methodological disparities between institutions in the Global North and South.

**partial_coverage:**
  - {"models": ["Panel A"], "point": "Reforms span three interconnected levels: structural (e.g., DORA, curriculum changes), procedural (e.g., preregistration, multiverse analysis), and community-driven (e.g., Big Team Science, adversarial collaborations), and all three must align for meaningful change."}
  - {"models": ["Panel B"], "point": "The decline in fragile p-values correlates with increased sample sizes, especially in social psychology due to online platforms, while fields like clinical psychology show slower gains due to cost and logistical constraints."}
  - {"models": ["Panel C"], "point": "The field needs a sustained 'metascientific' research agenda to empirically track replication rates, publication of null results, and researcher behavior to ensure reforms are effective and not superficial."}
  - {"models": ["Source 3 (Annual Review of Psychology)"], "point": "Replication should be reframed as a core scientific practice for self-correction rather than a personal attack, and adversarial collaborations can enhance rigor by minimizing researcher bias."}

### C3_cn_small
_всё мелкое_  
panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b | cost=$0.0788 | 661.3s | ptok=40415 ctok=12290 | retries=0

**consensus:**
  - The replication crisis caused significant damage to psychology's credibility, particularly in social/personality psychology.
  - The field is in recovery ('Credibility Revolution') through reforms like preregistration, open science, and larger sample sizes.
  - Structural changes (E.g., registered reports) have increased replication rates (85-89% for robustly designed studies).
  - Public trust remains damaged, but reforms are mandated by many journals and funders.

**contradictions:**
  - {"topic": "Severity of the crisis", "stances": [{"model": "qwen/qwen3.6-27b", "stance": "Crisis was significant but not overblown"}, {"model": "z-ai/glm-4.7-flash", "stance": "Some argue the crisis is overstated due to flawed replication methods"}, {"model": "evidence", "stance": "Tyner et al. (2026) found only 42% observed replication success despite pre-registration adoption"}]}
  - {"topic": "Impact of reforms", "stances": [{"model": "qwen/qwen3.6-27b", "stance": "Preregistration+large samples deliver 86-90% replication rates"}, {"model": "z-ai/glm-4.7-flash", "stance": "Top journals still publish 'fragile' p-values despite transparency mandates"}, {"model": "qwen/qwen3-32b", "stance": "ERR estimates (68%) exceed observed replication rates (42%) due to effect size shrinkage"}]}

**unique_insights:**
  - {"model": "z-ai/glm-4.7-flash", "insight": "Combining preregistration with N>1500 participants achieves nearly 90% replication rates"}
  - {"model": "qwen/qwen3-32b", "insight": "False discovery rates remain low (6% at alpha=.05) despite replication failures primarily due to effect size shrinkage"}
  - {"model": "qwen/qwen3-32b", "insight": "Z-curve analysis reveals 88% replication success for well-powered studies when methodological fidelity is maintained"}

**blind_spots:**
  - Long-term economic consequences for applied psychology industries
  - Impact of institutional prestige on publishing norms
  - Effectiveness of graduate training reforms in teaching modern methods
  - Policy incentives for replication vs. exploratory research
  - Mechanisms driving inconsistent adoption of reforms in lower-tier journals

**partial_coverage:**
  - {"models": ["qwen/qwen3.6-27b"], "point": "Clinical/developmental psychology lag in sample size improvements"}
  - {"models": ["z-ai/glm-4.7-flash"], "point": "Economic impacts on industries using psychology (e.g., marketing, healthcare)"}
  - {"models": ["qwen/qwen3-32b"], "point": "Z-curve analysis shows 88% replication success for well-powered studies when methodological fidelity is maintained"}


---
## BASELINE (одиночная модель, без fusion)

### B_cn  (model=deepseek-v4-pro | cost=$0.0053 | 38.7s)
The replication crisis has undeniably damaged psychology’s credibility, but the field’s response has turned that damage into a catalyst for meaningful reform. The crisis is not overblown—it exposed real, systemic weaknesses—but psychology is recovering, albeit unevenly across subfields. Here’s a breakdown of the damage, the trajectory, the reforms that have worked, and what it all means for researchers and policymakers.

### 1. How seriously damaged is psychology?
**Significant but not fatal.** The crisis struck at the heart of published findings, particularly in social, personality, and developmental psychology. The landmark 2015 Reproducibility Project: Psychology attempted to replicate 100 studies and found that only 36–47% produced statistically significant results in the same direction, with effect sizes typically half the original. Subsequent large-scale replication efforts (Many Labs, Social Sciences Replication Project) confirmed that while some areas (e.g., cognitive psychology) fare better, others (social priming, ego depletion, power posing) have replication rates below 30%.

The damage is real:
- **Public trust:** Media headlines framed psychology as a “science of shaky results,” eroding confidence among the public, students, and policymakers.
- **Internal credibility:** Many classic textbook findings are now considered unreliable or context-dependent. Entire research programs collapsed.
- **Policy impact:** Interventions based on non-replicable findings (e.g., certain nudges, implicit bias training) may have wasted resources or been ineffective.

However, the crisis also demonstrated that psychology is capable of self-correction—a hallmark of a maturing science. The damage is comparable to a severe but treatable injury: painful, but it forced necessary surgery.

### 2. Is the field recovering, getting worse, or is the crisis overblown?
**Recovering, with caveats.** The field is not getting worse; it is actively improving, though progress is slower in some corners. The crisis was not overblown—the original replication rates were genuinely low, and questionable research practices (p-hacking, HARKing, small samples, publication bias) were widespread. But the narrative that “most psychology is false” is an oversimplification. Many robust findings (e.g., Stroop effect, anchoring, basic memory phenomena) replicate well. The crisis primarily exposed a culture that rewarded novelty over rigor.

Evidence of recovery:
- **Replication rates are rising** in journals that mandate open practices. A 2023 meta-analysis of replication studies found that replicability has improved over time, especially in subfields that embraced reform.
- **Statistical power** has increased dramatically. The average sample size in social psychology roughly tripled between 2010 and 2020.
- **Questionable research practices** are declining. Surveys show that p-hacking and selective reporting are less common, though far from eliminated.
- **Incentives are shifting.** Hiring, promotion, and funding criteria increasingly value open science contributions (data sharing, preregistration, replication) alongside novel findings.

The crisis is not overblown because it revealed a systemic disease, not just a few bad apples. But the doomsday narrative that psychology is “broken beyond repair” is outdated. The field is in a period of credible rebuilding.

### 3. What reforms have actually worked?
Several evidence-based reforms have demonstrably improved research quality:

- **Preregistration and Registered Reports:** Preregistering hypotheses and analysis plans reduces p-hacking and HARKing. Registered Reports—where journals accept studies based on the question and methodology before results are known—dramatically increase the publication of null results and reduce publication bias. A 2022 study found that Registered Reports in psychology have a replication rate of ~80%, compared to ~40% for standard articles.
- **Open data and materials:** Sharing data, code, and stimuli allows independent verification and reanalysis. Journals with mandatory open data policies show higher replication rates and more error detection.
- **Large-scale, multi-lab collaborations:** Projects like Many Labs and the Psychological Science Accelerator use massive, diverse samples and standardized protocols, yielding more generalizable and replicable findings. They also normalize team science.
- **Statistical reforms:** Moving away from a binary “p < .05” threshold toward effect sizes, confidence intervals, Bayesian methods, and meta-analytic thinking has reduced overconfidence in single studies. Journals now often require power analyses and discourage small, underpowered experiments.
- **Badges and recognition:** The “open science badges” (e.g., for preregistration, open data) from the Center for Open Science have been adopted by dozens of journals and have been shown to increase data sharing and replication rates.
- **Replication as a valued activity:** Dedicated replication

### B_west  (model=gpt-5.2 | cost=$0.0211 | 31.8s)
Psychology isn’t “ruined,” but the replication crisis revealed that **a nontrivial share of published claims—especially surprising, small effects from small studies—were overstated or unreliable**. The field has **meaningfully improved** in methods and transparency over the last decade, but **the underlying incentive problems (publish-or-perish, novelty bias) are not fully fixed**, so it’s better to think of psychology as **in a long recovery and renovation**, not “post‑crisis.”

## 1) How seriously damaged is psychology?

### What the crisis actually established
Across large, systematic efforts (e.g., the Open Science Collaboration 2015; ManyLabs; Registered Replication Reports), several robust patterns emerged:

- **Replication rates were lower than the literature implied**, depending on how you define “replicates” (same direction? statistically significant? similar effect size?).
- **Effect sizes in original papers were often inflated** (winner’s curse + publication bias + low power).
- **Questionable research practices (QRPs)**—optional stopping, selective reporting, trying multiple analyses/variables—can easily produce publishable p-values without fraud.
- **Publication bias** (nulls not published) made meta-analytic summaries too optimistic unless adjusted.

### How uneven the damage is
Psychology is not one thing. Reliability varies a lot by topic and method:

- **More vulnerable areas** tend to be those with **small, context-sensitive effects**, heavy researcher degrees of freedom, and historically low-powered designs (some parts of social/personality, “hot hand” findings, some priming literatures, etc.).
- **Less vulnerable areas** include many **basic cognitive/perceptual phenomena** with large effects and tight experimental control, and parts of clinical/health psych that use larger samples/registered trials (though they have their own issues like measurement and generalizability).

### Bottom line on “damage”
- **Scientific credibility took a hit**: a single new paper is now (appropriately) treated as weak evidence.
- **The knowledge base wasn’t wiped out**: many findings replicate, and many failures were informative corrections (effects smaller, more conditional, or measure-dependent rather than nonexistent).
- The biggest “damage” is that **older literatures built on underpowered, flexible analyses are less trustworthy** until re-evaluated with modern methods.

## 2) Is the field recovering, getting worse, or is it overblown?

### Recovery: yes, on methods and norms
Compared with ~2011–2015, there is strong evidence of improvement in:
- **Preregistration** adoption
- **Open materials/data/code** norms (not universal, but much higher)
- **Multi-lab collaborations** and larger samples (e.g., Psychological Science Accelerator)
- **Registered Reports** growth (important because they change incentives)

Meta-research also suggests **average statistical power has improved** in some journals/areas, and **effect sizes in newer work are often smaller**, consistent with reduced inflation (a sign of healthier calibration, not failure).

### Not “overblown,” but sometimes oversimplified
It’s not accurate to say “most of psychology is false,” but it *is* accurate that:
- **The pre-crisis literature overrepresented clean, strong, general effects**.
- **Many results were not as stable as advertised**, especially those discovered via flexible analyses and published as if confirmatory.

### Not “over”
The crisis is best understood as a **per
