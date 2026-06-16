# fac-08 — Fast inverse square root — actual author
**Block:** factual  |  **difficulty:** hard

**Prompt:**
The fast inverse square root algorithm (featuring the magic constant 0x5F3759DF) became famous through Quake III Arena (1999). John Carmack is commonly credited as its author. Who actually devised the algorithm and the magic constant? How was the true authorship established?

**Expected answer (эталон):**
Greg Walsh devised the algorithm and constant while at Ardent Computer in the late 1980s. The misconception about Carmack was widely spread until 2006, when Walsh himself contacted Beyond3D to confirm his authorship after speculation went viral on Slashdot.

---
## FUSION-конфиги (judge-анализ; responses вынесены в resp_*.md)

### C1_west_closed
_западный закрытый фронтир_  
panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2 | cost=$0.4066 | 243.5s | ptok=23844 ctok=5028 | retries=1

**consensus:**
  - John Carmack did not devise the Quake III fast inverse square root routine; he explicitly denied authorship in an email (26 Apr 2004) reproduced by Beyond3D.
  - Rys Sommefeldt’s Beyond3D investigation (Part I + follow-up Part II, 2006; updated 2007) is the key public record used to establish provenance of the Quake III snippet and its constant 0x5F3759DF.
  - Greg Walsh (Ardent Computer, late 1980s) is identified as the author who engineered the fast 1/sqrt(x) implementation associated with the Quake III code, including the famous constant 0x5F3759DF; Cleve Moler is credited as the inspiration/seed for the idea (Beyond3D Part II).
  - Authorship was “resolved” publicly when the Beyond3D Part I article drew wide attention (notably via Slashdot), prompting Greg Walsh to contact Beyond3D and “own up” as the author (Beyond3D Part II).
  - Gary Tarolli is part of the later lineage: he recognized the code, stated he could not take credit for originating it, recalled re-deriving it and testing/simulating the hex constant, and described possible tweaking/usage in earlier work (email quoted in Beyond3D Part I).

**contradictions:**
  - {"topic": "Who devised the fast inverse square root algorithm and magic constant used in the Quake III code?", "stances": [{"model": "openai/gpt-5.2", "stance": "Greg Walsh devised the routine and the specific constant 0x5F3759DF at Ardent (late 1980s), with Cleve Moler as inspiration."}, {"model": "google/gemini-3.1-pro-preview (Model_A/Model_C + consensus)", "stance": "Greg Walsh at Ardent devised the algorithm and constant; Carmack did not."}, {"model": "x-ai/grok-4.3", "stance": "Greg Walsh originated the algorithm at Ardent, inspired by Cleve Moler; later passed through 3dfx/others to id."}, {"model": "google/gemini-3.1-pro-preview (Model_B)", "stance": "Gary Tarolli was the true author (at SGI/3dfx)."}, {"model": "evidence", "stance": "Beyond3D Part II explicitly names Greg Walsh as the author who came forward after Slashdot exposure; Tarolli’s quoted email in Beyond3D Part I disclaims full credit and frames his role as later use/tweaking."}]}
  - {"topic": "How definitively the transmission chain to id Software is established (Ardent → SGI/3dfx → id)", "stances": [{"model": "openai/gpt-5.2", "stance": "Presents a plausible lineage Ardent → SGI/3dfx (Tarolli) → id (possibly via Brian Hook), but notes it is not proven with definitive commit history."}, {"model": "google/gemini-3.1-pro-preview", "stance": "States a fairly specific chain (Walsh → Tarolli → Brian Hook → Carmack/id), implying stronger certainty."}, {"model": "x-ai/grok-4.3", "stance": "Says it passed through 3dfx (Tarolli) to id, without claiming a fully proven step-by-step chain."}, {"model": "evidence", "stance": "Beyond3D Part II says the 3dfx → id linkage is traceable “via Brian Hook at the very least” but presents this as reasoning/inference, not a documented end-to-end artifact trail."}]}

**unique_insights:**
  - {"model": "google/gemini-3.1-pro-preview", "insight": "Connects the ‘magic constant’ trick to an approximation of logarithms via IEEE-754 bit structure (a conceptual explanation of why the integer subtraction/shift approximates 1/sqrt)."}

