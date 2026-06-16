# fac-13 — Backpropagation 1986 paper
**Block:** factual  |  **difficulty:** very-hard

**Prompt:**
What is the exact title, authors, journal, volume, and page numbers of the foundational 1986 paper that popularized backpropagation for training neural networks?

**Expected answer (эталон):**
'Learning representations by back-propagating errors'. Authors: David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams. Journal: Nature. Volume 323, pages 533–536. Published October 9, 1986. (Note: backprop itself was independently developed earlier by Linnainmaa (1970) and Werbos (1974/1982); this paper popularized it for multi-layer perceptrons.)

---
## FUSION-конфиги (judge-анализ; responses вынесены в resp_*.md)

### C1_west_closed
_западный закрытый фронтир_  
panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2 | cost=$0.1732 | 137.3s | ptok=9977 ctok=1496 | retries=0

**consensus:**
  - The 1986 paper widely credited with popularizing backpropagation is titled “Learning representations by back-propagating errors” and is published in Nature.
  - Verified citation metadata: Rumelhart, D. E.; Hinton, G. E.; Williams, R. J.; Nature; volume 323; pages 533–536 (1986).

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "google/gemini-3.1-pro-preview", "insight": "Highlights that the famous Nature letter coexisted with a broader 1986 exposition by the same authors in the PDP volume, which can be a source of citation confusion when people ask for the ‘foundational 1986 work’."}

**blind_spots:**
  - No model provided additional verified bibliographic identifiers that help disambiguate editions/records (e.g., DOI 10.1038/323533a0, Nature issue date 09 Oct 1986, or issue number 6088), even though these are available from the journal record.
  - No model explicitly addressed potential ambiguity in the question between the short Nature letter (“Learning representations by back-propagating errors”) and the longer 1986 PDP chapter (“Learning internal representations by error propagation”), which are both commonly referenced.

**partial_coverage:**
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "Notes a contemporaneous, longer treatment by the same authors in Parallel Distributed Processing (1986) (often cited alongside the Nature article)."}
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "Adds historical context that core ideas/precursors of backpropagation/reverse-mode differentiation appear earlier (e.g., Linnainmaa 1970; Werbos 1974), so the 1986 paper popularized rather than originated the method."}

### C2_cn_open
_открытый китайский фронтир (умн+умн)_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507 | cost=$0.0351 | 90.0s | ptok=9681 ctok=1455 | retries=0

**consensus:**
  - The paper was published in Nature in 1986.
  - The title is 'Learning representations by back-propagating errors'.
  - The authors are David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams.
  - The volume number is 323.
  - The page numbers are 533–536.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "z-ai/glm-5.1", "insight": "The longer MIT Press book chapter version provides a more detailed exposition, but the Nature paper is the one that popularized backpropagation due to its brevity and visibility in a high-impact journal."}

**blind_spots:**
  - No model mentioned that backpropagation was independently discovered earlier, such as by Paul Werbos in his 1974 PhD thesis, or by others in the 1980s (e.g., Linnainmaa, LeCun), and that the 1986 paper's contribution was in demonstrating its practical effectiveness rather than inventing the algorithm itself.
  - No model addressed the biological plausibility critiques of backpropagation, which the original paper itself acknowledged, nor how this has shaped later research into more neuroscientifically plausible learning rules.
  - No model noted that while the paper was influential, deep learning's rise required later advances (e.g., ReLU, dropout, better hardware) to overcome training difficulties in deep networks.

**partial_coverage:**
  - {"models": ["z-ai/glm-5.1"], "point": "The paper was part of a broader revival following Minsky & Papert's 'Perceptrons' (1969), and a longer version was published in a 1986 MIT Press book chapter titled 'Learning Internal Representations by Error Propagation'."}
  - {"models": ["z-ai/glm-5.1", "deepseek/deepseek-v4-pro"], "point": "The paper's DOI is 10.1038/323533a0."}

### C5_smartpanel_dumbjudge
_умная панель + глупый судья_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b | cost=$0.0479 | 213.5s | ptok=9037 ctok=1292 | retries=0

**consensus:**
  - Title: Learning representations by back-propagating errors
  - Authors: David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams
  - Journal: Nature
  - Volume: 323
  - Pages: 533–536
  - Year: 1986

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "deepseek/deepseek-v4-pro", "insight": "A contemporaneous, longer version of this work also appeared in the same year as a chapter in the edited volume 'Parallel Distributed Processing'"}
  - {"model": "z-ai/glm-5.1", "insight": "The paper demonstrated backpropagation could train multi-layer networks, overcoming limitations of earlier single-layer approaches"}

**blind_spots:**
  - DOI not explicitly mentioned in all responses
  - Lack of mention about the paper being a 'Letter' to Nature
  - No discussion of the paper's role in sparking the late 1980s neural network resurgence

**partial_coverage:**
  - {"models": ["z-ai/glm-5.1"], "point": "Publication date (9 October 1986)"}
  - {"models": ["deepseek/deepseek-v4-pro", "z-ai/glm-5.1"], "point": "Issue number (6088)"}
  - {"models": ["z-ai/glm-5.1"], "point": "Citation example"}

### C5inv_dumbpanel_smartjudge
_глупая панель + умный судья (qwen-2.5-7b → gemma-3-12b-it)_  
panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1 | cost=$0.0656 | 123.0s | ptok=13077 ctok=2316 | retries=0

**consensus:**
  - Title: 'Learning representations by back-propagating errors'
  - Authors: David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams
  - Year: 1986

