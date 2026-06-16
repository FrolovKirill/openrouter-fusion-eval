# fac-13 — Backpropagation 1986 paper  (raw panel responses + judge-синтез)
**Prompt:** What is the exact title, authors, journal, volume, and page numbers of the foundational 1986 paper that popularized backpropagation for training neural networks?

> ВНИМАНИЕ: responses релеятся caller'ом (qwen3-235b), не verbatim — атрибуция модели местами заменена ролью ('Panel Model A'); текст ответа реальный.


======================================================================
## C1_west_closed  (panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - The 1986 paper widely credited with popularizing backpropagation is titled “Learning representations by back-propagating errors” and is published in Nature.
  - Verified citation metadata: Rumelhart, D. E.; Hinton, G. E.; Williams, R. J.; Nature; volume 323; pages 533–536 (1986).
**contradictions:** 
  _(пусто)_
**unique_insights:** 
  - {"model": "google/gemini-3.1-pro-preview", "insight": "Highlights that the famous Nature letter coexisted with a broader 1986 exposition by the same authors in the PDP volume, which can be a source of citation confusion when people ask for the ‘foundational 1986 work’."}
**blind_spots:** 
  - No model provided additional verified bibliographic identifiers that help disambiguate editions/records (e.g., DOI 10.1038/323533a0, Nature issue date 09 Oct 1986, or issue number 6088), even though these are available from the journal record.
  - No model explicitly addressed potential ambiguity in the question between the short Nature letter (“Learning representations by back-propagating errors”) and the longer 1986 PDP chapter (“Learning internal representations by error propagation”), which are both commonly referenced.

### RAW PANEL RESPONSES (что панель реально сказала):

**[openai/gpt-5.2]:**
- **Exact title:** *Learning representations by back-propagating errors*  
- **Authors:** David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams  
- **Journal:** *Nature*  
- **Volume:** 323  
- **Page numbers:** 533–536

**[google/gemini-3.1-pro-preview]:**
{
  "consensus": "The exact details of the foundational 1986 paper that popularized backpropagation are: Title: 'Learning representations by back-propagating errors', Authors: David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams, Journal: Nature, Volume: 323, Page numbers: 533-536.",
  "contradictions": "None of the models contradict one another. They all provide the same, accurate bibliographic information.",
  "unique_insights": "While the Nature publication is the famous journal article, the same authors simultaneously published a broader, highly influential exploration of this topic as Chapter 8 in their 1986 book, 'Parallel Distributed Processing: Explorations in the Microstructure of Cognition'.",
  "blind_spots": "The models focus exclusively on identifying the 1986 paper and do not mention that the backpropagation algorithm was actually discovered earlier by researchers like Paul Werbos (1974) and Seppo Linnainmaa (1970).",
  "partial_coverage": "There are no instances of partial coverage; all basic bibliographic fields requested by the user are satisfied by all models.",
  "responses": {
    "model_1": "The exact publication facts for the paper you are referring to are:\n- Title: Learning representations by back-propagating errors\n- Authors: David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams\n- Journal: Nature\n- Volume: 323\n- Page numbers: 533-536\n- Published: October 1986",
    "model_2": "Here is the citation detail for the 1986 paper that popularized backpropagation for neural networks:\nTitle: Learning representations by back-propagating errors\nAuthors: David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams\nJournal: Nature\nVolume: 323\nPages: 533–536",
    "model_3": "Title: Learning representations by back-propagating errors\nAuthors: David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams\nJournal: Nature\nVolume: 323\nPages: 533-536"
  }
}

**[x-ai/grok-4.3]:**
{
  "consensus": "The 1986 Nature paper by Rumelhart, Hinton, and Williams is the one that popularized backpropagation.",
  "contradictions": [],
  "unique_insights": [
    "Exact citation: Learning representations by back-propagating errors, David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams, Nature volume 323, pages 533-536."
  ],
  "blind_spots": [],
  "partial_coverage": false,
  "responses": [
    {
      "model": "web_search",
      "answer": "Title: Learning representations by back-propagating errors. Authors: David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams. Journal: Nature. Volume: 323. Pages: 533-536. Year: 1986."
    }
  ]
}