**blind_spots:**
  - No model squarely addresses the evidentiary standard: Beyond3D’s resolution heavily depends on retrospective testimony (Walsh coming forward) and emails, with no contemporaneous Ardent source/dated artifact shown publicly for the exact constant 0x5F3759DF.
  - No model cleanly distinguishes (a) invention of the general method (bit-level initial guess + Newton iteration) from (b) selection of the specific constant 0x5F3759DF used in Quake; Tarolli’s email implies he may have simulated/tweaked the constant, leaving open whether the Quake constant is exactly Walsh’s original or a later tuned variant.
  - No model evaluates alternative later claims/ambiguities about Cleve Moler’s contribution beyond ‘inspiration’ (e.g., whether some accounts conflate Moler’s role in transmitting/deriving the idea with authorship of the hack).
  - No model provides a clear timeline with dated milestones (Ardent late 1980s; Carmack email 2004; Quake III source release 2005; Beyond3D Part I/II 2006) to show how the public attribution shifted and when key evidence surfaced.
  - No model discusses the limits of the inferred transmission path into id Software (e.g., what would count as strong corroboration: internal source history, specific codebase sightings outside Quake, or independent witnesses), despite making fairly specific chain claims.

**partial_coverage:**
  - {"models": ["google/gemini-3.1-pro-preview", "x-ai/grok-4.3"], "point": "Chris Lomont’s 2003 analysis and his proposed alternative constant 0x5F375A86 (and that Lomont did not establish original authorship)."}
  - {"models": ["openai/gpt-5.2", "google/gemini-3.1-pro-preview"], "point": "Explicit mention of Brian Hook as a likely conduit from 3dfx to id Software (reflecting Beyond3D Part II’s suggestion)."}
  - {"models": ["openai/gpt-5.2", "x-ai/grok-4.3"], "point": "Walsh also implemented a related 1/cuberoot(x) method in the same Ardent/Titan context (from Beyond3D Part II)."}
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "Describes the algorithm’s structure as bit-level initial approximation followed by Newton–Raphson refinement, tying it to vector normalization use-cases."}
  - {"models": ["google/gemini-3.1-pro-preview", "openai/gpt-5.2"], "point": "Mentions earlier antecedents (e.g., Kahan/Ng floating-point bit tricks) as precursors/influence rather than origin of the Quake III snippet."}

### C2_cn_open
_открытый китайский фронтир (умн+умн)_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507 | cost=$0.1036 | 195.5s | ptok=19876 ctok=4000 | retries=0

**consensus:**
  - The fast inverse square root algorithm and the magic constant 0x5F3759DF were devised by Greg Walsh in the late 1980s while he was working at Ardent Computer on the Titan graphics minicomputer.
  - Walsh was inspired by Cleve Moler, who was investigating Newton-Raphson iteration techniques and had learned the underlying idea from an unpublished 1986 paper by William Kahan and K.C. Ng at UC Berkeley.
  - The algorithm reached Quake III Arena via a chain that includes Gary Tarolli, who encountered it while consulting for Kubota (Ardent's funder), likely brought it to 3dfx, and from there it entered id Software, possibly through Brian Hook.
  - The true authorship was established in 2006 through investigative journalism by Rys Sommefeldt published on Beyond3D, which initially traced the code to Gary Tarolli before Greg Walsh came forward after the article was widely publicized on Slashdot.
  - John Carmack denied authorship when asked and did not create the algorithm.

**contradictions:**
  - {"topic": "Origin of the magic constant 0x5F3759DF", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "The constant may have been refined by multiple hands; Gary Tarolli may have tweaked it, and it is unclear if 0x5F3759DF is Walsh's original or a later variant."}, {"model": "z-ai/glm-5.1", "stance": "Greg Walsh devised the constant; its exact derivation method is unknown, but it is definitively part of his original work."}, {"model": "moonshotai/kimi-k2.6", "stance": "The constant is part of Walsh's original work for the Titan, though its precise derivation is not perfectly documented."}]}

**unique_insights:**
  - {"model": "deepseek/deepseek-v4-pro", "insight": "Walsh and Tarolli later worked together at Accel Graphics, creating a direct professional link beyond the algorithm’s transmission path."}

