# fac-10 — Dengue virus serotypes
**Block:** factual  |  **difficulty:** hard

**Prompt:**
How many confirmed serotypes does the dengue virus have? List them by name. Why does secondary infection with a *different* serotype cause more severe disease than the first infection?

**Expected answer (эталон):**
4 confirmed serotypes: DENV-1, DENV-2, DENV-3, DENV-4. Secondary infection is more severe due to antibody-dependent enhancement (ADE): antibodies from the first infection bind but fail to neutralize the new serotype, instead facilitating viral entry into immune cells (Fc receptor-mediated), amplifying viral load.

---
## FUSION-конфиги (judge-анализ; responses вынесены в resp_*.md)

### C1_west_closed
_западный закрытый фронтир_  
panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2 | cost=$0.1201 | 368.1s | ptok=16122 ctok=3138 | retries=1

**consensus:**
  - Dengue virus has 4 confirmed serotypes: DENV-1, DENV-2, DENV-3, DENV-4 (supported by current public-health references such as CDC and PAHO).
  - Secondary infection with a different (heterologous) serotype is associated with higher risk of severe dengue, largely explained by antibody-dependent enhancement (ADE): pre-existing cross-reactive but insufficiently neutralizing antibodies can increase infection of Fc-receptor–bearing immune cells, raising viremia and inflammatory/vascular-leak pathology.

**contradictions:**
  - {"topic": "Whether heterologous secondary infection is inherently/typically more severe vs a probabilistic risk factor (severe dengue can also occur in primary infection)", "stances": [{"model": "openai/gpt-5.2", "stance": "Frames as a main reason a second infection with a different serotype can be more severe (risk-oriented language, but still implies a general mechanism explanation)."}, {"model": "google/gemini-3.1-pro-preview", "stance": "Says a secondary infection with a different serotype typically causes more severe disease (stronger implication of typicality)."}, {"model": "x-ai/grok-4.3", "stance": "Explicitly notes risk is higher on second infection but severe dengue can occur on first or later infections too."}, {"model": "evidence", "stance": "Epidemiology and clinical guidance describe heterologous secondary infection as an important risk factor, not a necessary or sufficient cause; severe dengue also occurs in some primary infections (and in infants with waning maternal antibodies)."}]}

**unique_insights:**
  - {"model": "x-ai/grok-4.3", "insight": "Makes the important nuance explicit that although heterologous secondary infection is a major risk factor, severe dengue is not exclusive to second infections (it can occur in primary or later infections depending on context)."}

**blind_spots:**
  - No response clearly distinguishes 'confirmed serotypes' (DENV-1–4) from ongoing debates about what would count as formal recognition (e.g., ICTV taxonomy vs antigenic/neutralization-defined serotypes) and why DENV-5 remains 'putative' in many modern summaries.
  - None discuss the antibody-titer/time-interval dependence of ADE (cross-protection early after first infection vs higher risk later as neutralizing titers wane), which is central to why secondary infections are not uniformly severe.
  - None mention severe dengue in infants driven by waning maternal anti-DENV antibodies (a classic ADE context) as supporting evidence for the mechanism.
  - No response covers NS1’s role and endothelial glycocalyx/complement interactions (and anti-NS1 effects) as additional, evidence-backed contributors to vascular leak alongside ADE.
  - No response addresses viral and host heterogeneity that modulates severity (viral genotype/strain virulence, prior infection sequence, host genetics/HLA, age, pregnancy, comorbidities), which are important for a truth-seeking explanation beyond a single mechanism.

**partial_coverage:**
  - {"models": ["openai/gpt-5.2", "google/gemini-3.1-pro-preview"], "point": "Mentions cross-reactive T-cell phenomena ('original antigenic sin') as an additional contributor to severity beyond ADE."}
  - {"models": ["openai/gpt-5.2", "google/gemini-3.1-pro-preview"], "point": "Specifies Fcγ/Fc receptors on monocytes/macrophages/dendritic cells as the cellular route exploited in ADE (mechanistic detail not consistently present in all responses)."}
  - {"models": ["google/gemini-3.1-pro-preview", "x-ai/grok-4.3"], "point": "States lifelong immunity is serotype-specific with only short-lived cross-protection to other serotypes after primary infection."}
  - {"models": ["openai/gpt-5.2", "google/gemini-3.1-pro-preview"], "point": "Adds the caveat that 'DENV-5' has been proposed in the literature but is not broadly accepted as a confirmed, routinely circulating human serotype."}