**contradictions:**
  - {"topic": "Publication venue, volume, and page numbers", "stances": [{"model": "qwen/qwen3-8b", "stance": "Published in Nature, volume 323, pages 533–536"}, {"model": "google/gemma-3-12b-it", "stance": "Published as a chapter in Parallel Distributed Processing: Explorations in the Microstructure of Cognition, Volume 1, with no standard page numbers"}, {"model": "z-ai/glm-4.7-flash", "stance": "Published in Nature, volume 323, pages 533–536"}, {"model": "evidence", "stance": "The Nature paper (Vol 323, pp 533–536) and the PDP book chapter are two distinct 1986 publications. The PDP chapter has a different title ('Learning Internal Representations by Error Propagation') and pages 318–362. The Nature article is the one that popularized backpropagation."}]}

**unique_insights:**
  - {"model": "google/gemma-3-12b-it", "insight": "Notes that the work existed in another form (PDP Volume 1 chapter), which sometimes causes bibliographic confusion — though the model itself falls victim to this confusion by merging the two publications"}

**blind_spots:**
  - No model clarified that the 1986 Nature paper popularized but did not invent backpropagation — prior descriptions exist by Linnainmaa (1970, reverse-mode autodiff), Werbos (1974 thesis/1982 NN application), LeCun (1985), and Parker (1985)
  - No model identified the two distinct 1986 Rumelhart-Hinton-Williams publications: the Nature letter ('Learning representations by back-propagating errors', pp 533-536) and the PDP book chapter ('Learning Internal Representations by Error Propagation', pp 318-362)
  - No model noted the Nature paper's issue number (6088) or DOI (10.1038/323533a0)

**partial_coverage:**
  - {"models": ["google/gemma-3-12b-it"], "point": "Mentions the PDP book chapter, which is a related but distinct longer publication by the same authors in 1986, but incorrectly conflates it with the Nature paper"}

### C6_echo
_контроль: эхо-камера_  
panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507 | cost=$0.0277 | 99.8s | ptok=8201 ctok=1085 | retries=0

**consensus:**
  - The paper titled 'Learning representations by back-propagating errors' by David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams was published in 1986 in Nature, volume 323, pages 533–536.

**contradictions:**
  - {"topic": "year inclusion", "stances": [{"model": "qwen/qwen3-235b-a22b-2507", "stance": "does not include year in response"}, {"model": "qwen/qwen3-235b-a22b-2507", "stance": "includes year: 1986"}, {"model": "qwen/qwen3-235b-a22b-2507", "stance": "includes year: 1986"}, {"model": "evidence", "stance": "year is 1986, as confirmed by publication date October 9, 1986"}]}

**unique_insights:**
  _(пусто)_

**blind_spots:**
  - The paper's prior technical work and historical context, such as the earlier development of backpropagation in the 1970s by Paul Werbos and others, which the 1986 paper built upon rather than invented from scratch.
  - The distinction between popularization and invention: the paper did not originate backpropagation but was instrumental in demonstrating its effectiveness in training deep networks with hidden layers, catalyzing the neural network revival.
  - The paper was part of a larger two-volume 1986 PDP (Parallel Distributed Processing) book series, where a more detailed version appeared, suggesting the Nature paper was a condensed, high-impact exposition.
  - The actual publication date was October 9, 1986, with received date May 1, 1986, and acceptance July 31, 1986—information absent from all responses.
  - The DOI 10.1038/323533a0 as a persistent identifier for the paper, essential for modern scholarly referencing, was not mentioned.

**partial_coverage:**
  - {"models": ["qwen/qwen3-235b-a22b-2507", "qwen/qwen3-235b-a22b-2507"], "point": "year: 1986"}

### C3_cn_small
_всё мелкое_  
panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b | cost=$0.0248 | 197.0s | ptok=9833 ctok=1459 | retries=0

**consensus:**
  - The foundational 1986 backpropagation paper is titled 'Learning representations by back-propagating errors' and was authored by David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams.
  - The paper was published in *Nature*, volume 323, pages 533–536.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "qwen/qwen3.6-27b", "insight": "Mention of a more detailed technical version of the 1986 paper published in the book *Parallel Distributed Processing: Explorations in the Microstructure of Cognition* (MIT Press, 1986)."}

**blind_spots:**
  - The omission of historical context regarding earlier conceptual developments of backpropagation, such as Paul Werbos's 1974 Ph.D. thesis, which predated the 1986 paper.
  - No model explicitly addresses the distinction between backpropagation as a mathematical technique and its subsequent popularization in neural networks through the 1986 paper.

**partial_coverage:**
  - {"models": ["qwen/qwen3-32b"], "point": "The lack of alternative candidate papers mentioned, despite backpropagation's earlier conceptual origins (e.g., Werbos 1974)."}


---
## BASELINE (одиночная модель, без fusion)

### B_cn  (model=deepseek-v4-pro | cost=$0.0005 | 4.4s)
The foundational 1986 paper that popularized the backpropagation algorithm for training neural networks is:

**Title:** "Learning representations by back-propagating errors"  
**Authors:** David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams  
**Journal:** *Nature*  
**Volume:** 323  
**Pages:** 533–536  
**Year:** 1986

(DOI: 10.1038/323533a0)

### B_west  (model=gpt-5.2 | cost=$0.0022 | 3.6s)
**Title:** “Learning representations by back-propagating errors”  
**Authors:** David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams  
**Journal:** *Nature*  
**Volume:** 323  
**Pages:** 533–536 (1986)