**blind_spots:**
  - No model addresses whether Greg Walsh’s original implementation included the exact same Newton-Raphson refinement step used in the Quake III code or if that was added later.
  - None of the models discuss documented evidence of how Kahan and Ng’s 1986 paper influenced Cleve Moler beyond informal transmission, such as correspondence or notes.
  - There is no mention of whether the algorithm appeared in any software or publications between Walsh’s implementation at Ardent and its appearance in the Quake III codebase, leaving a potential gap in dissemination history.
  - The role of Kubota in potentially transferring or modifying the algorithm during Tarolli’s consultancy is not investigated by any model.
  - No model references whether Walsh’s own comments included any explanation of how he derived 0x5F3759DF mathematically, or whether it involved empirical tuning versus analytical methods.

**partial_coverage:**
  - {"models": ["deepseek/deepseek-v4-pro"], "point": "Walsh also wrote a fast cube root function using similar methods for the Titan, indicating broader algorithmic work in approximate inverses."}
  - {"models": ["deepseek/deepseek-v4-pro", "z-ai/glm-5.1"], "point": "Gary Tarolli acknowledged using and possibly tweaking the constant, but declined full credit."}
  - {"models": ["moonshotai/kimi-k2.6"], "point": "The full journey from Tarolli to id Software specifically involved Brian Hook, who brought it from 3dfx."}

### C5_smartpanel_dumbjudge
_умная панель + глупый судья_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b | cost=$0.1162 | 146.5s | ptok=17080 ctok=1850 | retries=0

**consensus:**
  The fast inverse square root algorithm with the magic constant 0x5F3759DF was authored by Greg Walsh in the late 1980s, with foundational inspiration from Cleve Moler and antecedent work by William Kahan and K.C. Ng. John Carmack, though popularly credited, did not write it.

**contradictions:**
  - Initial online speculation (2002–2005) commonly attributed the algorithm to John Carmack because it appeared in the Quake III Arena source code; Carmack himself denied writing it.
  - Early investigations (including Chris Lomont's 2003 paper and Rys Sommefeldt's original Beyond3D article in 2006) pointed to Gary Tarolli as a possible author—based on his role at 3dfx and his known use of the code—before the actual author came forward.
  - Some sources treat the algorithm as an evolutionary piece of code passed through multiple programmers' hands, implying no single author, but the historical record later pinpointed Walsh as the originator of the specific constant and function.

**unique_insights:**
  - Greg Walsh developed the algorithm while working at Ardent Computer on the Titan graphics minicomputer, which was struggling to meet performance targets; the fast inverse square root was created to accelerate software that could not use the vector hardware.
  - Cleve Moler (founder of MathWorks and creator of MATLAB) was the immediate catalyst: he introduced Walsh to the idea of using Newton-Raphson iteration for approximation, and this interaction at Ardent in the late 1980s seeded the eventual code.
  - The intellectual lineage goes deeper than Walsh and Moler: William Kahan and K.C. Ng at UC Berkeley wrote an unpublished paper in May 1986 describing how to compute square roots using bit-manipulation followed by Newton iterations, which was the conceptual ancestor of the fast inverse square root. This paper circulated among researchers and was preserved as a comment in the fdlibm math library distributed via Netlib from 1993.
  - The same era and environment produced a sibling algorithm: Greg Walsh also wrote a fast 1/cuberoot(x) function for the Titan using similar methods.
  - The path from Ardent to id Software ran through Gary Tarolli (consulting for Kubota, which funded Ardent), who brought the algorithm to 3dfx Interactive around 1994, and from there it likely entered id Software via Brian Hook, landing in the Quake III engine.
  - An independent parallel development occurred: Jim Blinn published a general approximation of the inverse square root in a 1997 'Floating Point Tricks' column in IEEE Computer Graphics & Applications, and a variation of the algorithm was found in Activision's 1997 game Interstate '76, showing the technique was in wider circulation before Quake III made it famous.

**blind_spots:**
  - The exact method by which Greg Walsh arrived at the specific magic constant 0x5F3759DF is not fully documented; Chris Lomont's 2003 analysis suggests it was a tuned compromise, but whether Walsh derived it analytically or through trial-and-error experimentation remains unconfirmed.
  - The precise hand-off chain from 3dfx to id Software is partially based on inference ('you can trace 3dfx to id Software via Brian Hook at the very least'), so the exact moment and manner the code entered the Quake III codebase is not recorded in definitive written evidence.
  - The Kahan-Ng 1986 paper remains formally unpublished; our knowledge of it comes from code comments in fdlibm and secondary references, meaning its full content and any further unpublished details about the method's early development are lost or inaccessible.