### C2_cn_open
_открытый китайский фронтир (умн+умн)_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507 | cost=$0.0787 | 133.6s | ptok=17246 ctok=1165 | retries=0

**consensus:**
  All retrieved sources confirm that the dengue virus has four confirmed serotypes: DENV-1, DENV-2, DENV-3, and DENV-4 (also referred to as dengue virus 1, 2, 3, and 4). They agree that infection with one serotype confers lasting immunity to that specific serotype but not to the others, and that secondary infection with a different serotype carries a greater risk of severe disease (such as dengue hemorrhagic fever or severe dengue).

**contradictions:**
  There are no direct contradictions. A minor nuance exists between the NCBI Bookshelf, which states infection confers 'lifelong immunity to that serotype but not to others,' and the CDC Yellow Book, which states it confers 'long-term immunity to that virus but only short-lived protection against the other three dengue viruses.' This represents a difference in descriptive wording rather than a factual contradiction.

**unique_insights:**
  The Merck Manual explicitly identifies the mechanism causing worse outcomes upon secondary infection with a different serotype as 'antibody-dependent enhancement (ADE) of infection,' explaining that non-neutralizing antibodies from a previous infection with one serotype enhance infection upon exposure to a different serotype. Additionally, the CDC Yellow Book and Merck Manual highlight that the dengue vaccine (Dengvaxia/CYD-TDV) can mimic this risk, increasing the chance of severe disease in individuals without prior dengue infection who are subsequently exposed, which parallels the ADE phenomenon.

**blind_spots:**
  The retrieved snippets do not provide detailed molecular or cellular-level pathophysiology of antibody-dependent enhancement (e.g., specific Fc-gamma receptor interactions, complement activation pathways, or the precise cytokine cascade). They also do not mention or rule out the existence of any other potential or putative serotypes beyond the four confirmed ones.

**partial_coverage:**
  While all sources cover the number of serotypes and the increased severity of secondary infection, only the Merck Manual explicitly names antibody-dependent enhancement as the underlying mechanism. The NCBI Bookshelf and CDC Yellow Book describe the clinical association without naming the specific immunological mechanism in the provided excerpts. The CDC consumer page provides only basic naming of the four types and does not address the mechanism of severe secondary disease.

### C5_smartpanel_dumbjudge
_умная панель + глупый судья_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b | cost=$0.0715 | 469.1s | ptok=19078 ctok=3789 | retries=0

**consensus:**
  - There are four confirmed serotypes: DENV-1, DENV-2, DENV-3, and DENV-4.
  - Secondary infection with a different serotype causes more severe disease due to Antibody-Dependent Enhancement (ADE).

**contradictions:**
  - {"topic": "DENV-5 status", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "Proposed but not confirmed as a sustained human serotype"}, {"model": "evidence", "stance": "No confirmed evidence of sustained human transmission for DENV-5"}]}

**unique_insights:**
  - {"model": "moonshotai/kimi-k2.6", "insight": "CYD-TDV vaccine increases severe disease risk in seronegative recipients"}
  - {"model": "z-ai/glm-5.1", "insight": "ADE suppresses type I interferon signaling and promotes IL-10 production"}

**blind_spots:**
  - Role of genetic polymorphisms in ADE susceptibility
  - Impact of climate change on serotype prevalence
  - Mechanistic differences between primary and secondary infections in children vs adults

**partial_coverage:**
  - {"models": ["moonshotai/kimi-k2.6"], "point": "CYD-TDV vaccine approval and risks for seronegative recipients"}
  - {"models": ["moonshotai/kimi-k2.6"], "point": "Microvascular permeability escalates as viral titers decrease in severe dengue"}

### C5inv_dumbpanel_smartjudge
_глупая панель + умный судья (qwen-2.5-7b → gemma-3-12b-it)_  
panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1 | cost=$0.0815 | 301.8s | ptok=19126 ctok=3864 | retries=0

