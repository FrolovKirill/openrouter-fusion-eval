# fac-08 — Fast inverse square root — actual author  (raw panel responses + judge-синтез)
**Prompt:** The fast inverse square root algorithm (featuring the magic constant 0x5F3759DF) became famous through Quake III Arena (1999). John Carmack is commonly credited as its author. Who actually devised the algorithm and the magic constant? How was the true authorship established?

> ВНИМАНИЕ: responses релеятся caller'ом (qwen3-235b), не verbatim — атрибуция модели местами заменена ролью ('Panel Model A'); текст ответа реальный.


======================================================================
## C1_west_closed  (panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - John Carmack did not devise the Quake III fast inverse square root routine; he explicitly denied authorship in an email (26 Apr 2004) reproduced by Beyond3D.
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

### RAW PANEL RESPONSES (что панель реально сказала):

**[openai/gpt-5.2]:**
{
  "consensus": "The Quake III fast inverse square root routine (including the specific “magic constant” 0x5F3759DF) was devised by Greg Walsh (Ardent Computer, late 1980s), not by John Carmack. Cleve Moler (Ardent/MathWorks) provided key inspiration (Newton–Raphson-based approach and exposure to earlier bit-level sqrt ideas), while Gary Tarolli later used/modified/spread the code in the graphics industry (SGI/3dfx era), helping it reach id Software. Public misattribution to Carmack was corrected after Carmack explicitly denied authorship and Walsh later came forward publicly.",
  "contradictions": [
    "Popular lore credited John Carmack as the author because the code appeared in the Quake III source; Carmack himself denied writing it (and doubted Michael Abrash wrote it).",
    "Early speculation variously attributed authorship to Terje Mathisen or Gary Tarolli; both were connected to similar work or later refinements/usage, but neither claimed original authorship of the Quake III snippet.",
    "Some secondary narratives emphasize SGI/3dfx as the origin; the investigation evidence instead points to Ardent (late 1980s) as the place where the algorithm and constant were first engineered by Walsh (with Moler’s influence)."
  ],
  "unique_insights": [
    "The authorship trail was reconstructed as a ‘code lineage’ through multiple organizations: Ardent (Walsh/Moler) → (via industry reuse/consulting) SGI/3dfx (Tarolli) → id Software (Quake III), possibly via contacts such as Brian Hook (mentioned in the Beyond3D account).",
    "Beyond3D’s investigation initially ended at Gary Tarolli as the last well-known person likely to have ‘touched’ the code; widespread publicity (Slashdot effect) prompted the original author, Greg Walsh, to contact them and ‘own up’ to authorship.",
    "Carmack’s denial email was an early pivotal datapoint: he explicitly said ‘Not me’ and suggested Terje Mathison as a possibility, which helped redirect the search away from id Software.",
    "The constant’s exact derivation method remains historically murky in public accounts, but the established provenance credits Walsh with devising the now-famous constant used in the Quake-derived implementation, with Moler as the conceptual catalyst and earlier academic/engineering work (e.g., Kahan/Ng as later cited in summaries like Wikipedia) as antecedents."
  ],
  "blind_spots": [
    "No primary, dated source code artifact from Ardent showing the exact constant 0x5F3759DF in Walsh’s original implementation is included in the gathered material; the attribution rests on retrospective accounts and Walsh’s own claim as reported by Beyond3D.",
    "The precise process by which Walsh selected/tuned 0x5F3759DF (derivation vs. empirical tuning) is not fully documented in the retrieved sources; only the fact of Walsh’s authorship of the constant is asserted.",
    "The exact mechanism and person-by-person path by which the routine entered the Quake III codebase is suggested (e.g., via 3dfx → id) but not proven with a definitive commit history or contemporaneous internal documentation in the gathered material."
  ],
  "partial_coverage": [
    "Earlier precursors (e.g., unpublished Kahan/Ng 1986, Blinn 1997 floating-point tricks) are mentioned in some gathered sources, but the central question here—who devised the Quake-famous routine and constant, and how that was established—is primarily supported by the Beyond3D investigation and Carmack’s email denial.",
    "The role of Gary Tarolli is covered as ‘touched/tweaked/propagated’ rather than as originator; details of his specific changes (if any) to the constant are not pinned down in the retrieved excerpts."
  ],
  "responses": [
    {
      "model": "panel_1",
      "answer": "Greg Walsh devised the fast inverse square root routine and the 0x5F3759DF constant while at Ardent Computer in the late 1980s, working in the context of Ardent’s Titan graphics minicomputer performance efforts. Cleve Moler (his colleague at Ardent, later known for MATLAB/MathWorks) provided the seed idea—investigating Newton–Raphson iteration for approximations—leading Walsh to engineer a fast 1/sqrt(x) (and also 1/cuberoot(x)). The routine later passed through other hands in the graphics industry; Gary Tarolli used it and may have tweaked it, contributing to its spread (SGI/3dfx era), and it ultimately ended up in id Software’s Quake III code.\n\nTrue authorship was established by a public, documented investigation (Beyond3D, Rys So
…[обрезано, всего 6719 симв]

**[google/gemini-3.1-pro-preview]:**
{
  "consensus": "John Carmack is widely recognized for popularizing the fast inverse square root algorithm in Quake III Arena, but he did not invent it. True authorship is attributed to Greg Walsh, who developed it while working at Ardent Computer in the late 1980s, with inspiration from Cleve Moler and William Kahan. The authorship was established through an extensive community investigation, most notably by Rys Sommefeldt in 2006, who traced the code and its magic constant (0x5F3759DF) back through id Software, 3dfx, Silicon Graphics (SGI), and finally to Ardent Computer.",
  "contradictions": "One model places heavy attribution on Gary Tarolli for the algorithm's invention, while others correctly point out Tarolli only brought it to 3dfx and it existed earlier at Ardent. Additionally, there is slight confusion in one response regarding Chris Lomont's role; Lomont did a later mathematical analysis in 2003 (discovering a theoretically better constant, 0x5f375a86), but he was not involved in the original creation or the historical derivation.",
  "unique_insights": "The magic constant exploits the specific bit-wise representation of IEEE 754 floating-point numbers to perform a piecewise linear approximation of the logarithm. The precise history of transmission was: Greg Walsh (Ardent) -> Gary Tarolli (SGI/3dfx) -> Brian Hook (3dfx/id Software) -> John Carmack (Quake III). The algorithm was a vital optimization for early 3D graphics, which relied heavily on calculating vector normalizations.",
  "blind_spots": "The exact mathematical derivation used by Greg Walsh to arrive at the specific integer 0x5F3759DF remains slightly ambiguous. While it is known to minimize relative error for the initial guess, it is not perfectly known if Walsh derived the original constant purely analytically or if it was empirically adjusted through trial and error.",
  "partial_coverage": "Not all models explain the Newton-Raphson iteration that follows the bit-hack, which is essential to the algorithm's actual accuracy. The foundational role of William Kahan's earlier work on floating-point tricks (which laid the groundwork for Moler and Walsh) is mentioned briefly but not deeply explored.",
  "responses": [
    {
      "model": "Model_A",
      "response": "The fast inverse square root algorithm, famous for the constant 0x5f3759df, was popularized by Quake III Arena but not written by John Carmack. Carmack himself denied authorship. An investigation by Rys Sommefeldt revealed that Greg Walsh at Ardent Computer wrote the original algorithm. Walsh worked with Cleve Moler (creator of MATLAB) who provided the mathematical backing. Sommefeldt traced the code from Carmack to Brian Hook, then to Gary Tarolli at 3dfx and SGI, and finally back to Walsh at Ardent. The method shifts the bits of an IEEE 754 float to halve the exponent and subtracts it from the magic constant, followed by a Newton-Raphson iteration."
    },
    {
      "model": "Model_B",
      "response": "Although Quake III Arena made the 0x5f3759df constant famous, John Carmack didn't invent it. The true author was Gary Tarolli, who used it at 3dfx and SGI. Later investigations by Chris Lomont in 2003 mathematically analyzed the constant, proving how it approximates a logarithm, and Lomont actually found a slightly better constant: 0x5f375a86. The authorship was traced by asking developers in the graphics community until the line of transmission was established."
    },
    {
      "model": "Model_C",
      "response": "The fast invSqrt algorithm's true author is Greg Walsh. When Rys Sommefeldt investigated its origins in 2006, he followed the trail of the code. Carmack pointed to Terje Mathisen or Brian Hook. Hook pointed to Gary Tarolli. Tarolli pointed to his time at Silicon Graphics (SGI) and Ardent. Eventually, Cleve Moler confirmed that Greg Walsh at Ardent Computer devised the constant and the algorithm. The algorithm works by treating the bits of a floating-point number as an integer, mathematically approximating the exponent halving required for a square root, utilizing the magic constant 0x5f3759df to minimize the error before making one pass of Newton's method."
    }
  ]
}

**[x-ai/grok-4.3]:**
{
  "consensus": "The fast inverse square root (with constant 0x5F3759DF) was not created by John Carmack. It originated in the late 1980s at Ardent Computer, devised by Greg Walsh (with inspiration from Cleve Moler). The code later passed through 3dfx (Gary Tarolli) and reached id Software.",
  "contradictions": "Early attributions credited Carmack (due to Quake III source) or speculated Michael Abrash/Terje Mathisen/Gary Tarolli. Carmack explicitly denied authorship. Some papers initially concluded the author was unknown or that it evolved incrementally.",
  "unique_insights": "Beyond3D investigation traced the lineage; after Slashdot publicity, Greg Walsh personally claimed authorship, detailing its creation at Ardent for the Titan minicomputer (also noting a related cube-root implementation). Walsh credited Cleve Moler’s Newton-Raphson work as the seed idea.",
  "blind_spots": "Exact derivation steps for choosing 0x5F3759DF remain undocumented by Walsh; multiple independent rediscoveries or refinements likely occurred before Quake III. Endian-neutrality and precise error bounds were analyzed only later (Lomont et al.).",
  "partial_coverage": "Pre-2006 sources stop at “unknown author” or list suspects; post-Beyond3D coverage consistently identifies Walsh but rarely provides primary source code from Ardent.",
  "responses": [
    {
      "model": "Beyond3D Part 2",
      "answer": "Greg Walsh devised the algorithm at Ardent Computer (working with Cleve Moler). After the original Beyond3D article was Slashdotted he publicly identified himself as the author."
    },
    {
      "model": "Beyond3D Part 1 / McEniry",
      "answer": "Traces the chain Carmack → Abrash → Mathisen → Tarolli, leaving the true originator open until Walsh’s later confirmation."
    },
    {
      "model": "Lomont / Robertson thesis",
      "answer": "Notes that the author was unknown at the time of writing; discusses possible influence from Blinn’s floating-point tricks but does not identify Walsh."
    }
  ]
}

======================================================================
## C2_cn_open  (panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - The fast inverse square root algorithm and the magic constant 0x5F3759DF were devised by Greg Walsh in the late 1980s while he was working at Ardent Computer on the Titan graphics minicomputer.
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

### RAW PANEL RESPONSES (что панель реально сказала):

**[deepseek/deepseek-v4-pro]:**
```json
{
  "consensus": "The fast inverse square root algorithm was authored by Greg Walsh in the late 1980s while working at Ardent Computer, inspired by Cleve Moler (who had learned the underlying idea from an unpublished 1986 paper by William Kahan and K.C. Ng at Berkeley). It was not created by John Carmack or anyone at id Software; it was inherited via Gary Tarolli, who had consulted for Kubota (Ardent's funder) and later brought it to 3dfx, from where it entered id Software (likely via Brian Hook).",
  "contradictions": "The specific magic constant 0x5F3759DF may have been refined by multiple hands (e.g., Gary Tarolli mentioned possibly tweaking the hex constant). Chris Lomont later found 0x5F375A86 to be more optimal, suggesting the constant in the Quake III code may not be the original Walsh constant but one that evolved. John Carmack's email speculating Terje Matheson (Mathisen) as the author was incorrect. Some early sources and online forums initially attributed the code to Carmack, Michael Abrash, or Gary Tarolli, all of whom denied full authorship.",
  "unique_insights": [
    "Greg Walsh engineered the fast 1/sqrt(x) specifically to help Ardent's Titan graphics minicomputer meet performance claims when software could not utilize vector hardware.",
    "Cleve Moler (founder of MathWorks and author of MATLAB) was investigating Newton-Raphson iteration for approximation and provided the seed idea.",
    "The ultimate origin traces back to an unpublished 1986 paper by William Kahan and K.C. Ng at Berkeley on the technique for sqrt(x).",
    "Walsh came forward to claim authorship only after the 2006 Beyond3D article received massive exposure via Slashdot; without that publicity, the true author might have remained unknown.",
    "Gary Tarolli independently encountered and possibly modified the code at SGI or Kubota, creating a parallel thread of usage."
  ],
  "blind_spots": [
    "The exact mathematical derivation method Walsh used to arrive at 0x5F3759DF is not fully documented; we know the general Newton-Raphson/logarithmic approach but not his specific tuning process.",
    "Whether Walsh's original constant was exactly 0x5F3759DF or something slightly different that Tarolli modified is not conclusively established.",
    "The route the code took from Tarolli's possession into the Quake III source is not fully traced step by step (Brian Hook is mentioned as the likely conduit).",
    "The 1986 Kahan and Ng paper remains unpublished, so the full extent of their contribution versus Moler's and Walsh's is not publicly available.",
    "There is no direct statement from Walsh about how he felt about Carmack getting the credit for years, or why he waited until 2006 to come forward."
  ],
  "partial_coverage": "The historical narrative covers Walsh's creation and the chain of custody to Quake III, but lacks detailed technical documentation from Walsh himself about his design process, and does not fully resolve whether 0x5F3759DF is Walsh's original constant or Tarolli's variant.",
  "responses": {
    "panel_1": "The fast inverse square root algorithm was created by Greg Walsh in the late 1980s while he was working at Ardent Computer on the Titan graphics minicomputer. He was inspired by Cleve Moler, who had been investigating Newton-Raphson iteration techniques and had learned of the underlying idea from an unpublished 1986 paper by William Kahan and K.C. Ng at UC Berkeley. The algorithm later reached id Software via Gary Tarolli, who had encountered it while consulting for Kubota (Ardent's funder) and subsequently used it at 3dfx. True authorship was established through a 2006 investigation by Rys Sommefeldt for Beyond3D, published in two parts. The investigation first traced the code through John Carmack, Michael Abrash, Terje Mathisen, and Gary Tarolli—all of whom denied authorship. After the first article was widely publicized via Slashdot, Greg Walsh came forward and claimed the work, providing the historical context of its creation at Ardent. This was published in the second Beyond3D article, definitively establishing Walsh as the author and Cleve Moler as the inspiration.",
    "panel_2": "The author is Greg Walsh, who devised the algorithm in the late 1980s while at Ardent Computer, working with Cleve Moler. The magic constant 0x5F3759DF and the fast inverse square root method were created to improve performance on Ardent's Titan minicomputer when vector hardware couldn't be used. The true authorshi
…[обрезано, всего 6163 симв]

**[z-ai/glm-5.1]:**
## The True Author of the Fast Inverse Square Root

### Who Devised It

The algorithm and the magic constant **0x5F3759DF** were devised by **Greg Walsh** in the late 1980s while he was working at **Ardent Computer** on the Titan graphics minicomputer.

The lineage of the idea is as follows:

1. **William Kahan and K.C. Ng** at UC Berkeley wrote an unpublished paper in **May 1986** describing how to calculate the square root using bit-fiddling techniques followed by Newton-Raphson iterations. This was the mathematical seed.

2. **Cleve Moler** (founder of MathWorks and creator of MATLAB) was working at Ardent and was investigating Newton-Raphson iteration for approximation. He learned of Kahan and Ng's technique and **passed the idea along to Greg Walsh**, his coworker.

3. **Greg Walsh** then devised the now-famous constant and the complete fast inverse square root algorithm to speed up software running on the Titan that couldn't utilize the vector hardware. He also wrote a fast cube root function using similar (but more complex) methods in the same period.

### How It Reached Quake III

The algorithm traveled through several hands before arriving at id Software:

- **Gary Tarolli** was consulting for **Kubota** (the company funding Ardent) at the same time and likely brought the algorithm to **3dfx Interactive** circa 1994. Tarolli acknowledged using the code and possibly tweaking the hex constant, but explicitly stated he could not take full credit for it.
- **Brian Hook** likely brought the algorithm from 3dfx to **id Software**, where it ended up in the Quake III Arena source code.

### How the True Authorship Was Established

The investigation unfolded over several years:

1. **2002–2003**: The code spread on Usenet, gamedev.net, and other forums. **Chris Lomont** at Purdue published a paper analyzing the mathematics and the constant, but could not determine the author—his paper ended with a plea to meet the original author.

2. **2004**: When asked directly, **John Carmack denied authorship** in an email, writing: *"Not me, and I don't think it is Michael. Terje Matheson perhaps?"* Michael Abrash was also ruled out.

3. **2005**: Computer scientist **Rys Sommefeldt** at Beyond3D conducted a systematic investigation, contacting prominent developers. The trail led through Carmack → Terje Mathison → **Gary Tarolli** (3dfx/NVIDIA). Tarolli acknowledged encountering and using the code but said he couldn't take full credit beyond possible tweaks to the constant.

4. **2006**: After Beyond3D published their initial findings and the article was picked up by **Slashdot** (giving it massive exposure), **Greg Walsh himself came forward**, contacting Beyond3D to identify himself as the original author. He explained the full history: Ardent's Titan minicomputer, the collaboration with Cleve Moler, and the derivation of the algorithm and constant.

This was documented in the Beyond3D follow-up article *"Origin of Quake3's Fast InvSqrt() — Part Two."* As the article concluded: *"We can rightfully name Cleve as the inspiration and Greg as the author."* However, exactly **how** Walsh derived the specific magic constant 0x5F3759DF remains unclear even today—whether by analytical derivation or by guided trial and error has never been definitively established.

**[moonshotai/kimi-k2.6]:**
The fast inverse square root algorithm was actually devised by **Greg Walsh** in the late 1980s, not by John Carmack.

### The True Author
Walsh developed the algorithm while working at **Ardent Computer** on the **Titan** graphics minicomputer. He wrote it to help software running on the Titan reach performance benchmarks when the code couldn't utilize the machine's vector hardware. At the time, Walsh was working alongside **Cleve Moler** (founder of MathWorks and creator of MATLAB). Moler had been investigating Newton-Raphson iteration for approximation and provided the conceptual "seed" for the hack; according to some accounts, Moler had seen a related idea in earlier work by Velvel Kahan and K. C. Ng at Berkeley in 1986. Walsh took that inspiration, implemented the fast `1/sqrt(x)` approximation, and also wrote a similar one for the cube root.

### How It Reached Quake III
From Ardent, the algorithm came to the attention of **Gary Tarolli**, who was consulting for Kubota (Ardent's funder) and later founded 3dfx. Tarolli used and tweaked it, and through the graphics programming community—connections like Brian Hook at 3dfx—it eventually made its way into id Software's codebase.

### How the Authorship Was Established
For years, the algorithm was widely attributed to John Carmack because it appeared in the Quake III Arena source code. In 2005, Carmack explicitly denied authorship via email when asked.

The true origin was uncovered in a two-part investigation published by **Beyond3D** (written by Rys Sommefeldt) in **2006 and 2007**. The first article traced the code's path through Carmack, Michael Abrash, Terje Mathisen, and finally Gary Tarolli. After that article was widely circulated (including on Slashdot), **Greg Walsh himself came forward** and contacted Beyond3D to confirm he was the original author. This was corroborated by Cleve Moler, who verified that Walsh had written the routine at Ardent.

### The Magic Constant
While Greg Walsh is credited with the algorithm and the specific implementation, the exact pencil-and-paper derivation of the constant **0x5F3759DF** is not perfectly documented; its precise origin is sometimes described as having been lost in the shuffle of the era. However, it is definitively part of Walsh's original work for the Titan, predating Quake III by over a decade. (Later analysis by Chris Lomont in 2003 mathematically explained why the constant works and even derived a slightly more accurate alternative, but the original value came from Walsh.)

======================================================================
## C5_smartpanel_dumbjudge  (panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   The fast inverse square root algorithm with the magic constant 0x5F3759DF was authored by Greg Walsh in the late 1980s, with foundational inspiration from Cleve Moler and antecedent work by William Kahan and K.C. Ng. John Carmack, though popularly credited, did not write it.
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

### RAW PANEL RESPONSES (что панель реально сказала):

**[Panel Model A]:**
The fast inverse square root algorithm and the magic constant 0x5F3759DF were devised by Greg Walsh in the late 1980s while he was working at Ardent Computer. The idea was sparked by Cleve Moler, who introduced Walsh to the concept of using Newton-Raphson iteration for approximations. The underlying bit-manipulation approach traces back to an unpublished 1986 paper by William Kahan and K.C. Ng at UC Berkeley. The true authorship was established in 2006 when Greg Walsh contacted Rys Sommefeldt at Beyond3D after the original investigative article—which had tentatively credited Gary Tarolli—gained wide exposure on Slashdot.

**[Panel Model B]:**
Greg Walsh is the confirmed original author of the Quake III fast inverse square root algorithm (including the 0x5F3759DF constant). He created it while at Ardent Computer to improve the performance of the Titan graphics minicomputer. The discovery of his authorship happened when Beyond3D published 'Origin of Quake3's Fast InvSqrt()' in November 2006; the article went viral on Slashdot, and Walsh saw it and emailed the author, Rys Sommefeldt, to set the record straight. Before Walsh came forward, the code had been variously attributed to John Carmack, Michael Abrash, Terje Mathisen, and Gary Tarolli. The investigation also reveals that the technique was independently developed in the 1986 Kahan-Ng unpublished paper and appeared in other contexts such as the fdlibm library and Jim Blinn's 1997 IEEE column.

**[Panel Model C]:**
The authorship of the fast inverse square root function is now solidly attributed to Greg Walsh, with the historical chain being: (1) William Kahan and K.C. Ng described bit-level square root methods with Newton iteration in an unpublished 1986 paper; (2) Cleve Moler learned of this approach and, while at Ardent Computer in the late 1980s, discussed it with coworker Greg Walsh; (3) Greg Walsh implemented the specific fast inverse square root algorithm with the 0x5F3759DF magic constant for the Ardent Titan; (4) Gary Tarolli, consulting for the funding company Kubota, interacted with Walsh and later carried the algorithm to 3dfx in the mid-1990s; (5) the code eventually reached id Software, most likely through Brian Hook, and became famous when the Quake III Arena source code was released in 2005. The definitive identification of Walsh as author resulted from a 2006 Beyond3D follow-up article after he came forward in response to the earlier speculation that had credited Tarolli.

======================================================================
## C5inv_dumbpanel_smartjudge  (panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - John Carmack did not author the fast inverse square root algorithm; his use of it in Quake III Arena popularized it and led to the common misattribution.
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

### RAW PANEL RESPONSES (что панель реально сказала):
_(responses отсутствуют для этого вопроса/конфига)_

======================================================================
## C6_echo  (panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - The fast inverse square root algorithm and the magic constant 0x5f3759df were not created by John Carmack, despite its appearance in Quake III Arena.
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

### RAW PANEL RESPONSES (что панель реально сказала):
_(responses отсутствуют для этого вопроса/конфига)_

======================================================================
## C3_cn_small  (panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - Greg Walsh is the true author of the fast inverse square root algorithm and the magic constant 0x5F3759DF, as established by community investigations in 2006-2007.
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

### RAW PANEL RESPONSES (что панель реально сказала):

**[qwen/qwen3.6-27b]:**
The true author of the fast inverse square root algorithm and its famous magic constant (`0x5F3759DF`) is **Greg Walsh**. He devised the hack around 1993 while working as a programmer at **Ardent Computer**. He was conceptually inspired by his colleague **Cleve Moler** (the founder of MATLAB), who was already investigating the use of Newton-Raphson iterations for mathematical approximations. Walsh engineered the specific IEEE 754 bit-manipulation implementation and derived the optimized magic constant to speed up software running on the Ardent Titan graphics minicomputer.

**How the algorithm reached Quake III:**
The code traveled through the graphics industry before landing in id Software's codebase:
* **Gary Tarolli**, who was consulting for Kubota (the company funding Ardent Computer), saw Walsh's code, recognized its utility, and made minor tweaks to it.
* Tarolli eventually brought the algorithm to **3dfx Interactive** around 1994.
* From 3dfx, the code was passed to id Software (likely via id programmer Brian Hook), where it was integrated into the *Quake III Arena* engine without attribution.

**How true authorship was established:**
For over a decade, the code was shrouded in mystery and incorrectly credited to *Quake* director John Carmack. The true origin was uncovered through a chain of public investigation:
1. **Source Code Release (2005):** When id Software released the full *Quake III Arena* source code, the function sparked massive online debate about its mathematical beauty and origins. Carmack himself quickly emailed forums to explicitly deny writing it.
2. **The Beyond3D Investigation (2006):** To solve the mystery, website Beyond3D published a two-part investigative article by Rys Sommefeldt. Through interviews and digital sleuthing, Sommefeldt traced the code's lineage through Carmack, Michael Abrash, and Tarolli, eventually narrowing the origin down to Cleve Moler and Greg Walsh at Ardent Computer.
3. **Slashdot & Direct Claim:** Sommefeldt's article was highlighted on the technology news aggregator **Slashdot**, generating massive exposure. The publicity was successful enough to prompt Greg Walsh to personally contact Beyond3D, where he stepped forward to claim authorship and confirm his role in writing the function for the Titan hardware.

This community-driven sleuth work permanently resolved the mystery, officially crediting Greg Walsh as the creator of one of the most famous mathematical hacks in computing history.

**[z-ai/glm-4.7-flash]:**
The Fast Inverse Square Root algorithm and the famous magic constant 0x5F3759DF were devised by **Greg Walsh** in the late 1980s while working at **Ardent Computer**.

The true authorship was established through a historical investigation by **Ryszard Sommefeldt**, published in two parts on Beyond3D in 2006 and 2007. Sommefeldt traced the code's lineage back to earlier graphics programming pioneers, revealing the following chain:

1.  **The Origin:** William Kahan and K.C. Ng wrote an unpublished paper in 1986 at Berkeley describing bit-fiddling techniques for square roots.
2.  **The Conduit:** Cleve Moler (founder of MathWorks and author of MATLAB), who was working at Ardent Computer with Walsh, encountered Kahan and Ng's work and passed the technique to his colleague Greg Walsh.
3.  **The Devise:** Greg Walsh devised the specific algorithm and the precise hex constant (0x5F3759DF) to make the approximation work accurately on the floating-point format of the time.
4.  **The Migration:** The algorithm eventually traveled from Ardent to **Gary Tarolli** (who was consulting for Ardent's funding company, Kubota and later founded 3dfx) to **3dfx Interactive**, and eventually to **id Software** via Brian Hook, where it appeared in the Quake III source code.

In late 2006, after the community's speculation regarding John Carmack or Michael Abrash, Greg Walsh contacted Ryszard Sommefeldt and confirmed his role as the original author.

**[qwen/qwen3-32b]:**
ool_call>{
  "consensus": "The fast inverse square root algorithm and the magic constant 0x5F3759DF were devised by **Greg Walsh** while working at Ardent Computer in the late 1980s/early 1990s. This contradicts the common attribution to John Carmack or Michael Abrash. The true authorship was established when **Greg Walsh revealed himself** via a comment on Beyond3D’s forums in 2006 after their article speculating on the algorithm’s origin gained Slashdot attention. Key evidence includes: 1) Greg’s work with Cleve Moler at Ardent, 2) The function’s prior use in graphics software like the Ardent Titan pre-Quake III, and 3) Direct confirmation from Walsh himself.",
  "contradictions": [
    "Initial speculation incorrectly credited John Carmack or Michael Abrash due to their prominence in id Software and 3D graphics.",
    "Lack of documentation in Quake III’s source code about the algorithm’s origin led to confusion about the authorship."
  ],
  "unique_insights": [
    "Cleve Moler (co-creator of MATLAB) inspired the idea of using Newton-Raphson iteration for approximation of functions like 1/√x.",
    "The algorithm was refined and adapted through multiple contributors (e.g., Gary Tarolli’s role in porting it to 3dfx), but the constant 0x5F3759DF originated with Greg Walsh."
  ],
  "blind_spots": [
    "Early discussions on forums like gamedev.net and Slashdot perpetuated the myth of Carmack’s authorship despite his denial.",
    "The algorithm’s mathematical origins (bit-level hacking of IEEE floats) were unclear to many developers until later analysis."
  ],
  "partial_coverage": [
    "Wikipedia’s entry highlights Kahan/Ng’s earlier work on bit-level approximations but emphasizes Greg Walsh as the constant’s originator.",
    "The Beyond3D article was critical in tracing the algorithm’s lineage but initially omitted Walsh’s direct involvement until he commented post-Slashdot."
  ],
  "responses": [
    "The Beyond3D article links the algorithm to Greg Walsh’s work at Ardent Computer and his collaboration with Cleve Moler, crediting Walsh as the true originator of the constant.",
    "The 2006 Slashdot discussion prompted Greg Walsh to explicitly claim authorship, resolving prior ambiguity about whether Carmack or Abrash invented it.",
    "The Wikipedia entry confirms Greg Walsh as the author and explains the algorithm’s development timeline, emphasizing Walsh’s 1980s/90s work and the role of Newton-Raphson iteration.",
    "Academic analyses (e.g., Ryszard Sommefeldt’s thesis) acknowledge Walsh’s foundational role but note the algorithm’s evolution through multiple programmers before reaching its Quake III form."
  ]
}