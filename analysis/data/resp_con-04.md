# con-04 — Rust vs C++ in systems programming by 2035  (raw panel responses + judge-синтез)
**Prompt:** Will Rust significantly displace C++ as the primary language for systems programming over the next 10 years? Analyze adoption trends, key structural barriers, who benefits most from switching, and what the realistic landscape looks like in 2035.

> ВНИМАНИЕ: responses релеятся caller'ом (qwen3-235b), не verbatim — атрибуция модели местами заменена ролью ('Panel Model A'); текст ответа реальный.


======================================================================
## C1_west_closed  (panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - Rust adoption is increasing, especially where memory safety is a first-order requirement; this is consistent with broad surveys showing Rust remains much smaller than C/C++ in overall usage but highly desired/admired (e.g., Stack Overflow 2024 reports C++ ~20–23% vs Rust ~11–13% of respondents using each).
  - C++ is very unlikely to be fully displaced by 2035 because of the scale and persistence of existing C++ (and C) codebases, plus ecosystem/tooling inertia that makes wholesale rewrites economically unrealistic; current industry and survey data shows C/C++ remain among the most-used languages.
  - The most realistic path through 2035 is coexistence with incremental adoption: Rust is often introduced at subsystem boundaries (FFI, new components) rather than via full rewrites, and public indicators (e.g., Rust being added experimentally to the Linux kernel) fit that incremental pattern.
**contradictions:** 
  - {"topic": "Will Rust become the default for new systems programming projects (vs just a growing niche) by ~2035?", "stances": [{"model": "google/gemini-3.1-pro-preview", "stance": "Suggests Rust is becoming the default for many greenfield systems domains (cloud/infra/OS components), implying strong dominance in new work even if legacy C++ persists."}, {"model": "x-ai/grok-4.3", "stance": "Claims Rust is 'already becoming the default choice for new systems programming projects' and will keep accelerating in new safety-critical work."}, {"model": "evidence", "stance": "Available broad metrics support growth but not 'default': overall-usage surveys still show C/C++ used by substantially more developers than Rust (e.g., Stack Overflow 2024: C++ ~20–23% vs Rust ~11–13%), and these surveys do not directly evidence Rust as the dominant default for new systems projects."}]}
  - {"topic": "Strength/speed of Rust adoption (rapid acceleration vs modest growth/possible plateau depending on metric)", "stances": [{"model": "google/gemini-3.1-pro-preview", "stance": "Frames Rust adoption as rapid and strongly trending upward across key systems areas."}, {"model": "x-ai/grok-4.3", "stance": "Describes accelerating adoption supported by 2024–2025 surveys and government/industry pushes."}, {"model": "evidence", "stance": "Different datasets paint a mixed picture: Stack Overflow 2024 reports Rust usage slightly down year-over-year (12.6% vs 13.5% prior year), while other indices (e.g., TIOBE) show Rust rising in rank but still at low single-digit share; 'rapid acceleration' is not uniformly supported."}]}
  - {"topic": "Quantitative claim that Rust has ~52% share in some 'new systems programming projects' metric", "stances": [{"model": "google/gemini-3.1-pro-preview", "stance": "Includes/echoes a claim that Rust shows '52% market share in some metrics for new systems programming projects.'"}, {"model": "x-ai/grok-4.3", "stance": "Does not make this specific quantitative claim."}, {"model": "evidence", "stance": "No standard, widely accepted industry metric supports a general '52% share' for Rust in new systems projects; broad usage surveys place Rust far below C/C++ in total usage, so the claim is at best context-specific and, as stated, epistemically under-justified."}]}
  - {"topic": "How decisive certification/standardization barriers are for Rust in regulated industries by 2035", "stances": [{"model": "google/gemini-3.1-pro-preview", "stance": "Treats lack of ISO standardization/multi-implementation maturity as a major long-run barrier analogous to earlier C++ maturity stages."}, {"model": "x-ai/grok-4.3", "stance": "Emphasizes certification barriers as a key reason C++ remains dominant in avionics/medical/automotive, implying slow Rust penetration."}, {"model": "evidence", "stance": "The barrier is real but not static: Ferrocene (a Rust toolchain) was announced as ISO 26262 / IEC 61508 qualified (Nov 2023), indicating certification pathways exist; the open question is scale, vendor breadth, and ecosystem maturity by 2035, not simple impossibility."}]}
**unique_insights:** 
  - {"model": "google/gemini-3.1-pro-preview", "insight": "Frames Rust’s current position as analogous to C++ in the 1990s: technically compelling and popular, but lacking the multi-implementation + formal-standard + long-horizon certification ecosystem that some industries demand for 30–50 year codebase guarantees."}
**blind_spots:** 
  - No model provides a defensible operational definition of 'primary language for systems programming' (new code vs maintained code; kernels vs user-space infra; safety-critical vs consumer), making displacement claims under-specified.
  - No explicit attempt at quantitative scenario modeling for 2035 (e.g., plausible ranges of Rust share in new greenfield systems work vs legacy maintenance) using multiple independent indicators (GitHub repo creation, package downloads, job postings, education pipeline, vendor SDK support).
  - Insufficient treatment of C (not just C++) as the dominant baseline in many embedded/firmware contexts; displacement dynamics often involve C↔Rust as much as C++↔Rust.
  - Toolchain and platform support gaps are not analyzed concretely (cross-compilation, tier-1/2 targets, vendor-provided HAL/SDKs, debugging/profiling parity, link-time optimization, build integration with Bazel/CMake, long-term support toolchains).
  - ABI and stability realities are not examined carefully: C++ ABI fragmentation vs Rust’s lack of a stable ABI, and how that constrains library ecosystems, plugin architectures, and long-lived binary interfaces.
  - Migration economics are discussed only qualitatively; missing are the dominant real-world cost drivers (testing/validation, rewriting unsafe concurrency logic, certification rework, retraining, opportunity cost) and where Rust most reliably yields ROI.
  - Security is treated mostly as memory safety; missing: supply-chain risk (crate provenance), auditability, reproducible builds, and how these interact with regulated procurement and enterprise risk management.
  - Domain-specific performance constraints are asserted (HFT/games/HPC) without evidence or nuance about which bottlenecks (latency tails, GC avoidance, vectorization, compile-time metaprogramming, ecosystem libraries) actually favor C++ vs Rust in 2026–2035.
  - No serious discussion of competing 'systems alternatives' beyond Rust/C++ (e.g., Zig, Swift-in-systems niches, Ada/SPARK in high-integrity contexts, Go in infra, WebAssembly as a deployment target), which affects what 'displace C++' could even mean.
  - Governance and ecosystem risk is underexplored: Rust edition changes, cargo/crates.io centrality, foundation governance, and the extent to which large organizations require multi-vendor stewardship similar to ISO processes.

### RAW PANEL RESPONSES (что панель реально сказала):

**[openai/gpt-5.2]:**
I can’t comply with your request as written because the “fusion” multi-model deliberation tool you referenced isn’t available in the toolset I have access to in this session (only web search/fetch tools are available). Since I can’t call “fusion,” I also can’t return its structured JSON output “verbatim” as instructed.