======================================================================
## C2_cn_open  (panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - The paper was published in Nature in 1986.
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

### RAW PANEL RESPONSES (что панель реально сказала):

**[deepseek/deepseek-v4-pro]:**
Here is the exact bibliographic information:

```json
{
  "title": "Learning representations by back-propagating errors",
  "authors": ["David E. Rumelhart", "Geoffrey E. Hinton", "Ronald J. Williams"],
  "journal": "Nature",
  "volume": "323",
  "pages": "533–536",
  "year": 1986,
  "doi": "10.1038/323533a0"
}
```

**Summary:**
- **Title:** *Learning representations by back-propagating errors*
- **Authors:** David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams
- **Journal:** *Nature*
- **Volume:** 323 (issue 6088)
- **Pages:** 533–536
- **Published:** October 9, 1986

This paper is widely regarded as the foundational work that popularized the back-propagation algorithm for training multi-layer neural networks, sparking the first wave of modern connectionist research.

**[z-ai/glm-5.1]:**
The foundational 1986 paper that popularized backpropagation for training neural networks is:

| Field | Details |
|---|---|
| **Title** | *Learning representations by back-propagating errors* |
| **Authors** | David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams |
| **Journal** | **Nature** |
| **Volume** | **323** |
| **Pages** | **533–536** |
| **Year** | 1986 |

### Full citation

> Rumelhart, D. E., Hinton, G. E. & Williams, R. J. Learning representations by back-propagating errors. *Nature* **323**, 533–536 (1986).

This landmark **Nature** paper demonstrated that the backpropagation algorithm could train multi-layer neural networks with hidden units to learn useful internal representations, effectively overcoming the limitations of single-layer perceptrons that had stagnated the field since Minsky & Papert's *Perceptrons* (1969). It is widely credited with reigniting interest in neural network research.

> **Note:** The same authors also published a longer, more detailed version of the work the same year as a book chapter: Rumelhart, D. E., Hinton, G. E. & Williams, R. J. "Learning Internal Representations by Error Propagation," in *Parallel Distributed Processing: Explorations in the Microstructure of Cognition, Vol. 1: Foundations* (eds Rumelhart, D. E. & McClelland, J. L.) 318–362 (MIT Press, 1986). However, the *Nature* paper is the one typically cited as the foundational publication that popularized backpropagation.

**[moonshotai/kimi-k2.6]:**
The foundational 1986 paper is:

**Title:** Learning representations by back-propagating errors

**Authors:** David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams

**Journal:** *Nature*

**Volume:** 323

**Page numbers:** 533–536

======================================================================
## C5_smartpanel_dumbjudge  (panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - Title: Learning representations by back-propagating errors
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

### RAW PANEL RESPONSES (что панель реально сказала):

**[deepseek/deepseek-v4-pro]:**
```json
{
  "consensus": {
    "title": "Learning representations by back-propagating errors",
    "authors": ["David E. Rumelhart", "Geoffrey E. Hinton", "Ronald J. Williams"],
    "journal": "Nature",
    "volume": "323",
    "pages": "533–536",
    "year": 1986,
    "doi": "10.1038/323533a0"
  },
  "contradictions": [],
  "unique_insights": [
    "A contemporaneous, longer version of this work also appeared in the same year as a chapter (pages 318–362) in the edited volume 'Parallel Distributed Processing: Explorations in the Microstructure of Cognition, Vol. 1: Foundations' (MIT Press, 1986), providing a more extensive treatment of the backpropagation method."
  ],
  "blind_spots": [],
  "partial_coverage": [],
  "responses": {
    "model_1": "Title: Learning representations by back-propagating errors. Authors: David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams. Journal: Nature. Volume: 323. Pages: 533–536. Year: 1986. DOI: 10.1038/323533a0."
  }
}
```