**consensus:**
  - The dengue virus has four confirmed serotypes: DENV-1, DENV-2, DENV-3, and DENV-4.
  - Secondary infection with a different serotype causes more severe disease primarily via Antibody-Dependent Enhancement (ADE), where pre-existing non-neutralizing or sub-neutralizing antibodies bind the new serotype, facilitating viral entry into immune cells (monocytes/macrophages) via Fcγ receptors, increasing viral replication.
  - ADE triggers an exaggerated or dysregulated immune response, contributing to vascular leakage and severe dengue manifestations.
  - The risk and severity of ADE vary depending on the specific combination of serotypes involved in the primary and secondary infections.

**contradictions:**
  - {"topic": "Number of confirmed serotypes", "stances": [{"model": "qwen/qwen3-8b", "stance": "Strictly four confirmed serotypes (DENV-1 to DENV-4)."}, {"model": "google/gemma-3-12b-it", "stance": "Four confirmed serotypes, but acknowledges the 'possibility of other, less common or unconfirmed serotypes'."}, {"model": "evidence", "stance": "A fifth serotype (DENV-5) was proposed in 2013 from a sylvatic cycle isolate in Malaysia, but it remains unconfirmed/unapproved by ICTV and has not caused widespread human outbreaks; four remains the accepted standard."}]}
  - {"topic": "Mechanisms of cytokine dysregulation in ADE", "stances": [{"model": "qwen/qwen3-8b", "stance": "ADE leads to a 'cytokine storm' with extreme immune response, implying predominantly overactive pro-inflammatory cytokines."}, {"model": "z-ai/glm-4.7-flash", "stance": "ADE triggers high levels of pro-inflammatory cytokines AND suppression of anti-inflammatory cytokines (or vice versa: elevated IL-10, an anti-inflammatory cytokine)."}, {"model": "evidence", "stance": "Intrinsic ADE involves complex immunomodulation: suppression of pro-inflammatory cytokines/Type I IFNs within infected monocytes, coupled with increased production of IL-10 and IL-6, which inhibit NO synthesis and Type I IFN pathways, promoting viral replication."}]}

**unique_insights:**
  - {"model": "z-ai/glm-4.7-flash", "insight": "Intrinsic ADE mechanisms involve the virus-antibody complex using LILRB1 and SHP-1 to downregulate phagosome acidification and escape lysosomal degradation, allowing viral replication even after cell entry."}
  - {"model": "google/gemma-3-12b-it", "insight": "Molecular mimicry, where regions of different serotypes share structural similarities, could contribute to the severity of secondary infections beyond ADE."}

**blind_spots:**
  - T-cell cross-reactivity and original antigenic sin: No model adequately addressed the significant role of cross-reactive CD8+ T cells, which have altered cytokine profiles (altered peptide ligand effect) and lower avidity for the new serotype, contributing to delayed viral clearance and immunopathology.
  - The DENV-5 serotype: While one model vaguely alluded to unconfirmed serotypes, no model explicitly discussed the proposed fifth serotype (DENV-5), isolated in 2007/2013 from a sylvatic cycle, and its implications for current tetravalent vaccines.
  - Infant severe dengue: Severe dengue can also occur in infants experiencing primary infection (6-12 months) due to waning maternal antibodies entering the ADE window, which contradicts the models' implicit framing that severe disease strictly requires prior natural infection.
  - Innate immune suppression during intrinsic ADE: The suppression of Type I interferon and nitric oxide radical pathways within infected monocytes, which directly facilitates viral replication, was largely missed or oversimplified as just a 'cytokine storm'.

**partial_coverage:**
  - {"models": ["z-ai/glm-4.7-flash"], "point": "Only about 2-4% of secondary heterotypic dengue infections actually progress to severe disease (DHF/DSS)."}
  - {"models": ["z-ai/glm-4.7-flash"], "point": "ADE risk is highest when antibody levels are in a specific 'enhancement window' (sub-neutralizing concentrations)."}
  - {"models": ["z-ai/glm-4.7-flash"], "point": "Severity is associated with elevated levels of afucosylated IgG1 Fc glycoforms that bind more strongly to activating Fcγ receptors."}
  - {"models": ["z-ai/glm-4.7-flash"], "point": "Mention of intrinsic ADE mechanisms beyond viral entry, such as suppression of phagosome acidification (via LILRB1 and SHP-1)."}
  - {"models": ["google/gemma-3-12b-it"], "point": "Molecular mimicry between serotypes may play a role in secondary infection severity."}