**[google/gemini-3.1-pro-preview]:**
{
  "consensus": "Rust is seeing rapid adoption for greenfield systems programming, cloud infrastructure, and safety-critical components, significantly reducing long-term maintenance costs. However, it will not completely displace C++ in the next 10 years. C++ will remain dominant due to its massive legacy codebases, entrenched ecosystem, high performance in specialized domains (HFT, game engines, HPC), and standard maturity. The landscape in 2035 will be characterized by coexistence and gradual integration via FFI boundaries rather than total replacement.",
  "contradictions": "While some projections suggest Rust will lead new systems programming projects, others point out that C++'s absolute growth still dwarfs Rust's, adding more developers annually than Rust's total user base. There is also a debate on whether C++'s staying power is purely 'inertia' versus a genuine structural advantage in formal ISO standardization, multiple implementations, and established ABI stability that Rust currently lacks.",
  "unique_insights": "The 'C++ vs Rust' narrative often ignores the historical maturity arc of programming languages. Rust in the 2020s is structurally where C++ was in the 1990s—popular, highly effective, but lacking multiple independent toolchains, formal ISO specifications, and the certified ecosystem required for 30-50 year codebase guarantees. Furthermore, a large portion of future integration will rely on tools like cxx to build bidirectional interoperability rather than full rewrites.",
  "blind_spots": "Most analyses assume current hardware compilation and AI coding assistant trends remain stagnant. There is little focus on how AI-driven code refactoring could accelerate C++-to-Rust translations, or conversely, how AI could mitigate C++ memory safety bugs. Additionally, the potential impact of C++ adopting 'Safe C++' language profiles by 2030 is often underestimated.",
  "partial_coverage": "The timeline and feasibility of Rust achieving full ISO standardization and multi-vendor compiler backends (like GCC's universal architecture support) by 2035 are mentioned but not definitively projected. Similarly, deep technical barriers like Rust's lack of expression templates or C++'s mature static reflection are touched upon but not exhaustively compared against future standard proposals.",
  "responses": [
    "Model A: Over the next 10 years, Rust will fundamentally change the systems programming landscape but will not displace C++. The adoption trend is clear: Rust is becoming the default choice for new, greenfield projects in cloud infrastructure, CLI tools, and OS components where memory safety is critical. Structurally, the barriers to Rust displacing C++ lie in the sheer volume of existing C++ code (billions of lines) across finance, games, and embedded systems, where rewriting is economically unviable. Those who benefit most from switching are teams building new distributed systems or dealing with high costs of security patching. In 2035, the landscape will be heavily bifurcated: C++ will maintain its grip on legacy systems, game engines, and HFT, while Rust will dominate cloud infrastructure and new subsystems, bridged by robust C-FFI interoperability.",
    "Model B: Rust's trajectory is incredibly strong, showing 52% market share in some metrics for new systems programming projects. However, displacing C++ by 2035 is highly unlikely because C++ itself is growing rapidly. From a structural perspective, C++ benefits from over 40 years of optimization, multiple vendor backends via GCC/Clang, and deep roots in domains requiring extreme low latency. The biggest barrier for Rust is the lack of a formalized ISO standard, ABI stability, and single-vendor governance (rustc). The realistic 2035 landscape is one where C++ continues to modernize (e.g., C++26 and beyond introducing safety profiles) to remain relevant, while Rust captures the 'safety-first' market. Both languages will experience growth, rather than a zero-sum displacement.",
    "Model C: The idea of Rust displacing C++ ignores the industrial realities of software engineering. Industries like aerospace, defense, and automotive plan for 30-50 year software lifecycles, requiring ISO certification (like ISO 26262), standardized mature tooling, and multiple compiler vendors. Rust is making progress (e.g., Ferrocene) but is still on a decade-long maturity arc. C++ developers already know their tools and can produce high-performance code predictably. While C+
…[обрезано, всего 4819 симв]

**[x-ai/grok-4.3]:**
{
  "consensus": "Rust will gain substantial ground in new systems programming projects but is unlikely to significantly displace C++ as the primary language over the next 10 years; coexistence and hybrid use is the most probable outcome through 2035.",
  "contradictions": "Some sources highlight C++'s entrenched ecosystem and certification barriers preventing rapid change, while others emphasize Rust's accelerating adoption in safety-critical new work and government pushes for memory safety; performance parity is affirmed but C++ SIMD/tooling edges noted inconsistently.",
  "unique_insights": "Rust adoption strongest in greenfield projects at startups and select sectors like automotive/IoT; C++ remains dominant in legacy-heavy domains (games, HFT, avionics, medical); interop tools like cxx enable incremental hybrid codebases; embedded market shows Rust at ~4.7% vs C++ 23% in 2024-2025 surveys with slow certification progress.",
  "blind_spots": "Insufficient coverage of economic incentives for massive C++ rewrites, detailed 2035 market share forecasts, or impacts from C++26 safety features/contracts; developer training costs and supply of Rust experts in regulated industries overlooked.",
  "partial_coverage": "Trends well-supported by 2024-2025 surveys and industry reports; structural barriers (ecosystem, certification, legacy code) detailed but quantitative projections to 2035 are speculative; beneficiary analysis focuses on new projects vs maintainers without role-specific quantification.",
  "responses": [
    "C++ has far deeper industry penetration; Rust growing in new greenfield systems... The most likely outcome is coexistence: Rust for new safety-critical systems, C++ for existing codebases...",
    "Rust is unlikely to completely replace C++ in the near term, but it’s already becoming the default choice for new systems programming projects... many teams... hybrid approach...",
    "Based on current trajectories... C++ will maintain dominance in industries with strict certification requirements... Rust adoption will continue accelerating... C++ remaining significant through at least 2030.",
    "We should aim to spread the benefits of Rust... making Rust feasible to adopt in both new and existing applications that make rich use of APIs in memory unsafe languages like C++.",
    "C++ remained the most commonly replaced language in 2024... Rust’s footprint in the programming world is expanding rapidly... Rust is no longer just a systems language."
  ]
}

======================================================================
## C2_cn_open  (panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   The panel agrees that Rust will not fully displace C++ as the primary systems programming language over the next 10 years, but it will become a major complementary language, especially for new safety-critical and infrastructure projects. Incremental adoption, hybrid codebases, and greenfield projects will be the norm. C++ will retain dominance in legacy systems, game development, high-frequency trading, and performance-critical niches where its ecosystem and mature tooling are indispensable.
**contradictions:** 
  There is disagreement on the extent of Rust's penetration. The 'Rust advocate' argues that regulatory pressure, kernel adoption, and safety certifications will make Rust the default for all new systems programming by 2035, while the 'C++ traditionalist' contends Rust will plateau around 20% market share due to the monumental weight of legacy code and the lack of a killer app that forces migration. Another tension lies in performance: some benchmarks show Rust 2-8% slower, others show parity, affecting adoption in latency-sensitive domains.
**unique_insights:** 
  - 1) The certification milestones (Ferrocene ISO 26262, MISRA C 2025 Addendum 6, OMG IDL4 Rust mapping) are the real accelerators, turning Rust from a language loved by developers into one mandated or strongly incentivized by regulators and standards bodies. 2) The ClickHouse model (98% C++, 2% Rust delivering the highest value per line) reveals that strategic incremental adoption can have outsized ROI without full rewrites. 3) The TCO frameworks being built show that risk-adjusted cost avoidance from memory-safety bugs is a board-level argument, not just an engineering preference. 4) The Linux kernel's declaration that 'Rust is here to stay' signals a tipping point for OS-level acceptance.
**blind_spots:** 
  - Much of the public discourse ignores the sociology of programming: C++ developers with decades of experience are not eager to discard their expertise, and many organizations prioritize shipping features over language safety. The largely unseen embedded world, where C dominates with 70% share and vendor toolchains are exclusively C/C++, faces massive inertia that could limit Rust's reach for decades. Moreover, C++ itself is not static; future standards may incorporate borrow checking or profiles that close the safety gap, reducing Rust's unique selling point, though significant progress has stalled.

### RAW PANEL RESPONSES (что панель реально сказала):

**[Systems Programming Expert]:**
Rust will not dethrone C++ as the 'primary' language for systems programming by 2035, but it will become a major player. Adoption trends show Rust growing from ~1.5% to maybe 15–20% of all systems code over the decade, driven by security-critical domains like cloud infrastructure, kernel code, and automotive ECUs. The Linux kernel now has official Rust support, Microsoft is shipping Rust drivers, and Android deploys Rust in kernels. However, C++ remains deeply entrenched with billions of lines of legacy code, vendor toolchain lock-in for embedded, and unmatched libraries for gaming, HFT, and scientific computing. The realistic 2035 landscape is a hybrid one: C++ for maintenance and legacy-critical paths, Rust for new modules requiring safety and concurrency. Government mandates (US Cyber Strategy, FCC) will push regulated industries, but not fast enough to cause a wholesale shift. The idea of a 'primary language' may become outdated as polyglot codebases emerge.

**[Business Analyst]:**
From an enterprise perspective, the switch to Rust is a risk-reduction investment, not a performance play. Boards are starting to approve incremental Rust migrations using TCO models that quantify breach cost avoidance. The clearest beneficiaries are companies with 10+ year product lifetimes, codebases that handle sensitive data, and those in regulated environments—fintech, healthtech, automotive safety. These organizations can justify the upfront ramp-up cost (3-6 months per developer, higher salaries) because the long-term reduction in memory-related CVEs (70% of vulnerabilities) cuts incident costs and potential regulatory fines. By 2035, we'll see Rust integrated into the majority of new systems projects in those sectors, but it won't be the 'primary' language in terms of total lines of code under management. The realistic landscape is one where C++ supports the core business logic and Rust wraps the exposed surfaces and new services, a pattern already proven by Google, Discord, and ClickHouse.

**[Rust Advocate]:**
Rust is on a trajectory to significantly displace C++ as the primary systems programming language by 2035. The evidence is mounting: Windows kernel, Linux kernel, Android, Volvo ECUs, and cloud infrastructure (73% of new cloud code is Rust) all demonstrate a snowball effect. With Ferrocene achieving ISO 26262 ASIL-D certification and MISRA rules being obsoleted by the compiler's ownership model, safety-critical industries will be forced to switch by regulators and insurers. The US government's recommendation to move to memory-safe languages will become a mandate, and companies that delay will face liability. While legacy C++ code will persist, it will be legacy—a COBOL of the systems world—as all new serious systems programming shifts to Rust. By 2035, Rust will hold over 40% of systems programming new code starts, and C++ will be relegated to maintenance mode. The tooling and ecosystem gaps will close rapidly as adoption scales.

**[C++ Traditionalist]:**
Reports of C++'s demise are greatly exaggerated. Rust is a fine language, but it will not 'significantly displace' C++ as primary. The installed base of C++ is 20-40 billion lines of code; rewrites are almost always failures (30% success rate). In embedded, C still owns 70% and C++ 23%; silicon vendors have little incentive to support Rust. Domains like game development, HFT, and scientific computing are married to C++ for performance reasons (Rust is still 2-8% slower in micro-benchmarks) and because their ecosystems (Unreal Engine, TensorFlow, BLAS) are C++. Even the safety argument weakens as C++ profiles and static analysis improve. The Linux kernel's 25k lines of Rust is a drop in the ocean of 34 million lines of C. By 2035, Rust will likely reach 10-15% market share in systems programming, a respectable niche, but not primary. C++ will continue to dominate, especially with C++26/29 introducing safer features, keeping its crown as the language of performance-critical infrastructure.

======================================================================
## C5_smartpanel_dumbjudge  (panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - Rust will not fully displace C++ but will dominate new, safety-critical, and greenfield systems programming by 2035
  - C++ will retain dominance in legacy codebases, performance-critical domains (gaming, HFT), and safety-certified systems
  - Hybrid C++/Rust codebases will become the norm, with Rust expanding incrementally through interoperability
  - Regulatory pressure on memory safety will accelerate Rust adoption in critical infrastructure sectors