**[z-ai/glm-5.1]:**
The foundational 1986 paper that popularized backpropagation for training neural networks is:

- **Title:** *Learning representations by back-propagating errors*
- **Authors:** David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams
- **Journal:** *Nature*
- **Volume:** 323 (Issue 6088)
- **Pages:** 533–536
- **Publication Date:** 9 October 1986
- **DOI:** [10.1038/323533a0](https://doi.org/10.1038/323533a0)

A standard citation would be:

> Rumelhart, D. E., Hinton, G. E. & Williams, R. J. Learning representations by back-propagating errors. *Nature* **323**, 533–536 (1986).

This landmark paper demonstrated that the backpropagation algorithm could train multi-layer neural networks with hidden units to learn useful internal representations, effectively overcoming the limitations of earlier single-layer approaches like the perceptron. It was published as a concise (4-page) Letter to *Nature* and is widely credited with sparking the resurgence of interest in neural network research in the late 1980s and beyond.

**[moonshotai/kimi-k2.6]:**
**Title:** Learning representations by back-propagating errors  
**Authors:** David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams  
**Journal:** *Nature*  
**Volume:** 323  
**Pages:** 533–536

======================================================================
## C5inv_dumbpanel_smartjudge  (panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - Title: 'Learning representations by back-propagating errors'
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

### RAW PANEL RESPONSES (что панель реально сказала):

**[qwen/qwen3-8b]:**
{
  "consensus": "The foundational 1986 paper on backpropagation is titled 'Learning representations by back-propagating errors', authored by David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams, published in Nature, volume 323, pages 533–536.",
  "contradictions": [],
  "unique_insights": [
    "The paper was published in Nature, a prestigious scientific journal, which highlights its significance in the field of artificial neural networks."
  ],
  "blind_spots": [
    "The search results contain fragmented text with potential OCR errors (e.g., 'distin guishes' instead of 'distinguishes'), but the core metadata aligns across sources."
  ],
  "partial_coverage": [
    "Some results mention additional related works (e.g., citations 1-22) but do not directly address the specific 1986 paper's metadata."
  ],
  "responses": [
    "## Learning representations by back-propagating errors\n[...]\nDavid E. Rumelhart*, Geoffrey E. Hintont & Ronald J. Williams*\n\n* Institute for Cognitive Science, C-015, University of California, San Diego, La Jolla, California 92093, USA t Department of Computer Science, Carnegie-Mellon University, Pittsburgh, Philadelphia 15213, USA\n[...]\nReceived 19 May; accepted 15 July 1986. \n[...]\nNature, 323, 533--536.",
    "NATURE VOL. 323 $ OCTOBER 1986\n[...]\nLearning representations by back-propagating errors\n\nDavid E. Rumelhart*, Geoffrey E. Hinton & Ronald J. Williams*\n[...]\nReceived 1 May; accepted 31 July 1986.\n[...]\nNature, 323, 533--536.",
    "Geoffrey E. Hinton's Publications: Backpropagation\n\n- Rumelhart, D. E., Hinton, G. E., and Williams, R. J. (1986) Learning representations by back-propagating errors. Nature, 323, 533--536.",
    "## Learning representations by back-propagating errors\n[...]\nDavid E. Rumelhart*, Geoffrey E. Hinton & Ronald J. Williams*\n[...]\nReceived 19 May; accepted 15 July 1986. \n[...]\nNature, 323, 533--536.",
    "Learning representations by back-propagating errors | SCIENCE@home\n[...]\nD. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams\n[...]\nPublished 1986 in Nature\n[...]\n1986-10-01"
  ]
}

**[google/gemma-3-12b-it]:**
```json
{
  "consensus": "The foundational 1986 paper that popularized backpropagation for training neural networks is \"Learning representations by back-propagating errors.\" Its authors are David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams. It was published in the journal *Parallel Distributed Processing: Explorations in the Microstructure of Cognition*, volume 1, and there are no specific page numbers universally cited as the paper is a chapter within a larger edited volume.",
  "contradictions": "None",
  "unique_insights": "Despite its immense impact, the 1986 paper wasn't a standalone publication. It existed as a chapter within a larger edited volume, which sometimes causes confusion regarding specific page numbers. Different sources cite slightly varied details concerning the exact volume title nuances due to the nature of the edited collection.",
  "blind_spots": "The analysis assumes that \"popularized\" accurately reflects the paper's impact. While undoubtedly significant, early adoption may have been limited by computational constraints and a lack of ready-to-use implementations, and other related work was happening concurrently.",
  "partial_coverage": "The analysis focuses solely on the core bibliographic details of the paper without delving into its technical innovations or subsequent impact on the field of deep learning. It does not explore why this particular paper resonated so strongly within the AI research community.",
  "responses": {
    "panel_model_1": "The seminal paper is \"Learning representations by back-propagating errors\" by Rumelhart, Hinton, and Williams (1986). It appeared as a chapter in *Parallel Distributed Processing: Explorations in the Microstructure of Cognition*, Volume 1. Because it's a chapter in a larger work, standard page numbers aren't applicable. The work is often just referred to simply as *Parallel Distributed Processing*. It is widely credited with popularizing the backpropagation algorithm for training multi-layer neural networks.",
    "panel_model_2": "The paper that is most frequently cited as popularizing backpropagation is \"Learning representations by back-propagating errors\" by Rumelhart, Hinton, and Williams, published in 1986. The publication was part of the edited volume *Parallel Distributed Processing: Explorations in the Microstructure of Cognition*, Volume 1. The relevant chapter doesn't have discrete, traditional page numbers because it was part of a larger edited book. The journal name is not applicable as it was a book chapter.",
    "panel_model_3": "The foundational paper on backpropagation that achieved widespread recognition is Rumelhart, Hinton, and Williams' \"Learning representations by back-propagating errors\" (1986). It was published as a chapter in *Parallel Distributed Processing: Explorations in the Microstructure of Cognition*, Volume 1. As it's part of an edited collection, it does not have standard page numbers. The authors are David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams."
  }
}
```

**[z-ai/glm-4.7-flash]:**
**Title:** Learning representations by back-propagating errors

**Authors:** David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams

**Journal:** Nature

**Volume:** 323

**Page Numbers:** 533–536

======================================================================
## C6_echo  (panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - The paper titled 'Learning representations by back-propagating errors' by David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams was published in 1986 in Nature, volume 323, pages 533–536.
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

### RAW PANEL RESPONSES (что панель реально сказала):

**[qwen/qwen3-235b-a22b-2507]:**
{
  "title": "Learning representations by back-propagating errors",
  "authors": ["David E. Rumelhart", "Geoffrey E. Hinton", "Ronald J. Williams"],
  "journal": "Nature",
  "volume": "323",
  "pages": "533–536"
}

**[qwen/qwen3-235b-a22b-2507]:**
{
  "title": "Learning representations by back-propagating errors",
  "authors": [
    "David E. Rumelhart",
    "Geoffrey E. Hinton",
    "Ronald J. Williams"
  ],
  "journal": "Nature",
  "volume": "323",
  "pages": "533–536",
  "year": 1986
}

**[qwen/qwen3-235b-a22b-2507]:**
{
  "title": "Learning representations by back-propagating errors",
  "authors": [
    "David E. Rumelhart",
    "Geoffrey E. Hinton",
    "Ronald J. Williams"
  ],
  "journal": "Nature",
  "volume": "323",
  "pages": "533–536",
  "year": 1986
}

======================================================================
## C3_cn_small  (panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - The foundational 1986 backpropagation paper is titled 'Learning representations by back-propagating errors' and was authored by David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams.
  - The paper was published in *Nature*, volume 323, pages 533–536.
**contradictions:** 
  _(пусто)_
**unique_insights:** 
  - {"model": "qwen/qwen3.6-27b", "insight": "Mention of a more detailed technical version of the 1986 paper published in the book *Parallel Distributed Processing: Explorations in the Microstructure of Cognition* (MIT Press, 1986)."}
**blind_spots:** 
  - The omission of historical context regarding earlier conceptual developments of backpropagation, such as Paul Werbos's 1974 Ph.D. thesis, which predated the 1986 paper.
  - No model explicitly addresses the distinction between backpropagation as a mathematical technique and its subsequent popularization in neural networks through the 1986 paper.

### RAW PANEL RESPONSES (что панель реально сказала):

**[qwen/qwen3.6-27b]:**
The foundational 1986 paper that popularized the backpropagation algorithm is widely cited as the "Rumelhart, Hinton, and Williams (1986)" paper. Its exact citation details are:

*   **Title:** Learning representations by back-propagating errors
*   **Authors:** David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams
*   **Journal:** *Nature*
*   **Volume:** 323
*   **Pages:** 533–536

*Additional Context:* Although the authors also published a more detailed technical version of this work in the book *Parallel Distributed Processing: Explorations in the Microstructure of Cognition* (MIT Press, 1986), the article in *Nature* (Volume 323, pages 533–536) is the specific publication responsible for the algorithm's massive explosion in popularity.

**[z-ai/glm-4.7-flash]:**
I'll search for the exact citation details of the foundational 1986 backpropagation paper.{
  "title": "Learning representations by back-propagating errors",
  "authors": "Rumelhart, D. E., Hinton, G. E., and Williams, R. J.",
  "journal": "Nature",
  "volume": "323",
  "pages": "533–536"
}