**partial_coverage:**
  While the origin story is now well-established in enthusiast and historical programming literature—particularly through Beyond3D's two-part investigation and the updated Wikipedia article—the primary sources are a combination of personal communications (Greg Walsh emailing Beyond3D, Cleve Moler commenting on his own blog) and the fdlibm code comment. There is no formal peer-reviewed history paper or corporate archive that exhaustively documents every link in the chain. Nonetheless, the convergence of these independent sources provides a coherent and widely accepted account.

### C5inv_dumbpanel_smartjudge
_глупая панель + умный судья (qwen-2.5-7b → gemma-3-12b-it)_  
panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1 | cost=$0.1163 | 267.5s | ptok=17560 ctok=3463 | retries=0

**consensus:**
  - John Carmack did not author the fast inverse square root algorithm; his use of it in Quake III Arena popularized it and led to the common misattribution.
  - Cleve Moler played an inspirational role in the algorithm's creation, sharing the concept of using Newton-Raphson iteration and bit manipulation with the actual author.
  - Gary Tarolli contributed to the algorithm's spread through his work at 3dfx after encountering it via the Ardent/Kubota connection.
  - The algorithm and magic constant predate Quake III Arena (1999) by years.

**contradictions:**
  - {"topic": "Primary authorship of the algorithm and magic constant", "stances": [{"model": "qwen/qwen3-8b", "stance": "Greg Walsh, with contributions from Cleve Moler and refinement by others"}, {"model": "google/gemma-3-12b-it", "stance": "Walter Fendt, a German physicist who published a paper in 1997"}, {"model": "z-ai/glm-4.7-flash", "stance": "Greg Walsh, inspired by coworker Cleve Moler at Ardent Computer"}, {"model": "evidence", "stance": "Greg Walsh is the confirmed author; Walter Fendt is a German physics educator who creates Java applets and has no connection to this algorithm whatsoever — Gemma's attribution is a complete hallucination"}]}
  - {"topic": "How true authorship was established", "stances": [{"model": "qwen/qwen3-8b", "stance": "Established through Chris Lomont's 2003 paper and historical tracing of code evolution"}, {"model": "google/gemma-3-12b-it", "stance": "Established through discovery of Walter Fendt's original 1997 paper"}, {"model": "z-ai/glm-4.7-flash", "stance": "Established through Rys Sommefeldt's Beyond3D investigation (2006), which gained Slashdot exposure, prompting Greg Walsh to personally email the team and confirm authorship"}, {"model": "evidence", "stance": "Beyond3D investigation and Walsh's personal confirmation is correct; Lomont's 2003 paper analyzed the mathematics but explicitly stated he could not confirm authorship; Fendt's 1997 paper does not exist in this context"}]}
  - {"topic": "Time period of Walsh's work at Ardent", "stances": [{"model": "qwen/qwen3-8b", "stance": "1990s"}, {"model": "z-ai/glm-4.7-flash", "stance": "Early 1990s"}, {"model": "evidence", "stance": "Late 1980s — Ardent Computer was active in the late 1980s, and Walsh's work on the Titan minicomputer dates to that period"}]}

**unique_insights:**
  - {"model": "z-ai/glm-4.7-flash", "insight": "Greg Walsh also wrote a fast 1/cuberoot(x) function for the Titan using similar but more complex methods during the same period at Ardent"}
  - {"model": "qwen/qwen3-8b", "insight": "Michael Abrash was mooted as a possible author due to his role as x86 assembly optimizer at id Software during Quake's development, though this was incorrect"}