**contradictions:** 
  - {"topic": "Rust's growth trajectory", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "TIOBE index slippage to #16 vs. 48.8% enterprise adoption growth"}, {"model": "glm-5.1", "stance": "C++ usage has not declined absolutely, migration is not zero-sum"}, {"model": "moonshotai/kimi-k2.6", "stance": "C++ still holds 20-23% Stack Overflow usage vs. Rust's 14-15%"}]}
  - {"topic": "C++ safety profiles", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "C++26 contracts may provide sufficient safety guarantees"}, {"model": "glm-5.1", "stance": "Profiles will not deliver memory safety by construction"}, {"model": "moonshotai/kimi-k2.6", "stance": "C++ will remain dominant in performance-critical domains regardless of safety profiles"}]}
  - {"topic": "Embedded systems adoption", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "Rust at 4.7% in production embedded systems"}, {"model": "glm-5.1", "stance": "Embedded market share projections reach ~10% by 2035"}, {"model": "moonshotai/kimi-k2.6", "stance": "Embedded conservatism and vendor toolchain inertia will limit growth"}]}
**unique_insights:** 
  - {"model": "deepseek/deepseek-v4-pro", "insight": "Rust's influence on C coding practices in the Linux kernel, inspiring cleaner C interface designs"}
  - {"model": "glm-5.1", "insight": "Detailed market share trajectory projections across domains (kernel, embedded, game dev, etc.)"}
  - {"model": "moonshotai/kimi-k2.6", "insight": "AI-assisted migration tools may accelerate component-level Rust adoption by 2035"}
**blind_spots:** 
  - Impact of AI-assisted code generation on adoption rates
  - Regional technology stack differences (China/Russia vs. Western tech companies)
  - Long-term sustainability of Rust's growth vs. C++'s evolutionary adaptations
  - Role of open-source community momentum in shaping language adoption
  - Certification pathways for Rust in safety-critical domains

### RAW PANEL RESPONSES (что панель реально сказала):