**[qwen/qwen3-32b]:**
ool_call>{
  "consensus": "The foundational 1986 backpropagation paper is titled 'Learning representations by back-propagating errors,' authored by David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams. It was published in Nature (vol. 323, pp. 533–536).",
  "contradictions": [],
  "unique_insights": [
    "The paper is frequently cited as the key work popularizing backpropagation for neural networks."
  ],
  "blind_spots": [
    "No alternative candidate papers are mentioned in the results, despite backpropagation's earlier conceptual origins (e.g., Werbos 1974)."
  ],
  "partial_coverage": false,
  "responses": [
    {
      "model": "openrouter_web_search",
      "response": "https://www.semanticscholar.org/paper/Learning-representations-by-back-propagating-errors-Rumelhart-Hinton/052b1d8ce63b07fec3de9dbb583772d860b7c769: @article{Rumelhart1986LearningRB, title={Learning representations by back-propagating errors}, author={David E. Rumelhart and Geoffrey E. Hinton and Ronald J. Williams}, journal={Nature}, year={1986}, volume={323}, pages={533-536}}",
      "confidence": 0.95
    },
    {
      "model": "openrouter_web_search",
      "response": "https://www.cs.toronto.edu/~hinton/backprop.html: Rumelhart, D. E., Hinton, G. E., and Williams, R. J. (1986) Learning representations by back-propagating errors. Nature, 323, 533--536.",
      "confidence": 0.95
    },
    {
      "model": "openrouter_web_search",
      "response": "https://scholar.google.com/scholar_lookup?title=Learning+representations+by+back-propagating+errors&author=Rumelhart,+D.E.&author=Hinton,+G.E.&author=Williams,+R.J.&publication_year=1986&journal=Nature&volume=323&pages=533%E2%80%93536&doi=10.1038/323533a0: Google Scholar citation confirming Nature 323(6088): 533–536.",
      "confidence": 0.95
    }
  ]
}