### C6_echo
_контроль: эхо-камера_  
panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507 | cost=$0.1004 | 853.5s | ptok=139582 ctok=20188 | retries=0

**consensus:**
  - The dengue virus has four confirmed serotypes: DENV-1, DENV-2, DENV-3, and DENV-4.
  - Secondary infection with a different serotype increases the risk of severe dengue, though severe disease can also occur in primary infections.
  - Antibody-dependent enhancement (ADE) is the primary mechanism explaining increased severity in secondary heterologous infections, where non-neutralizing antibodies from the primary infection facilitate increased viral entry into Fc receptor-bearing cells, leading to higher viremia and immunopathology.

**contradictions:**
  - {"topic": "ADE as universally accepted mechanism", "stances": [{"model": "qwen/qwen3-235b-a22b-2507", "stance": "ADE is consistently named and described as the key mechanism for increased severity in secondary infection."}, {"model": "evidence", "stance": "While ADE is dominant in textbooks, recent studies highlight its limitations: some patients with severe primary dengue exhibit high antibody titers suggesting prior unrecognized infection, and infant models show ADE occurs only within a narrow window of waning maternal antibodies. Additionally, T-cell immunopathology and viral genetic factors contribute significantly, implying ADE is necessary but not sufficient alone."}]}

**unique_insights:**
  - {"model": "qwen/qwen3-235b-a22b-2507", "insight": "The PLOS Neglected Tropical Diseases study in Nicaragua demonstrates that DENV-3 causes significant severity in both primary and secondary infections, challenging the assumption that severe disease is predominantly secondary, and highlighting serotype-specific pathogenic differences."}

**blind_spots:**
  - None of the models discuss the role of viral genetic diversity (intra-serotype genotypes) in modulating virulence and disease outcomes.
  - No mention of the impact of pre-existing flavivirus immunity (e.g., Zika, yellow fever) on dengue severity via original antigenic sin or cross-protection.
  - Limited discussion on sex-based differences in immune response and clinical outcomes in dengue.
  - The socioeconomic and healthcare system burdens of dengue in endemic countries, including costs of hospitalization and vector control, are overlooked.
  - No model references the latest dengue vaccine developments post-2023, such as the rollout of Qdenga in Brazil or phase 3 results for TV003.

**partial_coverage:**
  - {"models": ["qwen/qwen3-235b-a22b-2507"], "point": "DENV-2 and DENV-4 are more frequently associated with secondary infections and dengue shock syndrome (DSS), while DENV-3 is strongly linked to dengue hemorrhagic fever (DHF), with regional variation in severity patterns."}
  - {"models": ["qwen/qwen3-235b-a22b-2507"], "point": "T-cell responses in secondary infection, particularly cross-reactive memory T cells producing excessive cytokines and ineffective viral control, contribute to immunopathology and cytokine storms."}
  - {"models": ["qwen/qwen3-235b-a22b-2507"], "point": "HMGB1 and NLRP3 inflammasome pathways are involved in initiating inflammatory responses, vascular permeability, and organ damage during severe dengue."}

### C3_cn_small
_всё мелкое_  
panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b | cost=$0.0376 | 217.4s | ptok=12678 ctok=2178 | retries=0

**consensus:**
  - There are four confirmed dengue virus serotypes (DENV-1, DENV-2, DENV-3, DENV-4).
  - Secondary infection with a different serotype causes more severe disease via antibody-dependent enhancement (ADE).

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "z-ai/glm-4.7-flash", "insight": "Quantified ADE progression to severe disease (<5%) and explicitly linked cytokine suppression (IL-12, IFN-γ) to immune dysfunction."}
  - {"model": "qwen/qwen3-32b", "insight": "Highlighted 'original antigenic sin' as a factor in antibody ineffectiveness during secondary infections."}

**blind_spots:**
  - Role of T-cell-mediated immune responses in secondary dengue pathogenesis (mechanisms like CD4+ T-cell cross-reactivity and cytokine imbalance).
  - Population-level immune dynamics (e.g., seroprevalence trends and age-specific risk patterns).