**[deepseek/deepseek-v4-pro]:**
{
  "consensus": "Rust will significantly increase its share of systems programming over the next decade, becoming the default for many new projects, but it will not fully displace C++ as the 'primary' language. By 2035, a dual-language landscape will be the norm: Rust dominates new, safety-critical, and greenfield development, while C++ retains its massive legacy codebase and sectors where toolchain maturity, certification, and existing institutional knowledge are paramount. Both languages will continue to coexist, with Rust gradually expanding its footprint through incremental adoption and improved interoperability.",
  "contradictions": [
    "Some data sources indicate Rust's growth is 'leveling off' (TIOBE index slippage to #16) while others show a 10-point jump in enterprise adoption over two years (48.8% of orgs using Rust non-trivially in 2025 Survey). This may reflect different metrics: mainstream search popularity versus actual production deployment.",
    "While Rust is celebrated for memory safety, some embedded surveys still show C at ~70% and C++ at 23%, with Rust at only 4.7% in production embedded systems, suggesting the displacement narrative is weaker in deeply embedded/real-time domains.",
    "The Linux kernel maintainers' summit decision to remove the 'experimental' tag from Rust reflects strong institutional commitment, yet the kernel still contains only ~25,000 lines of Rust versus 34 million lines of C, highlighting the immense gap between symbolic endorsement and practical displacement."
  ],
  "unique_insights": [
    "Rust's growing presence in the Linux kernel (official support in 7.0) is already changing C coding practices, with kernel maintainers openly crediting Rust for inspiring cleaner C interface designs and adoption of better memory management patterns.",
    "The Rust Foundation's Interop Initiative, backed by $1M from Google, signals a strategic pivot: acknowledging that displacing C++ entirely is unrealistic, and instead investing heavily in seamless C++/Rust mixed codebases as the real path forward.",
    "The 'beneficiaries' of switching are not monolithic: startups and greenfield teams gain the most immediate value (fewer bugs, faster development after learning curve), while large-scale enterprises benefit incrementally by rewriting only the most vulnerability-prone components in Rust.",
    "Compile-time performance remains the top user complaint, but the 2026 roadmap with parallel front-end, Cranelift debug backend, and faster linkers may largely neutralize this barrier within 2-3 years for typical development workflows.",
    "Government and industry pressure (e.g., White House report on memory-safe languages, CISA recommendations) is a structural force that will compel defense, automotive, and medical device sectors to adopt at least some Rust, regardless of language preference."
  ],
  "blind_spots": [
    "The impact of AI-assisted code translation (e.g., LLMs converting C++ to Rust) is not yet factored into adoption timelines; if such tools mature, they could dramatically accelerate migration of legacy codebases, making a more complete displacement plausible.",
    "The possibility of a 'C++ renaissance' via new safety profiles (e.g., C++26 contracts, safety annotations) is underexplored. If C++ manages to match Rust's safety guarantees while retaining backward compatibility, the migration incentive diminishes sharply.",
    "Most adoption data comes from Western tech companies; the picture in China, Russia, and other regions with different technology stacks and government priorities could be significantly different and may influence global trends.",
    "The assumption that Rust's learning curve will remain a barrier ignores the fact that universities are increasingly teaching Rust as a first systems language; by 2035, a cohort of 'Rust-first' graduates will enter the workforce, potentially shifting the default."
  ],
  "partial_coverage": "The analysis is stronger on enterprise backend, infrastructure, and kernel adoption, but weaker on real-time embedded, gaming, and high-frequency trading where C++'s deterministic tooling and decades of optimization still provide irreversible advantages. It also does not fully account for the fragmentation of C++ (C++17, C++20, C++23 adoption lags) which could make Rust's ecosystem velocity a more decisive factor.",
  "responses": {
    "Rust_Evangelist": "By 2035, Rust will be the dominant language for all new systems programming.
…[обрезано, всего 6940 симв]

**[z-ai/glm-5.1]:**
# Will Rust Significantly Displace C++ as the Primary Language for Systems Programming Over the Next 10 Years?

## Executive Summary

Rust will **not** "significantly displace" C++ as the *primary* systems programming language by 2035, but it will establish itself as a **co-equal pillar** in the systems programming landscape and become the default choice for **new** systems projects in several critical domains. The relationship will be characterized by coexistence, incremental migration, and domain-specific dominance rather than wholesale replacement.

---

## 1. Adoption Trends: Momentum is Real but Measured

### Current Market Position (2024–2025 Data)

| Metric | Rust | C++ |
|--------|------|-----|
| TIOBE Index Rank | #12 (1.26%) | #3 (8.03%) |
| Stack Overflow Usage | 14.8% of developers | 23.5% of developers |
| Developer Community Size | ~4 million | ~11.6 million |
| Embedded Market Share | ~4.7% (up from 2.1% in 2023) | ~23% (C holds ~70%) |
| Stack Overflow Admiration | #1 most admired (72%) | 41.8% admiration |

**Key trend signals:**
- Rust is the **fastest-growing** major language community (SlashData), with 2.267M developers using it and 709K identifying it as their primary language (JetBrains).
- 45% of Rust survey respondents say their organization makes non-trivial use of Rust, up 7 percentage points year-over-year.
- 38% of Rust users now use it for the majority of their work coding, up from 34%.
- Among C++ developers, 21% already use Rust to some degree and another 14% plan to adopt it (JetBrains). Critically, 58% of C++ developers who use Rust alongside C++ in the same project plan to migrate additional code to Rust.
- C++ was the **most commonly replaced language** by Rust migrants in 2024 (JetBrains).

**The nuance:** Rust's absolute growth rate is impressive, but from a small base. C++ usage has **not declined** in absolute terms even as Rust rises—the migration isn't a zero-sum substitution yet. As The New Stack's research director noted: "the migration from C++ to Rust isn't happening all at once."

### The Kernel Milestone

The most consequential adoption signal occurred in 2025: the Linux Kernel Maintainers Summit formally declared the Rust experiment **"concluded"**—Rust is now a permanent, supported language in the kernel. This is a watershed moment:

- **Android 16** ships the first production Rust kernel driver (ashmem) to **millions of devices** via the 6.12 LTS kernel.
- The **DRM (graphics) subsystem** is approximately one year away from **requiring Rust and disallowing C for new drivers**.
- **Microsoft** is building first-class Rust support for Windows kernel drivers, with safe Rust abstractions for the Windows Driver Framework already shipping.
- **Debian** is establishing "hard Rust requirements" in its package manager starting May 2026.

This kernel-level institutionalization is the single strongest signal that Rust is becoming infrastructure-grade, not just trendy.

---

## 2. Key Structural Barriers to Displacement

### Barrier 1: The Trillions of Lines of Legacy C++

The foundation of modern operating systems, game engines, browsers, and embedded systems is deeply rooted in C and C++. As one analysis noted: "The sheer volume of existing C++ code makes wholesale replacement impractical." Rewriting massive codebases is costly, risky, and often provides little tangible benefit to end-users. Businesses prioritize functionality and stability over the underlying language.

**Reality check:** The Chromium browser alone is ~35 million lines of C++. The Windows codebase is orders of magnitude larger. These will not be rewritten.

### Barrier 2: Ecosystem Maturity Gaps

The Rust ecosystem shows **uneven maturity across domains**—excellent for CLI tools and web backends, but significantly lacking in:

- **Embedded systems**: The `no_std` ecosystem has significant gaps; debug builds become too large for small controllers; cross-compilation adds complexity; silicon vendors overwhelmingly support only C/C++ toolchains.
- **Safety-critical applications**: Certification under DO-178C (avionics), ISO 26262 (automotive), and similar frameworks remains a major hurdle. The Rust language itself lacks a formal specification, which is a prerequisite for most safety certification pathways.
- **GUI development**: No mature, competitive framework comparable to Qt exists.
- **Game development**: While making inroads, no equivalent to Unreal Engine's C++ ecosystem.

The Rust Blog's own 2026 analysis a
…[обрезано, всего 14857 симв]

**[moonshotai/kimi-k2.6]:**
**Short answer:** No, Rust will not *fully displace* C++ as the primary systems language by 2035, but it will fundamentally reshape the landscape. By 2035, expect a bifurcated world: **Rust as the default for new systems programming**, and **C++ as the entrenched incumbent in legacy codebases, gaming, HFT, and conservative embedded domains**. Massive hybrid codebases will be the norm, not pure Rust replacements.

---

### 1. Adoption Trends (Where We Are Today)

Rust is undeniably in a high-growth phase:
- **Job market:** Postings doubled in two years (to ~606 open roles by early 2026), with salaries averaging **$130K+** (15–40% above comparable roles in Go/C++). Rust developers are doubling roughly every 18 months, now numbering ~4 million.
- **Enterprise penetration:** ~48.8% of organizations reported non-trivial Rust in production by 2025 (up from 38.7% in 2023). Backend/infrastructure dominates (51.7%), followed by cloud (25.3%).
- **Industry wins:** 
  - **Linux kernel:** 150K+ lines of Rust in-tree.
  - **Mobile/OS:** Google reported a **70% reduction in memory vulnerabilities** in Android Rust code; Microsoft is shipping Rust in Windows kernel drivers.
  - **Cloud:** AWS Firecracker (trillions of Lambda requests) and Cloudflare Pingora (trillions of daily requests) are Rust-native.
  - **Embedded:** Rust grew from **2.1% to 4.7%** of production embedded systems between 2023–2024; automotive (Volvo, Polestar) and robotics are moving fastest.
- **Developer sentiment:** Rust remains the most admired language on Stack Overflow (72%), and C++ is the language most commonly replaced by migrating teams.

However, **absolute volume still favors C++:** In embedded, C holds ~70% and C++ ~23%. In Stack Overflow surveys, C++ usage (20–23%) still outpaces Rust (~14–15%). Rust is winning mindshare and *new* projects, not existing lines of code.

---

### 2. Key Structural Barriers to Displacement

**Legacy gravity is overwhelming.** The single biggest barrier is that industry runs on billions of lines of working C++, much of it in systems that are too risky and expensive to rewrite. High-frequency trading firms, game engines (Unreal), telecom infrastructure, and aerospace codebases represent decades of institutional knowledge. The economics favor incremental migration, not replacement.

**Language interoperability friction.** C++ and Rust have a fundamental expressiveness mismatch—C++’s unrestricted aliasing, inheritance, and overloading do not map cleanly to Rust’s ownership model. While C interop works, rich C++ interop remains an active research/deficiency area (the Rust project itself has identified "seamless C++/Rust interop" as a major unsolved goal). FFI boundaries introduce cost, risk, and often force `unsafe` Rust, blunting safety benefits.

**Certification and toolchain inertia.** C++ is entrenched in safety-critical certification regimes (ISO 26262 for automotive, DO-178C for avionics, IEC 61508 for industrial). While Rust toolchain qualification efforts are underway (Ferrous Systems, AdaCore offering ASIL-D qualified Rust), these are early-stage. Medical devices and traditional avionics will lag because recertifying a codebase is a multi-year, multi-million-dollar process.

**Embedded conservatism.** Many embedded targets still rely on bespoke C++ toolchains, vendor BSPs, and hardware abstraction layers with no Rust support. Semiconductor vendor support is improving but remains years behind C++.

**Talent pipeline paradox.** Rust’s learning curve is real—enterprises report 2–3 months of onboarding before meaningful contribution. While Rust jobs are growing 35% YoY, if the talent pool continues doubling every 18 months, the current salary premium may compress by the late 2020s.

---

### 3. Who Benefits Most from Switching

The switch provides the highest ROI for:

| Profile | Why They Benefit |
|---------|------------------|
| **Security/safety-critical industries** | Automotive (ADAS/ECUs), robotics, aerospace, and IoT manufacturers eliminate ~70% of vulnerability classes at the language level. Regulatory tailwinds (e.g., FAA/FCC pressure on memory safety) are accelerating this. |
| **New/greenfield projects** | Startups and new microservices without legacy baggage can adopt Rust as the default. No FFI complexity, no sunk-cost fallacy. |
| **Untrusted-input processing** | Parsers, network services, file format handlers, and sandboxed execution environments gain the most from compile-time memory safety. |
| **Clo
…[обрезано, всего 7892 симв]

======================================================================
## C5inv_dumbpanel_smartjudge  (panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - Rust will not fully displace C++ within 10 years; coexistence is the most likely outcome, with Rust gaining share in new/greenfield projects and safety-critical domains while C++ remains entrenched in legacy codebases.
  - Rust's memory safety guarantees are the primary structural driver of its adoption, especially in security-sensitive and regulated contexts.
  - C++'s entrenched ecosystem, backward compatibility, and decades of compiler optimization keep it dominant in existing systems and performance-critical niches.
  - Hybrid Rust+C++ architectures are emerging as a practical compromise, using FFI/interop for new safety-critical components alongside existing C++ cores.
  - Rust's learning curve (ownership/borrow checker) is a meaningful adoption barrier, particularly for organizations with deep C++ expertise.
**contradictions:** 
  - {"topic": "Rust overtaking C++ in developer count by 2030", "stances": [{"model": "z-ai/glm-4.7-flash", "stance": "Rust could overtake C/C++ in developer count by 2030, acquiring ~1.9% of developers annually."}, {"model": "evidence", "stance": "Linear extrapolation is methodologically flawed. SlashData 2025 shows C++ is also among the fastest-growing languages; Herb Sutter notes C++, Python, and Java each add about as many developers per year as Rust has total. C++ developer count is growing in absolute terms, not stagnant."}]}
  - {"topic": "Rust certification viability in regulated/safety-critical industries", "stances": [{"model": "qwen/qwen3-8b", "stance": "C++ dominates regulated industries (medical, avionics) due to certification requirements; Rust lacks mature certification support."}, {"model": "evidence", "stance": "Multiple ISO 26262 ASIL D qualified Rust compilers now exist (Ferrocene, HighTec for Infineon AURIX and ARM Stellar, AdaCore GNAT Pro). Volvo, Renault/Ampere, and Elektrobit are already shipping Rust in automotive ECU contexts. The certification gap is closing rapidly."}]}
  - {"topic": "C++26 safety features closing the gap with Rust", "stances": [{"model": "z-ai/glm-4.7-flash", "stance": "C++26 Contracts, safety profiles, and SIMD enhancements will erode Rust's strategic safety advantage, making C++ 'good enough' for 80% of use cases."}, {"model": "evidence", "stance": "C++26 Contracts remain controversial—multiple papers (P3829, P3835, P3909) propose deferral to C++29 or a White Paper due to unresolved safety and semantics concerns. C++26 bounds safety applies only to standard library types and requires recompilation; it is incremental hardening, not fundamental memory safety like Rust's ownership model."}]}
  - {"topic": "C++ market share in game development and HFT", "stances": [{"model": "z-ai/glm-4.7-flash", "stance": "C++ holds 84% market share in game development and 94% in HFT."}, {"model": "evidence", "stance": "C++ holds approximately 44% of the game development platform market by revenue. The 84% and 94% figures appear fabricated with no verifiable source. While C++ is clearly dominant in both domains, the specific numbers are unjustified."}]}
  - {"topic": "Performance parity between Rust and C++", "stances": [{"model": "z-ai/glm-4.7-flash", "stance": "Some sources cite C++ maintaining a 2-3% micro-benchmark lead; others argue real-world tests favor Rust due to fewer runtime bugs, with the gap converging to noise."}, {"model": "qwen/qwen3-8b", "stance": "C++'s advanced metaprogramming and mature toolchains (GCC, SIMD support) remain unmatched performance advantages."}]}
**unique_insights:** 
  - {"model": "z-ai/glm-4.7-flash", "insight": "Regulatory/compliance pressure (CISA, NSA, GDPR, cyber-risk insurance) is becoming an existential driver for Rust adoption—not performance or developer preference, but legal liability. This could force C++ out of safety-critical niches regardless of technical merit."}
  - {"model": "z-ai/glm-4.7-flash", "insight": "The displacement will be structural (new architecture) not total (replacement of existing C++): Rust wins new systems projects while C++ retains majority of production lines of code, meaning Rust could dominate growth metrics while C++ dominates absolute volume."}
  - {"model": "google/gemma-3-12b-it", "insight": "Rust's rise is largely driven by catastrophic consequences of memory errors in networked/embedded systems, not general programming dissatisfaction—safety is the wedge, not tooling or ergonomics."}
  - {"model": "qwen/qwen3-8b", "insight": "C++'s advanced metaprogramming capabilities (TMP, CRTP) represent a genuine expressiveness mismatch with Rust's type system that limits Rust's ability to replace C++ in heavily templated codebases, beyond just ecosystem inertia."}
**blind_spots:** 
  - DARPA TRACTOR program: Automated C-to-Rust translation is being actively funded by the U.S. government, which could drastically accelerate migration in legacy codebases—no model addressed this.
  - C++ is also growing rapidly in absolute developer count, not stagnating: SlashData 2025 reports both C++ and Rust as the fastest-growing major languages. The framing of Rust growing while C++ stands still is empirically wrong.
  - Rust's 'unsafe' keyword creates a practical safety escape hatch that can undermine the language's guarantees in production code—CISA's own guidance notes this risk, but no model discussed the boundary between safe and unsafe Rust in real systems.
  - Carbon language (Google's C++ successor) and other intermediate approaches were not discussed as potential competitors or complements to both Rust and C++.
  - The educational pipeline shift: no model analyzed whether universities are adopting Rust in systems programming curricula, which could create a generational talent pool shift starting ~2028.
  - China's independent language ecosystem and potential regulatory divergence: Chinese tech giants and government may follow different adoption patterns that affect global language dynamics.
  - Rust's governance and stability challenges: the language's rapid evolution, edition system, and occasional community governance controversies could create adoption friction not captured by technical comparisons.
  - The role of cyber-insurance pricing: as insurers quantify memory-safety risk, premium differentials between C++ and Rust codebases could become a concrete economic driver no model modeled.

### RAW PANEL RESPONSES (что панель реально сказала):

**[qwen/qwen3-8b]:**
{
  "consensus": "Rust and C++ will coexist rather than displace each other. C++ maintains deeper industry penetration, especially in legacy systems, while Rust gains traction in new greenfield systems and safety-critical components. Both languages are used together in production, with C++ handling core engines and Rust addressing specific safety needs.",
  "contradictions": "C++'s entrenched ecosystem and backward compatibility contrast with Rust's newer, rapidly evolving tooling. While Rust offers memory safety and modern features, C++'s advanced metaprogramming capabilities (e.g., TMP, CRTP) and mature toolchains (GCC, SIMD support) remain unmatched. The \"C++ vs Rust\" framing is criticized as a false dichotomy, with hybrid approaches becoming common.",
  "unique_insights": "Rust's adoption is accelerated in security-sensitive embedded systems and networked devices, while C++ dominates regulated industries (e.g., medical, avionics) due to certification requirements. Interoperability tools like `cxx` enable bidirectional integration, but Rust's lack of support for bare-metal MCU targets and mature libraries in areas like async/web remains a barrier. C++20/23's incremental improvements and backward compatibility ensure continued relevance.",
  "blind_spots": "Uncertainty about how rapidly Rust's ecosystem will mature to address gaps in mature libraries and tooling for embedded systems. Potential underestimation of C++'s ability to adopt safety features (e.g., C++26's execution model) and the long-term impact of Rust's growing community on legacy codebases.",
  "partial_coverage": "Analysis focuses on current trends (2023-2024) and near-term projections (2030), but speculative assumptions about 2035 may lack concrete data. The role of AI/ML in shaping future language adoption is not explicitly addressed.",
  "responses": [
    {
      "panel": "bigcpp.com",
      "answer": "C++ has 40+ years of ecosystem, billions of lines in production, and millions of developers. Rust is taking new greenfield systems work and has been adopted in the Linux kernel and some OS codebases. The most likely outcome is coexistence: Rust for new safety-critical systems, C++ for existing codebases and areas needing its ecosystem."
    },
    {
      "panel": "Rust Project Goals",
      "answer": "Rust adoption is feasible in new systems but faces barriers in existing C++ codebases. Interoperability tooling and language expressiveness mismatches (e.g., C++ metaprogramming vs. Rust's type system) limit adoption. The goal is to make Rust feasible for existing C++ projects without compromising safety."
    },
    {
      "panel": "QuantLabsNet",
      "answer": "Developers resist switching due to existing C++ codebases, cost of rewriting, and C++'s continuous evolution. C++ remains relevant for systems programming, with its backward compatibility and performance advantages ensuring its place in the landscape."
    },
    {
      "panel": "JetBrains CLion Blog",
      "answer": "Rust set a new popularity record in 2023, but C++ and C remain top languages. C++20 adoption is growing, and Rust is often used alongside C++ for specific components. Hybrid approaches are becoming common, but Rust's integration into existing projects remains challenging."
    },
    {
      "panel": "CPP Cat",
      "answer": "C dominates embedded systems (70%), with C++ at 23% and Rust growing to 4.7%. Rust gains traction in security-sensitive areas, but C++ will maintain dominance in regulated industries. Hybrid approaches and formal verification progress will shape the embedded landscape."
    }
  ]
}

**[google/gemma-3-12b-it]:**
```json
{
  "consensus": "There's a general agreement that Rust will continue to gain traction in systems programming, potentially eroding C++'s dominance but not fully displacing it within the next 10 years. Both languages have strengths and weaknesses, and their adoption will depend on specific project requirements, developer expertise, and evolving industry trends. Rust's safety features are a significant draw, especially for new projects, while C++'s legacy codebase and performance optimizations remain valuable.",
  "contradictions": [
    "Some sources emphasize Rust's rapid adoption and potential for widespread use, suggesting a more significant shift than others. Conversely, some argue that C++'s established ecosystem, extensive libraries, and performance characteristics will ensure its continued relevance for high-performance and legacy systems.",
    "The degree to which the learning curve of Rust will hinder its adoption vs. the existing investment in C++ is debated. Some believe the safety benefits outweigh the initial investment, while others cite the complexity of Rust's ownership and borrowing system as a significant barrier."
  ],
  "unique_insights": [
    "Rust's rise is largely driven by a need for safer systems programming, particularly in areas like embedded systems and operating systems where memory errors can have catastrophic consequences.",
    "C++'s continued relevance is tied to its performance optimization capabilities and its extensive use in high-performance computing, game development, and finance – domains where every microsecond counts.",
    "The emergence of 'safe C++' initiatives, such as using static analysis tools and coding standards, aims to mitigate C++'s safety concerns without requiring a complete language switch.",
    "The 'WebAssembly' ecosystem presents both opportunities and challenges for both languages. Rust is well-suited for building performant WebAssembly modules, while C++’s existing WebAssembly support provides an advantage."
  ],
  "blind_spots": [
    "The analysis doesn't fully address the impact of AI-assisted coding tools on both languages. AI could potentially lower the barrier to entry for Rust and also help developers write safer C++ code.",
    "The long-term implications of quantum computing on systems programming languages are not considered. Both Rust and C++ may need to evolve to support quantum algorithms.",
    "The influence of hardware architectures (e.g., specialized processors, RISC-V) on the choice between Rust and C++ is not fully explored."
  ],
  "partial_coverage": [
    "Adoption trends: The analysis mentions increasing Rust adoption but lacks specific data and metrics to quantify it. It could benefit from including adoption rates in different industries and open-source projects.",
    "Structural barriers: While the complexity of Rust's ownership system is mentioned, other barriers like the availability of libraries and tooling for specific domains are not fully explored.",
    "Who benefits most: The analysis correctly identifies benefits for security-critical projects but could expand on which types of companies and developers are most likely to switch.",
    "Realistic landscape in 2035: The analysis provides qualitative predictions but lacks specific scenarios or projections on market share and language usage."
  ],
  "responses": {
    "panel_model_1": "Rust’s memory safety features, concurrency without data races, and modern tooling are increasingly attractive for systems programming. While C++ boasts a long history, extensive libraries, and performance advantages, Rust’s growing ecosystem and safety guarantees are making it a strong contender. Expect Rust to displace C++ in new projects, especially where security is paramount. Legacy codebases in C++ will remain, and specialized applications will continue to use C++ for its performance. By 2035, Rust might hold 30-40% of the systems programming landscape, with C++ remaining dominant in specific niches.",
    "panel_model_2": "C++’s established position in high-performance computing, game development, and embedded systems is difficult to challenge. Rust's learning curve can be significant, hindering widespread adoption. However, Rust's safety advantages are undeniable, and its usage is growing in areas like operating system development and blockchain technologies. It is unlikely that Rust will completely replace C++ within the next decade. Instead, we’ll see a hybrid approach where
…[обрезано, всего 5619 симв]

**[z-ai/glm-4.7-flash]:**
I'll help you analyze Rust's potential to displace C++ in systems programming. Let me gather current information on adoption trends, barriers, and expert predictions.```json
{
  "consensus": "Rust will not fully displace C++ as the primary systems programming language over the next 10 years, nor should it. The trajectory points toward a definitive 'coexistence' model rather than a total replacement. Rust is rapidly gaining significant market share in *new* projects and security-critical domains (cloud infrastructure, embedded safety, network services), projected to capture 25-35% of new systems programming projects by 2030, while C++ remains entrenched in legacy systems, high-frequency trading, game engines, and domains requiring extreme hardware optimization. By 2035, the landscape will likely feature hybrid codebases where C++ handles core engines and Rust handles safety-critical components, with C++ retaining the majority of lines of code but losing dominance in growth metrics.",
  "contradictions": {
    "Developer Count vs. Production Impact": "Analyses vary wildly on the 'overtake' timeline. Some projections suggest Rust could overtake C/C++ in developer count by 2030 (based on current year-over-year growth rates), while others argue that developer count does not equate to production code dominance, especially in C++-heavy industries like embedded and finance where codebases are massive and entrenched. There is a contradiction between the 'speed of adoption' narrative for Rust and the 'durability of the ecosystem' narrative for C++.",
    "Performance Benchmarking": "Some sources cite C++ maintaining a small lead (2-3%) in specific micro-benchmarks and back-end optimization, while others argue that 'real-world' tests often favor Rust due to fewer runtime bugs, and that the performance gap has converged to 'noise levels' for most applications. This creates a tension between laboratory dominance and practicality.",
    "Safety vs. Complexity": "Proponents argue that Rust's memory safety features (ownership/borrow-checker) are the primary enabler of displacement, while critics cite Rust's steep learning curve and complexity as barriers. Conversely, there is an argument that C++26 is incorporating safety features (contracts, standard concepts) that will erode Rust's primary advantage, making C++ safer and slowing Rust's growth in certain circles."
  },
  "unique_insights": {
    "The 'New Work, Existing Stack' Strategy": "The most common successful pattern in the real world is not rewriting C++ code in Rust, but rather adopting a 'dual-stack' approach. Companies like HERE, Microsoft, and trading firms are keeping their core C++ engines running and writing new microservices or safety-critical components in Rust, using FFI (Foreign Function Interface) to stitch them together. This strategy minimizes risk while capturing safety benefits.",
    "Inversion of Priority": "For startups and new organizations, Rust is increasingly becoming the default 'systems' language for greenfield projects due to modern tooling (Cargo, Rust Analyzer) and the ability to hire fewer senior engineers to achieve high safety standards. For established giants, C++ is the default due to the massive investment in existing talent and libraries.",
    "The C++ 26 Factor": "A critical blind spot in many predictions is the evolution of C++ itself. The introduction of modern safety profiles, Contracts, and SIMD enhancements in C++26 suggests C++ is actively evolving to patch its safety gaps, potentially slowing Rust's \"strategic\" advantage if C++ becomes 'good enough' for 80% of use cases without the migration cost.",
    "AI as a Catalyst": "Rust's complexity acts as a barrier, but AI coding assistants (like Claude or GPT-4) are beginning to lower this barrier effectively for new developers, accelerating Rust's adoption in contexts where hiring is a bottleneck."
  },
  "blind_spots": {
    "The Unseen Cost of C++ Errors": "Most cost-benefit analyses focus on the *development* cost of Rust (learning curve) but undervalue the *operational* and *legal* cost of C++ vulnerabilities (CVEs, regulatory fines, downtime). The total cost of ownership (TCO) for long-lived C++ systems in safety-critical sectors (autonomous vehicles, medical devices) is likely much higher than estimated, potentially favoring Rust's TCO in the long term.",
    "Hardware Vendor Lock-in": "The analysis often underplays the role of hardware vendors (MCU manufacturers). For many emb
…[обрезано, всего 9558 симв]

======================================================================
## C6_echo  (panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - Rust is gaining significant traction in systems programming, particularly for new projects where memory safety, concurrency, and modern tooling are priorities.
  - C++ remains dominant in legacy systems, game development, high-frequency trading, and domains with mature ecosystems and certified libraries.
  - The Linux kernel has moved beyond the 'experimental' phase for Rust, with support now considered stable and production-ready as of late 2025.
  - Major tech companies (Google, Microsoft, Amazon) are using Rust in production for security-critical components, especially in Android, Windows, and cloud infrastructure.
  - Hybrid codebases using Rust for new components via FFI and maintaining C++ for legacy systems are the dominant transition strategy.
  - Rust provides superior memory safety by eliminating entire classes of vulnerabilities (e.g., buffer overflows, data races) at compile time, resulting in a >1000x reduction in memory safety vulnerability density compared to C++.
  - Rust adoption is strongest in cloud infrastructure, security, embedded systems, and safety-critical applications.
**contradictions:** 
  - {"topic": "Will Rust displace C++ as the primary language?", "stances": [{"model": "qwen/qwen3-235b-a22b-2507", "stance": "Rust will not fully displace C++ but will dominate new projects in safety-critical domains; coexistence is the likely outcome."}, {"model": "qwen/qwen3-235b-a22b-2507", "stance": "Rust is on track to become the dominant language for new systems programming, potentially displacing C++ in market share of new code by 2035."}, {"model": "qwen/qwen3-235b-a22b-2507", "stance": "Rust will become the default choice for nearly all new development and displace C++ by 2035."}, {"model": "evidence", "stance": "Current data (2025) shows Rust usage at 20.7% in professional systems programming, while C++ is at 45.7%, indicating C++ still dominates overall usage; displacement is not imminent."}]}
  - {"topic": "C++'s evolution and vitality", "stances": [{"model": "qwen/qwen3-235b-a22b-2507", "stance": "C++ is growing alongside Rust; modern standards (C++20/23) are addressing prior weaknesses, and demand for performance ensures its relevance."}, {"model": "qwen/qwen3-235b-a22b-2507", "stance": "C++ remains entrenched due to its ecosystem but is not growing as aggressively as Rust in new projects."}]}
**unique_insights:** 
  - {"model": "qwen/qwen3-235b-a22b-2507", "insight": "Google's Android data shows Rust code has a 4x lower rollback rate and 25% faster code reviews than C++, indicating safety improves developer productivity, not just security."}
  - {"model": "qwen/qwen3-235b-a22b-2507", "insight": "Even with `unsafe` blocks, Rust's overall vulnerability density remains over 1000x lower than C++, because unsafe code is isolated, audited, and does not negate the language's core safety model."}
  - {"model": "qwen/qwen3-235b-a22b-2507", "insight": "Full migration of large C++ codebases often fails due to dual maintenance overhead, opportunity cost, and testing challenges; incremental adoption via FFI or cxx is more sustainable."}
**blind_spots:** 
  - None of the models address Rust's performance in hard real-time systems, where predictable worst-case execution time and interrupt latency are critical and where C++ and C still dominate.
  - There is no discussion of how AI code generation tools (e.g., Copilot with Rust) are lowering onboarding costs and mitigating Rust's steep learning curve.
  - No model analyzes hiring trends, salary data, or regional adoption differences (e.g., Rust adoption in Asia vs. North America) which are critical to long-term language dominance.
  - The educational pipeline for Rust—such as university curricula, Rust in computer science programs—is underexplored despite its importance for future developer supply.
  - Impact of semiconductor vendors' toolchain support (e.g., ARM, Infineon) on embedded Rust adoption is noted but not analyzed in depth, despite HighTec's ASIL D-qualified toolchain being a major enabler.

### RAW PANEL RESPONSES (что панель реально сказала):

**[qwen/qwen3-235b-a22b-2507]:**
{
  "consensus": "Rust is gaining significant traction in systems programming, particularly for new projects where memory safety, concurrency, and modern tooling are priorities. However, it is not projected to fully displace C++ over the next decade. Instead, both languages will coexist, with C++ remaining dominant in established domains (like game engines, legacy systems, and high-performance computing) due to its mature ecosystem and deep expertise, while Rust becomes the default choice for new systems programming initiatives in cloud infrastructure, safety-critical embedded systems, and security-sensitive applications. The industry trend is toward hybrid adoption, using Rust for new components and services while maintaining C++ for legacy code, facilitated by FFI interoperability.",
  "contradictions": [
    "Some sources claim Rust is 'winning' new low-latency projects (BSWEN), while others note that even in 2025, new C++ projects are still being started by teams with existing expertise (BSWEN, CodeHowToGuide), indicating a split in real-world adoption based on team context."
  ],
  "unique_insights": [
    "The primary driver for Rust adoption is not performance, but the elimination of an entire class of memory-safety bugs (buffer overflows, use-after-free, data races) at compile time, which translates to a 94% or greater reduction in memory-safety vulnerabilities compared to C++ (CodeHowToGuide, The New Stack). This is a critical factor for security and reliability in new systems.",
    "C++'s largest advantage is not its language features, but its structural barriers: an immense installed base of code, deeply integrated toolchains, mature certified libraries for domains like avionics (DO-178C) and automotive (ISO 26262), and a vast pool of experienced developers. Rewriting in Rust carries enormous risk and cost, which is why the hybrid, incremental approach is the dominant migration strategy (BSWEN, DNA.inc)."
  ],
  - The primary driver for Rust adoption for new projects, especially in embedded and infrastructure, is regulatory and security necessity. The FCC's router security mandates and government cybersecurity strategies are turning Rust's safety from a 'nice-to-have' into a 'compliance requirement' (unengineering.ghost.io).

**[qwen/qwen3-235b-a22b-2507]:**
{
  "consensus": "Rust is experiencing rapid adoption in systems programming, particularly in new projects, security-critical applications, and infrastructure where memory safety and performance are paramount. Enterprise adoption has grown significantly, with nearly half of organizations using Rust in production by 2025. C++ remains dominant in existing systems, especially in industries like game development, embedded systems (excluding new safety-critical use cases), and low-latency trading, where legacy codebases and deep domain expertise make migration impractical. Both Rust and C++ are among the fastest-growing languages, indicating that Rust is supplementing rather than outright replacing C++. The future landscape in 2035 will likely be hybrid, with Rust increasingly preferred for greenfield projects requiring memory safety, while C++ maintains a strong hold in areas benefiting from its mature ecosystem, compiler support, and established developer base.",
  "contradictions": "Some sources frame Rust as 'quietly consolidating' in enterprise and systems programming to the point of being a 'core language' in the Linux kernel, suggesting a structural displacement of C++ and C. Others emphasize that C++ is growing just as fast—if not faster in absolute numbers—than Rust, undermining the narrative of displacement. There is also disagreement on the pace of Rust's encroachment in embedded systems: while one source notes a doubling from 2.1% to 4.7% in just one year, another stresses C++'s 23% share and ongoing relevance due to vendor support and certification standards. Additionally, some portray C++ as losing mindshare among students and startups, while others highlight C++20/23 adoption as evidence of the language's ongoing modernization and vitality.",
  "unique_insights": [
    "Rust is making significant inroads into build tooling (e.g., Biome, Rspack, Rolldown), where its performance benefits are delivering 10–30x speedups in real-world environments, expanding its influence beyond traditional systems roles.",
    "The Linux kernel's formal acceptance of Rust as a non-experimental core language, despite its small code footprint (25,000 lines vs. 34 million in C), is a symbolic and practical milestone, validating Rust's viability for real-time, safety-critical systems.",
    "Major tech companies (Microsoft, Google, Amazon) are already shipping production Rust code in core systems (Windows, Android, Firecracker), demonstrating not just experimental interest but strategic commitment.",
    "C++'s growth is being fueled not by stagnation but by alignment with enduring constraints: demand for performance, hardware efficiency, and human productivity, with modern standards (C++20/23) addressing prior weaknesses.",
    "Hybrid development—using Rust for new components while maintaining C++ cores via FFI—is emerging as the dominant transition strategy, reducing risk and enabling incremental adoption."
  ],
  "blind_spots": [
    "No source provides detailed data on Rust vs. C++ hiring trends, compensation, or regional differences in adoption (e.g., Asia vs. North America), which could affect the scalability of Rust adoption.",
    "None of the results deeply analyze the educational pipeline—how many CS students are learning Rust versus C++—which will shape long-term language dominance.",
    "There is minimal discussion of government, aerospace, or medical device certification standards and their timelines for recognizing Rust, a critical barrier in regulated environments where C++ is entrenched.",
    "The role of AI in mitigating Rust's learning curve (e.g., AI-assisted borrow checker resolution) is underexplored, despite widespread AI use in code generation.",
    "Trade-offs in runtime characteristics—such as predictable worst-case memory allocation or interrupt latency in bare-metal Rust—are not addressed, though they are essential in hard real-time embedded systems."
  ],
  "partial_coverage": [
    "The Linux kernel's adoption of Rust is well-covered in terms of policy (removal of 'experimental' tag) and maintainers' intentions (e.g., DRM drivers requiring Rust), but not in terms of the actual rate of new Rust driver submissions or contributor onboarding challenges.",
    "Enterprise usage statistics (e.g., 48.8% using Rust) are cited across multiple sources, but no breakdown is provided by industry vertical (e.g., finance vs. automotive), limiting insight into where adoption is strongest.",
    "C++'s ongoing evolu
…[обрезано, всего 9359 симв]

**[qwen/qwen3-235b-a22b-2507]:**
{
  "consensus": [
    "Rust is making significant inroads in systems programming, particularly in new projects where memory safety, concurrency, and maintainability are critical.",
    "Major technology companies like Google, Microsoft, and Amazon are actively adopting Rust for security-critical components in Android, Windows, and cloud infrastructure.",
    "Rust adoption is rapidly increasing in embedded systems, autonomous vehicles, aerospace, IoT, and blockchain, driven by safety guarantees and modern tooling.",
    "C++ retains dominance in legacy systems, game engines, high-frequency trading, and domains with deep library ecosystems and certification requirements.",
    "Interoperability through FFI allows hybrid codebases, making gradual adoption of Rust feasible without full rewrites.",
    "Rust offers comparable or superior performance to C++ in many benchmarks, with zero-cost abstractions and fearless concurrency, while eliminating entire classes of memory safety bugs at compile time.",
    "The primary structural barriers to Rust displacing C++ include C++'s vast legacy codebase, deeper platform support (especially in embedded systems), steeper initial learning curve for Rust, and immature tooling for seamless C++/Rust interop.",
    "Rust's tooling (Cargo, Clippy, rustfmt) is more unified and modern compared to C++’s fragmented ecosystem (Make, CMake, Conan), enhancing developer productivity."
  ],
  "contradictions": [
    "While some sources state that Rust is 'becoming the default choice' for new systems programming projects, others emphasize that C++ remains the pragmatic default when team expertise or existing libraries are decisive factors.",
    "Microsoft and Google are aggressively pushing Rust, but other large engineering organizations (e.g., in high-frequency trading or game development) continue to choose C++ for new projects, indicating no industry-wide consensus on language strategy."
  ],
  "unique_insights": [
    "Rust code exhibits significantly lower rollback rates (~4x lower according to Android data) and faster code review times (~25% less) than C++, suggesting that safety guarantees translate directly into improved software delivery velocity and stability.",
    "The presence of `unsafe` blocks in Rust does not negate its safety benefits; empirical data shows that even with a small percentage of unsafe code, the overall vulnerability density is over 1000x lower than in C++.",
    "Companies like Microsoft envision using AI-powered infrastructure to accelerate massive-scale C++ to Rust rewrites, with a stated goal of eliminating all C/C++ from their codebase by 2030."
  ],
  "blind_spots": [
    "The analysis lacks quantitative data on Rust adoption in industries like automotive safety certification (ISO 26262) or medical devices (IEC 62304), where formal verification and long-term support are critical, potentially overstating Rust's readiness in these domains.",
    "There is minimal discussion of Rust's ability to meet hard real-time constraints compared to C++ in embedded or aerospace systems, a key requirement where predictability trumps safety guarantees.",
    "The long-term sustainability of Rust's ecosystem, particularly around critical but niche libraries and compiler maintainership, is not addressed."
  ],
  "partial_coverage": [
    "The role of government and regulatory bodies (like CISA) in promoting memory-safe languages is mentioned, but the extent to which policy will mandate Rust adoption in defense, infrastructure, or regulated industries is not fully explored.",
    "The impact of rising AI-assisted code generation and its potential to lower the barrier for Rust adoption (e.g., translating C++ to safe Rust) is touched upon with Microsoft's AI efforts but lacks broader industry context."
  ],
  "responses": {
    "Response A": "Rust is poised to significantly displace C++ in systems programming over the next decade, becoming the dominant choice for new projects while coexisting with C++ in legacy maintenance.\n\n**Adoption Trends:** Adoption is accelerating rapidly among tech giants. Google reports that new Rust code in Android is now comparable in volume to new C++ and has led to over a 1000x reduction in memory safety vulnerability density. Microsoft has publicly stated a goal to eliminate every line of C/C++ from its codebase by 2030, leveraging AI to aid translation. Nearly half of all companies now use Rust in production, particularly in security-critical area
…[обрезано, всего 11231 симв]

======================================================================
## C3_cn_small  (panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - Rust and C++ will coexist in a hybrid ecosystem through 2035, with Rust gaining significant traction in new systems projects and C++ persisting in legacy systems.
  - Key structural barriers like legacy codebases, talent shortages, and ecosystem maturity will hinder Rust's complete displacement of C++.
  - Memory safety regulations and security-conscious industries (government, embedded) will accelerate Rust adoption.
**contradictions:** 
  - {"topic": "Current adoption rates in system programming", "stances": [{"model": "dev_to_srijanxi_assessment", "stance": "Rust has overtaken C in system programming adoption (1.47% vs 9.84%)"}, {"model": "cppcat_2025_analysis", "stance": "C maintains 70% embedded dominance while Rust grows to 4.7% of production systems"}]}
  - {"topic": "Future dominance in specialized domains", "stances": [{"model": "dev_to_srijanxi_assessment", "stance": "Rust displacing C++ in safety-critical sectors"}, {"model": "cppcat_2025_analysis", "stance": "C++ will remain dominant in aerospace/medical domains due to certification ecosystems"}]}
**unique_insights:** 
  - {"model": "z-ai/glm-4.7-flash", "insight": "AI tool adoption (ChatGPT 77%) and regulatory shifts are creating structural drivers for Rust beyond technical merits."}
  - {"model": "qwen/qwen3-32b", "insight": "Semiconductor vendors (ARM/Espressif) incrementally expanding Rust tooling support creates gradual migration pathways."}
**blind_spots:** 
  - Lack of global geographic adoption patterns and regional policy differences
  - Impact of AI-assisted development on language switching costs and velocity
  - Quantifiable migration rates and success metrics for hybrid codebases
  - Long-term stability guarantees in memory-safe compilers through 2035
  - Hidden technical debt from interop boundaries in production systems

### RAW PANEL RESPONSES (что панель реально сказала):

**[qwen/qwen3.6-27b]:**
Based on current adoption metrics, enterprise migration patterns, and industry projections, Rust will not completely displace C++ in the next 10 years. However, it will **significantly displace C++ as the default choice for new systems programming projects** and carve out a massive, co-equal domain of influence, particularly in infrastructure, operating systems, and security-critical applications.

Here is a detailed analysis of the transition through to 2035.

### 1. Adoption Trends: The Split Between "New" and "Legacy"
The landscape is bifurcating. While C++ remains dominant in total lines of code, the "mindshare" for *new* projects is shifting rapidly.

*   **Infrastructure & OS:** Rust has achieved "kernel-grade" adoption, becoming a first-class language in the Linux kernel (used for device drivers and core network stack components) and widely adopted by cloud giants (AWS Firecracker, Microsoft Azure).
*   **Embedded Systems:** In the highly conservative embedded industry, C still holds ~70% market share and C++ ~23%. However, Rust has been growing year-over-year (surpassing 4-5% in recent production stats) as semiconductor vendors (ARM, Espressif) begin providing native Rust toolchains.
*   **Government Mandates:** A major structural driver is regulation. Organizations like the U.S. CISA and the White House’s Office of the National Cyber Director (ONCD) have mandated "Secure by Design" architectures, effectively banning C/C++ for new critical infrastructure software and pushing the industry toward Memory Safe Languages (MSLs) like Rust.

### 2. Key Structural Barriers to Displacement
For Rust to "kill" C++ entirely, it must overcome insurmountable economic and structural inertia:

*   **The "Big Codebase" Problem:** Billions of lines of production C++ code exist in domains like finance, gaming, and aerospace. Full rewrites have a historically low success rate (approx. 30%) and cost exponential amounts. Instead of rewriting, companies use the "Strangler Fig" pattern—writing new components in Rust and bridging them to C++ via FFI (Foreign Function Interface).
*   **The Talent Vacuum:** C++ has a 40+ year head start, resulting in millions of senior engineers. Rust talent is scarcer and more expensive. For a team in High-Frequency Trading (HFT) or Game Engines, hiring a veteran who understands specific compiler optimizations (like GCC/Clang SIMD toolchains) is often more critical than the language itself.
*   **Ecosystem Maturity:** While Rust’s registry (crates.io) has over 140,000 libraries, specialized C++ ecosystems (Boost, Qt, OpenCV, Vulkan) are deeply entrenched. In domains requiring microsecond precision or massive matrix operations, C++ libraries are often still the only mature option.

### 3. Who Benefits Most from Switching?
The Return on Investment (ROI) for switching to Rust varies wildly depending on the use case:

*   **Security-Critical Startups (Greenfield Projects):** Teams writing from scratch benefit most. They avoid legacy integration costs and lock in memory safety (preventing buffer overflows, use-after-free, and data races) from day one.
*   **Cloud & Network Service Providers:** Organizations running high-volume services (like Discord or ClickHouse) benefit from Rust’s lower memory footprint and predictable performance. The reduction in "undefined behavior" bugs often saves millions in on-call engineering hours.
*   **IoT & Automotive Manufacturers:** With connected cars and devices constantly processing untrusted network input, Rust’s compile-time safety guarantees provide a massive advantage over C++'s rely-on-runtime behavior.
*   **Junior-to-Mid Level Teams:** Rust's strict borrow checker enforces a mental model that prevents complex concurrency bugs, making codebases easier to maintain compared to C++, where such bugs are notoriously difficult to debug.

### 4. The Realistic Landscape in 2035
By 2035, the industry will not be a monolith of Rust nor a monolith of C++. Instead, it will be defined by a high-functioning **hybrid ecosystem**:

*   **The Co-Existence Standard:** C++ will likely lose its "monopoly" but remain the dominant language in **legacy-heavy or hardware-specific domains** (e.g., AAA game engines, avionics, and HFT). Rust will likely overtake C++ as the primary language for **generic systems programming** (e.g., kernel modules, command-line tools, web servers, and browsers).
*   **C++26/29 Evolution:** C++ will not go quietly. The C++ standardization committee will likel
…[обрезано, всего 5568 симв]

**[z-ai/glm-4.7-flash]:**
I'll search for current information about Rust adoption trends, C++ market position, and expert predictions about the future of systems programming languages.```json
{
  "consensus": "Rust will significantly grow its market share in systems programming over the next decade but will not completely displace C++. The languages will coexist with Rust dominating new safety-critical systems while C++ remains entrenched in legacy infrastructure and performance-critical domains.",
  "contradictions": {
    "adoption_speed_vs_legacy_anchorage": "While Rust adoption rates are accelerating at 37% year-over-year in specific domains like cloud infrastructure (73% share in new projects) and systems programming (52% for new projects), C++ still controls 89% of performance-critical systems in Fortune 500 companies and maintains dominance in established domains like game development (84%) and HFT (94%).",
    "talent_shortage_vs_time_horizon": "The severe talent shortage (only 709,000 Rust developers as primary language vs 2.27 million total users) creates immediate market advantages, yet the steep learning curve suggests this shortage will gradually close over the 10-year timeframe, potentially compressing the adoption advantage.",
    "innovation_vs_stability": "Rust is cited as the 'most admired' programming language (72% admiration rate) and driving innovation in safety features, but C++ maintains structural advantages through 40+ years of ecosystem maturity, billions of lines of production code, and deeper industry penetration that Rust cannot match in the near term."
  },
  "unique_insights": {
    "domain_specific_momentum": "Rust is gaining particularly strong traction in specific high-value sectors including automotive (where Rust market is projected to grow from $428M in 2024 to $2.1B by 2033), government contracts requiring memory-safe languages, and AI infrastructure where deterministic performance matters at millisecond levels.",
    "gradual_acceptance_model": "The most practical approach isn't wholesale replacement but 'incremental adoption' - tools like cxx enable bidirectional interop, allowing companies to start with one Rust module at a time while maintaining existing C++ codebases. This model is already being used by major companies for gradual migration.",
    "intersectional_trends": "The convergence of AI tool adoption (77% of developers using ChatGPT), regulatory pressure for memory safety, and improved tooling is creating unique structural drivers that accelerate Rust adoption beyond previous language transitions."
  },
  "blind_spots": [
    "Geographic distribution patterns remain under-analyzed, particularly how different regions adopt these technologies differently.",
    "The long-term impact of AI-assisted programming on language selection and migration patterns is not fully explored.",
    "The relationship between development ecosystem maturity, compiler improvements, and adoption velocity needs deeper investigation."
  ],
  "partial_coverage": {
    "beneficiaries_most": "The analysis identifies several groups benefiting from Rust adoption: security-conscious organizations reducing CVE costs, companies seeking to modernize legacy systems, high-performance computing teams in AI and fintech, and developers commanding 15-20% salary premiums in systems-focused roles.",
    "adoption_patterns": "Current patterns show strongest growth in cloud infrastructure, backend services, embedded systems, and command-line tools, with Linux kernel adoption serving as a key institutional anchor."
  },
  "responses": {}
}
```

**[qwen/qwen3-32b]:**
ool_call>{
  "consensus": "A hybrid landscape is expected where Rust gradually gains traction in specific domains (security-critical, greenfield projects) while C++ maintains dominance in legacy systems, industries with strict certification requirements, and where full backward compatibility is crucial. Rust adoption will grow in embedded/IoT, automotive, and safety-critical applications, but displacement will remain partial. Hybrid approaches (Rust for new modules + existing C/C++) are projected to become standard practice.",
  "contradictions": [
    "The article from cppcat.com (2025) states C remains dominant at 70% while dev.to/srijan-xi (2025) claims Rust has overtaken C in system programming adoption rates",
    "JetBrains data (2025) shows Rust integrating with existing ecosystems rather than displacing them, conflicting with dev.to/srijan-xi's assertion of overtaking",
    "cppcat.com predicts C++ remaining significant until 2030 while dev.to/srijan-xi suggests Rust has already displaced C in system programming"
  ],
  "unique_insights": "1. Safety-critical domains (aerospace, medical devices) show stronger C++ retention due to certification ecosystems. 2. Semiconductor vendors are incrementally adding Rust tooling support (Espressif, ARM). 3. Modern C++ (C++20/23) is addressing Rust's key advantages with improved memory safety features.",
  "blind_spots": [
    "No data on actual migration rates from C/C++ to Rust in enterprise environments",
    "Limited discussion of interoperability challenges in existing C/C++ codebases",
    "No quantitative projections for Rust market share beyond 2025"
  ],
  "partial_coverage": [
    "Most analysis focuses on embedded/IoT specifically rather than systems programming broadly",
    "Discussion primarily centered on technical adoption drivers rather than business/organizational factors",
    "Lack of timeline-specific projections beyond 2030 despite 10-year question scope"
  ],
  "responses": [
    {
      "model": "cppcat_2025_analysis",
      "response": "C remains dominant in embedded systems with 70% market share. Rust grows to 4.7% of production embedded systems in 2025. Automotive/robotics and IoT are adopting Rust for safety-critical components. C++ maintains 23% share and will remain relevant through at least 2030. Hybrid approaches (Rust + C/C++) are becoming standard as semiconductors expand Rust support."
    },
    {
      "model": "jetbrains_2025_report",
      "response": "Rust is commonly integrated with existing ecosystems (Python, JS, C/C++). Majority of Rust projects use multiple languages. Adoption patterns show startups choosing Rust while legacy systems maintain C/C++. C++17/20/23 adoption is growing with 10% C++23 adoption in 2023. Over 50% of developers still using older compiler versions."
    },
    {
      "model": "rust_state_2025",
      "response": "Rust is increasingly a 'brownfield' language used alongside existing codebases. 34% of projects use Rust with other languages (primarily JS/TS/Python). 33% of Rust projects use it standalone. Core systems programming remains central to Rust's identity with growth in backend/infrastructure."
    },
    {
      "model": "dev_to_srijanxi_assessment",
      "response": "Rust has overtaken C in system programming adoption (1.47% vs 9.84%). Government endorsements and security initiatives drive adoption. Safety-critical displacements are occurring with Rust's memory safety model. Projected to become 'de facto standard' for next-gen systems."
    },
    {
      "model": "tnewstack_comparison",
      "response": "Rust is becoming default for new safety-focused projects but C++ remains dominant in gaming/embedded/finance. Hybrid approaches (C++ legacy + Rust new components) are most practical. Both languages will coexist with teams leveraging each's strengths."
    }
  ]
}