**blind_spots:**
  - No model mentions William Kahan and K.C. Ng's unpublished 1986 Berkeley paper on bit-fiddling square root techniques, which was the earliest known origin that Cleve Moler learned from and passed to Walsh
  - No model addresses whether the magic constant 0x5F3759DF was derived mathematically or found by trial and error — this remains genuinely unresolved even after Walsh's confirmation
  - No model mentions the algorithm's obsolescence due to hardware rsqrtss SSE instructions introduced circa 1999, which are both faster and more accurate
  - No model discusses the 64-bit double-precision magic constant (0x5FE6EB50C7B537A9, later corrected by Matthew Robertson from Lomont's initial value) or extension to other floating-point formats
  - No model mentions early Usenet/forum appearances of the code in 2000-2002 (e.g., comp.graphics.algorithms, CS

**partial_coverage:**
  - {"models": ["qwen/qwen3-8b"], "point": "Chris Lomont's 2003 paper mathematically analyzed the constant and found a slightly better alternative (0x5f375a86), though the original performed better after Newton iterations"}
  - {"models": ["qwen/qwen3-8b"], "point": "James F. Blinn's 1997 'Floating-Point Tricks' paper contained a more general predecessor method for approximating log2(x) and x^n"}
  - {"models": ["z-ai/glm-4.7-flash"], "point": "The specific transmission chain: Ardent Computer → Gary Tarolli (consulting at Kubota) → 3dfx Interactive → id Software via Brian Hook"}
  - {"models": ["z-ai/glm-4.7-flash"], "point": "Greg Walsh personally emailed the Beyond3D team to confirm his authorship after their investigation gained exposure through Slashdot"}

### C6_echo
_контроль: эхо-камера_  
panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507 | cost=$0.0675 | 431.0s | ptok=55472 ctok=5182 | retries=0

**consensus:**
  - The fast inverse square root algorithm and the magic constant 0x5f3759df were not created by John Carmack, despite its appearance in Quake III Arena.
  - The algorithm originated from earlier work at Ardent Computer in the mid-1980s, with Greg Walsh as the primary implementer.
  - Cleve Moler provided the initial inspiration for the algorithm by exploring numerical approximation methods, including the Newton-Raphson technique, during his time at Ardent.
  - Gary Tarolli encountered the algorithm independently, possibly during work at SGI or for Kubota, and may have tweaked the constant before it spread to 3dfx and eventually id Software.
  - The true authorship was established through investigative journalism by Rys Sommefeldt (Ryszard) of Beyond3D in 2006, involving direct email correspondence with Carmack, Terje Mathisen, and Gary Tarolli, which led to Greg Walsh coming forward as the original author.

**contradictions:**
  - {"topic": "Role of Jim Blinn in the origin of the algorithm", "stances": [{"model": "evidence", "stance": "Jim Blinn described a related approximation method in a 1997 IEEE paper, but did not invent the specific algorithm or constant 0x5f3759df; the algorithm predates his publication and originated at Ardent in the 1980s."}]}

**unique_insights:**
  - {"model": "qwen/qwen3-235b-a22b-2507", "insight": "The magic constant 0x5f3759df is not arbitrary but results from a deliberate calculation involving the exponent bias, mantissa scaling, and a chosen sigma value (approximately 0.0450465) to optimize logarithmic approximation, later confirmed through mathematical derivation by researchers like Chris Lomont and McEniry."}

**blind_spots:**
  - The exact process Greg Walsh used to derive the constant 0x5f3759df—whether through analytical derivation, empirical testing, or a combination—remains unverified by direct documentation or first-hand account.
  - There is no explicit confirmation from Cleve Moler or Greg Walsh in the available sources detailing the full technical lineage from Kahan and Ng’s 1986 work to the final implementation.
  - The influence of earlier MIT HAKMEM-style bit hacks on the algorithm’s design is suggested but not firmly established in the evidence.
  - The role of Brian Hook in transferring the algorithm from 3dfx to id Software is mentioned but lacks detailed corroboration or documentation.
  - The algorithm is now obsolete due to hardware support (e.g., x86 SSE rsqrtss), but this historical context is only briefly noted rather than integrated into the authorship narrative.

**partial_coverage:**
  - {"models": ["qwen/qwen3-235b-a22b-2507"], "point": "William Kahan and K.C. Ng at Berkeley developed an unpublished method in 1986 for computing square roots using bit manipulation and Newton iteration, which influenced Cleve Moler and thus the eventual development of the fast inverse square root."}
  - {"models": ["qwen/qwen3-235b-a22b-2507"], "point": "Chris Lomont later mathematically analyzed the magic constant in 2003, deriving slightly more optimal values (e.g., 0x5F375A86), but this was a retrospective optimization, not a contribution to the original authorship."}

### C3_cn_small
_всё мелкое_  
panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b | cost=$0.0585 | 364.7s | ptok=13912 ctok=2521 | retries=0

**consensus:**
  - Greg Walsh is the true author of the fast inverse square root algorithm and the magic constant 0x5F3759DF, as established by community investigations in 2006-2007.
  - The algorithm was first conceptualized in the late 1980s/early 1990s at Ardent Computer, not during Quake III's development.
  - John Carmack and Michael Abrash are commonly but incorrectly credited with the algorithm.

**contradictions:**
  - {"topic": "Initial attribution", "stances": [{"model": "qwen/qwen3.6-27b", "stance": "Wrongly attributed to Carmack due to Quake III's prominence"}, {"model": "z-ai/glm-4.7-flash", "stance": "Carmack and Abrash wrongly speculated as authors"}, {"model": "qwen/qwen3-32b", "stance": "Lack of documentation in Quake III codebase caused confusion"}]}
  - {"topic": "Provenance details", "stances": [{"model": "z-ai/glm-4.7-flash", "stance": "Includes Kahan and K.C. Ng's 1986 work as precursor"}, {"model": "qwen/qwen3-32b", "stance": "Focuses on Walsh-Moler direct collaboration"}]}

**unique_insights:**
  - {"model": "qwen/qwen3-32b", "insight": "Cleve Moler's tuition of Newton-Raphson adaptation for inverse square roots influenced the algorithm's conceptual origins."}
  - {"model": "qwen/qwen3.6-27b", "insight": "The algorithm's journey from Ardent Titan to 3dfx to id Software via Brian Hook is documented with specific intermediaries."}

**blind_spots:**
  - Mathematical derivation of the magic constant 0x5F3759DF (not focused on authorship but algorithm technicalities)
  - Post-2006 academic or archival documentation confirming or expanding the 2006-2007 conclusions
  - Lack of direct citation to Greg Walsh's public confirmation or primary sources from his communication

**partial_coverage:**
  - {"models": ["qwen/qwen3-32b", "z-ai/glm-4.7-flash"], "point": "Mentions William Kahan and K.C. Ng's 1986 paper as foundational for the algorithm's bit-level techniques"}
  - {"models": ["qwen/qwen3-32b"], "point": "Points to Wikipedia and academic analyses (like Ryszard Sommefeldt's thesis) as supplementary sources for the algorithm's lineage"}


---
## BASELINE (одиночная модель, без fusion)

### B_cn  (model=deepseek-v4-pro | cost=$0.0021 | 25.3s)
The fast inverse square root algorithm popularized by *Quake III Arena* is often misattributed to John Carmack, but he did not create it. The actual author is **Greg Walsh**, a programmer at **Ardent Computer**, who devised the implementation and the iconic magic constant `0x5F3759DF` in 1988.

### Who Actually Devised It?

- **Greg Walsh (Ardent Computer)** wrote the code while working on the Titan graphics supercomputer. He adapted an idea from **Cleve Moler** (the creator of MATLAB), who had used a similar bit‑trick on a Cray vector machine to compute an initial guess for inverse square root.
- Walsh tuned the “magic constant” empirically to maximize accuracy for the initial guess across the full floating‑point range of 32‑bit IEEE 754 numbers. The constant became `0x5F3759DF` (later refined by others to `0x5F375A86` for slightly better results).
- The core bit‑hack (`i = 0x5F3759DF - (i >> 1)`) combined with one iteration of Newton’s method produced the famously efficient approximation.

### How True Authorship Was Established

1. **Revelation by Greg Walsh (2006)** – In discussions on the *Beyond3D* forums, Walsh openly stated that he wrote the routine for the Ardent Titan. He explained the historical context and his derivation of the magic number, which matched the code later found in *Quake III*.
2. **Code Archaeology** – Enthusiasts traced the algorithm’s lineage backward. The exact sequence of operations and the same magic constant appeared in the Ardent Titan’s software (late 1980s), predating id Software’s use by over a decade.
3. **Research & Analysis** – Mathematician Chris Lomont investigated the algorithm, tested many possible constants, and wrote a detailed paper (2003) that confirmed the optimal constant was close to Walsh’s original. Lomont’s work sparked further debate, ultimately leading Walsh to come forward.
4. **Carmack’s Own Statement** – John Carmack himself clarified that he did not invent the trick; he encountered it in other codebases (likely from the demo‑scene or earlier graphics libraries) and included it in *Quake III* because it was fast and effective.

In summary, the fast inverse square root is a product of the high‑performance computing world of the 1980s. Greg Walsh was its primary author, building on Cleve Moler’s concept, and the constant was his hand‑tuned improvement. The algorithm’s true origin emerged through a combination of community forensic analysis and Walsh’s firsthand account.

### B_west  (model=gpt-5.2 | cost=$0.0211 | 37.4s)
_(пустой ответ)_