**partial_coverage:**
  - {"models": ["z-ai/glm-4.7-flash"], "point": "Detailed explanation of ADE mechanisms including Fcγ Receptor-Mediated Entry, cytokine storm dynamics, and Th2-skewed immune response."}
  - {"models": ["qwen/qwen3-32b"], "point": "Mention of 'serotype immunity gaps' and DENV-3 re-emergence after 15 years in Brazil."}


---
## BASELINE (одиночная модель, без fusion)

### B_cn  (model=deepseek-v4-pro | cost=$0.0025 | 17.8s)
The dengue virus has **four confirmed serotypes**, which are:

- **DENV-1**
- **DENV-2**
- **DENV-3**
- **DENV-4**

*(Note: A purported fifth serotype, DENV-5, was reported in a single sylvatic strain from Malaysia in 2013, but it does not circulate in humans and is not considered a confirmed serotype in the context of human disease.)*

---

### Why secondary infection with a *different* serotype causes more severe disease

The increased severity of a second dengue infection with a different serotype is primarily explained by **antibody-dependent enhancement (ADE)**. Here’s how it works:

1. **Primary infection:** The immune system produces neutralizing antibodies that are highly specific to the infecting serotype and provide lifelong immunity to *that* serotype. However, they also generate cross-reactive, non-neutralizing antibodies against the other three serotypes.

2. **Secondary heterotypic infection:** When a person is later infected with a different serotype, the pre-existing cross-reactive antibodies bind to the new virus but **cannot neutralize it**. Instead, these antibody–virus complexes are efficiently taken up by cells bearing Fcγ receptors (especially monocytes, macrophages, and dendritic cells) via Fc receptor-mediated endocytosis. This actually *facilitates* viral entry and replication in exactly the cells that are the primary targets of dengue, leading to a higher viral load.

3. **Immune hyperactivation:** The increased viral replication triggers massive immune activation, a “cytokine storm” (including TNF-α, IL-6, IL-10, etc.), and complement activation. This causes the hallmark of severe dengue: **vascular endothelial dysfunction, plasma leakage, bleeding, and potentially shock** (dengue hemorrhagic fever/dengue shock syndrome).

Additionally, a phenomenon called **original antigenic sin** in the T-cell response contributes to the severity: memory T cells generated during the primary infection are reactivated but have a suboptimal, skewed response against the new serotype, leading to delayed viral clearance and exaggerated inflammatory damage.

### B_west  (model=gpt-5.2 | cost=$0.0075 | 11.4s)
### Confirmed dengue virus serotypes (by name)
There are **4 confirmed serotypes** of dengue virus:

1. **DENV-1** (Dengue virus serotype 1)  
2. **DENV-2** (Dengue virus serotype 2)  
3. **DENV-3** (Dengue virus serotype 3)  
4. **DENV-4** (Dengue virus serotype 4)

*(Occasionally a putative “DENV-5” is mentioned in the literature, but the widely accepted, confirmed human dengue serotypes remain 1–4.)*

---

### Why a secondary infection with a different serotype can be more severe
The main reason is **antibody-dependent enhancement (ADE)**:

- After a first dengue infection, your immune system makes antibodies that **strongly neutralize that same serotype**.
- If you later get infected with a **different serotype**, some of those existing antibodies may **bind** the new serotype but **not neutralize** it effectively (they’re “cross-reactive, sub-neutralizing”).
- These antibody–virus complexes can then attach to **Fcγ receptors** on immune cells (especially **monocytes/macrophages and dendritic cells**), which **promotes viral entry and replication** inside those cells.
- This can lead to **higher viral load (viremia)** and a more intense immune activation, increasing the risk of **severe dengue** (e.g., plasma leakage, hemorrhage, shock).

Additional contributing immunology often cited:
- **Cross-reactive T-cell responses** (“original antigenic sin”) may be skewed toward the first serotype and can produce a strong but less effective response, amplifying inflammatory cytokines.
- The resulting **cytokine and complement activation** contributes to **endothelial dysfunction and vascular permeability**, key features of severe dengue.

So, the first infection tends to “prime” immunity; a second infection with a different serotype can, paradoxically, use that partial immunity to **enhance infection and inflammation**, making disease more severe.
