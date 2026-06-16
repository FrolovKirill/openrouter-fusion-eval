# fac-09 — HTTP/1.1 current defining RFC
**Block:** factual  |  **difficulty:** hard

**Prompt:**
HTTP/1.1 was originally defined in RFC 2616 (1999). What RFC currently defines HTTP/1.1 as of 2022–2024? Walk through the succession: what replaced RFC 2616, and what then replaced that?

**Expected answer (эталон):**
RFC 2616 (1999) was replaced by RFCs 7230–7235 (2014). Those were superseded by RFC 9112 (June 2022), which is the current Internet Standard for HTTP/1.1 (STD 99). HTTP/2 is currently RFC 9113.

---
## FUSION-конфиги (judge-анализ; responses вынесены в resp_*.md)

### C1_west_closed
_западный закрытый фронтир_  
panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2 | cost=$0.4003 | 152.7s | ptok=16909 ctok=3376 | retries=0

**consensus:**
  - RFC 2616 (1999) is obsolete; it was obsoleted in 2014 by the HTTP/1.1 “bis” split into RFCs 7230, 7231, 7232, 7233, 7234, and 7235 (RFC Editor metadata for RFC 2616 and RFC 7230).
  - The 2014 HTTP/1.1 bis documents were superseded by the 2022 HTTP core revision: RFC 9112 (HTTP/1.1 message syntax / connection management), RFC 9110 (HTTP Semantics), and RFC 9111 (HTTP Caching).
  - RFC 9112 obsoletes the HTTP/1.1 messaging/connection-management portions of RFC 7230, while RFC 9110 obsoletes the remaining (version-independent) portions of RFC 7230 (stated in RFC 9112 and RFC 9110).
  - RFC 9111 obsoletes RFC 7234 (HTTP caching) (RFC Editor metadata for RFC 9111).

**contradictions:**
  - {"topic": "Whether RFC 9111 (HTTP Caching) is part of the current HTTP/1.1 definition / replacement chain", "stances": [{"model": "openai/gpt-5.2", "stance": "Includes RFC 9111 as part of the defining set for HTTP/1.1 and notes it obsoletes RFC 7234."}, {"model": "x-ai/grok-4.3", "stance": "Includes RFC 9111 alongside RFC 9110 and RFC 9112 as the companion documents defining HTTP/1.1."}, {"model": "google/gemini-3.1-pro-preview", "stance": "Mentions only RFC 9110 and RFC 9112 as the 2022 successors; omits RFC 9111 and does not account for RFC 7234 being obsoleted by RFC 9111."}, {"model": "evidence", "stance": "RFC 9111 (June 2022) explicitly obsoletes RFC 7234; RFC 9112’s introduction states HTTP/1.1 is defined by RFC 9112, RFC 9110, and RFC 9111."}]}

**unique_insights:**
  - {"model": "x-ai/grok-4.3", "insight": "Highlights the Internet Standard designation for HTTP/1.1: RFC 9112 is STD 99 (useful when asked what ‘currently defines’ HTTP/1.1 in standards terms, beyond just the RFC number)."}

**blind_spots:**
  - No model explicitly ties the 2022 HTTP core suite to the STD-series identifiers as a set (e.g., HTTP Semantics RFC 9110 is STD 97; HTTP Caching RFC 9111 is STD 98; HTTP/1.1 RFC 9112 is STD 99), which can matter when answering “what defines HTTP” at standards level.
  - No model (including those that were otherwise correct) explicitly cites primary RFC Editor ‘Obsoletes/Obsoleted by’ metadata as evidence in the answer itself, even though the question is about specification succession/authority rather than general description.

**partial_coverage:**
  - {"models": ["openai/gpt-5.2", "x-ai/grok-4.3"], "point": "Explicitly states that RFC 7230 was only partially obsoleted by RFC 9112 (HTTP/1.1-specific parts) and that the remaining parts are obsoleted by RFC 9110 (version-independent semantics/architecture)."}
  - {"models": ["openai/gpt-5.2"], "point": "Enumerates which 2014 RFCs are obsoleted by which 2022 RFC: RFC 9110 obsoletes RFC 7231/7232/7233/7235 (and parts of 7230), RFC 9111 obsoletes RFC 7234, and RFC 9112 obsoletes the HTTP/1.1 messaging parts of RFC 7230."}
  - {"models": ["x-ai/grok-4.3"], "point": "Calls out that RFC 9112 is published as STD 99 (HTTP/1.1’s Internet Standard number)."}

### C2_cn_open
_открытый китайский фронтир (умн+умн)_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507 | cost=$0.0813 | 138.9s | ptok=15362 ctok=3098 | retries=0

**consensus:**
  - HTTP/1.1 is currently defined by RFC 9112, RFC 9110, and RFC 9111 as of 2022–2024.
  - RFC 2616 (1999) was replaced by RFCs 7230–7235 in 2014.
  - RFCs 7230–7235 were in turn replaced by RFCs 9110, 9111, and 9112 in June 2022.
  - RFC 9112 specifically covers HTTP/1.1 message syntax, parsing, and connection management.
  - RFC 9110 defines HTTP semantics (methods, status codes, headers) as version-independent.
  - RFC 9111 defines HTTP caching behavior, replacing RFC 7234.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "deepseek/deepseek-v4-pro", "insight": "The 2022 restructuring explicitly separates version-independent semantics (RFC 9110) from version-specific wire formats (RFC 9112), enabling HTTP/2 and HTTP/3 to share the same semantic core."}

**blind_spots:**
  - No model discussed the role of IETF's HTTP Working Group in maintaining these specifications post-2022.
  - None addressed potential security implications or errata updates to RFC 9110–9112 since publication.
  - No mention of how implementations (e.g., browsers, servers) have adopted the 2022 RFC updates in practice.
  - Omission of the relationship between the new RFC structure and HTTP/2 or HTTP/3 standardization processes.
  - Lack of discussion on backward compatibility expectations for parsers handling legacy HTTP/1.1 messages.

**partial_coverage:**
  - {"models": ["deepseek/deepseek-v4-pro"], "point": "RFC 9110 obsoletes additional RFCs beyond the 723x series, including RFC 2818, 7538, 7615, and 7694."}

### C5_smartpanel_dumbjudge
_умная панель + глупый судья_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b | cost=$0.0632 | 801.4s | ptok=18310 ctok=7816 | retries=0

**consensus:**
  - RFC 2616 (1999) was replaced by RFCs 7230–7235 (2014)
  - RFCs 7230–7235 were replaced by RFCs 9110–9112 (2022)
  - HTTP/1.1 is defined by RFC 9112 (STD 99) as of 2022–2024

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "z-ai/glm-5.1", "insight": "RFC 9110 extracts shared semantics for all HTTP versions, enabling version-specific specs to reference a common core"}
  - {"model": "deepseek/deepseek-v4-pro", "insight": "RFC 9112 is co-authored by Roy T. Fielding (HTTP/1.1 original designer)"}

**blind_spots:**
  - Lack of mention of RFC 9931 (2023) as a minor update to RFC 9112
  - No discussion of IETF's standards track maturity levels beyond STD status
  - Omission of HTTP/2/3 RFCs (9113, 9114) in the succession chain

**partial_coverage:**
  - {"models": ["deepseek/deepseek-v4-pro", "z-ai/glm-5.1"], "point": "RFC 9110 separates HTTP semantics across all versions (1.1, 2, 3)"}
  - {"models": ["z-ai/glm-5.1"], "point": "RFC 9110, 9111, 9112 are all Internet Standards (STD 97/98/99)"}

### C5inv_dumbpanel_smartjudge
_глупая панель + умный судья (qwen-2.5-7b → gemma-3-12b-it)_  
panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1 | cost=$0.0859 | 166.2s | ptok=18081 ctok=3572 | retries=0

**consensus:**
  - RFC 2616 was replaced by the RFC 7230-7235 series (six RFCs) in 2014.
  - The RFC 7230-7235 series were themselves replaced by RFCs in the 9110+ range in June 2022.
  - As of 2022-2024, the 9110-series RFCs are the current standards.

**contradictions:**
  - {"topic": "What currently defines HTTP/1.1 as of 2022-2024", "stances": [{"model": "qwen/qwen3-8b", "stance": "HTTP/3 (RFC 9114) is the current standard, treating HTTP/2 and HTTP/3 as replacements for HTTP/1.1's defining RFCs."}, {"model": "google/gemma-3-12b-it", "stance": "RFC 9110 alone defines HTTP/1.1; the succession is 2616 → 7230 → 9110."}, {"model": "z-ai/glm-4.7-flash", "stance": "HTTP/1.1 is defined by RFCs 9110-9115, with specific recognition that 9112 covers HTTP/1.1 messaging separately from shared semantics."}, {"model": "evidence", "stance": "HTTP/1.1 is defined by the combination of RFC 9110 (HTTP Semantics), RFC 9111 (HTTP Caching), and RFC 9112 (HTTP/1.1 messaging). HTTP/2 (RFC 9113) and HTTP/3 (RFC 9114) are separate coexisting protocol versions, not replacements for HTTP/1.1."}]}
  - {"topic": "Whether HTTP/2 and HTTP/3 replaced HTTP/1.1 specifications", "stances": [{"model": "qwen/qwen3-8b", "stance": "RFC 7230-7235 were 'superseded by' RFC 7540 (HTTP/2), which was 'replaced by' RFC 9114 (HTTP/3) — conflates protocol version evolution with specification document succession."}, {"model": "evidence", "stance": "HTTP/1.1, HTTP/2, and HTTP/3 are parallel protocol versions that share common semantics (RFC 9110). Newer protocol versions do not obsolete or replace HTTP/1.1's defining documents."}]}
  - {"topic": "Number of RFCs that replaced RFC 2616", "stances": [{"model": "qwen/qwen3-8b", "stance": "Seven RFCs (7230-7235)."}, {"model": "evidence", "stance": "Six RFCs (7230, 7231, 7232, 7233, 7234, 7235) — confirmed by RFC 7230's own text listing six documents."}]}

**unique_insights:**
  - {"model": "z-ai/glm-4.7-flash", "insight": "The 2022 restructuring separated HTTP semantics (RFC 9110) and caching (RFC 9111) from HTTP/1.1 message syntax (RFC 9112), allowing each major protocol version to progress independently while sharing core semantics. This is the first time HTTP/1.1 messaging had its own standalone document distinct from shared semantics."}

**blind_spots:**
  - No model precisely states that HTTP/1.1 is defined by exactly three RFCs (9110 + 9111 + 9112), as explicitly stated in RFC 9112 Section 1.
  - The critical distinction between protocol version succession (HTTP/1.1 → HTTP/2 → HTTP/3 as coexisting protocol options) and specification document succession (RFC 2616 → RFCs 7230-7235 → RFCs 9110-9112 as obsoleting replacements) was not clearly articulated by any model.
  - RFC 9112's role as STD 99 and its specific obsolescence of the HTTP/1.1 messaging portions of RFC 7230 (while RFC 9110 obsoletes the semantic portions) was only partially addressed.
  - No model mentions that the 2014 RFC 7230-7235 series elevated HTTP/1.1 from Draft Standard to Proposed Standard, while the 2022 RFC 9110-9112 series elevated it to full Internet Standard status.

**partial_coverage:**
  - {"models": ["google/gemma-3-12b-it"], "point": "Correctly identifies the document-level succession from RFC 7230 to RFC 9110 for HTTP semantics, but misses that RFC 7230-7235 was a six-part series and that RFC 9112 specifically handles HTTP/1.1 messaging."}
  - {"models": ["z-ai/glm-4.7-flash"], "point": "Correctly notes STD designations (STD 97-101) for the 2022 RFC series, and identifies that the 2022 restructuring split HTTP/1.1 messaging into its own document (RFC 9112)."}

### C6_echo
_контроль: эхо-камера_  
panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507 | cost=$0.0472 | 111.7s | ptok=20805 ctok=4316 | retries=0

**consensus:**
  - HTTP/1.1 was originally defined in RFC 2616 (1999).
  - RFC 2616 was obsoleted in 2014 by RFC 7230–7235, with RFC 7230 being the primary specification for HTTP/1.1 message syntax and routing.
  - In June 2022, RFC 9112 was published and became the current standard for HTTP/1.1 message syntax and connection management.
  - RFC 9112 obsoletes the portions of RFC 7230 related to HTTP/1.1 messaging and connection management.
  - The current HTTP/1.1 specification is now modular, with shared semantics covered in RFC 9110 and caching in RFC 9111.

**contradictions:**
  - {"topic": "Whether RFC 9112 obsoletes the entirety of RFC 7230", "stances": [{"model": "qwen/qwen3-235b-a22b-2507", "stance": "Implies RFC 9112 completes the update series started by RFC 7230, possibly suggesting full obsoletion."}, {"model": "evidence", "stance": "RFC 9112 obsoletes only portions of RFC 7230; other parts are obsoleted by RFC 9110 (HTTP Semantics). This is explicitly stated in the text of RFC 9112: 'This document obsoletes the portions of RFC 7230 related to HTTP/1.1 messaging and connection management... The other parts of RFC 7230 are obsoleted by \"HTTP Semantics\" [HTTP].'"}]}

**unique_insights:**
  - {"model": "mistral-large-latest", "insight": "Identified the architectural motivation behind the 2022 split: modularizing shared semantics (RFC 9110) across HTTP versions to reduce redundancy and improve maintainability, which reflects a deeper understanding of the design rationale."}

**blind_spots:**
  - No model mentioned that RFC 9112 is part of a larger reorganization under the "HTTP Semantics" framework (RFC 9110), which redefines how HTTP standards are structured across versions.
  - None addressed that RFC 9931 (published in 2025) updates RFC 9112 by clarifying message parsing rules, indicating an active maintenance cycle not mentioned in the responses.
  - No model specified that the IETF HTTPbis working group transitioned to HTTP Working Group, and that the restructuring into RFC 9110–9112 reflects a long-term effort to unify HTTP specifications across versions.
  - Omission of the role of 'message/http' media type in allowing obsolete line folding (obs-fold), which is a specific normative reference in RFC 9112 but not explained in responses.

**partial_coverage:**
  - {"models": ["mistral-large-latest", "openai", "llama-3.1-8b-instruct", "mixtral-8x7b-32768"], "point": "The 2022 restructure splits shared semantics (across HTTP/1.1, 2, 3) into RFC 9110, and caching into RFC 9111, separating version-specific from version-agnostic components."}
  - {"models": ["mistral-large-latest", "openai", "llama-3.1-8b-instruct"], "point": "RFC 9112 is part of Internet Standard STD 99, the current standard track for HTTP/1.1."}

### C3_cn_small
_всё мелкое_  
panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b | cost=$0.0360 | 622.7s | ptok=15689 ctok=2877 | retries=0

**consensus:**
  - RFC 2616 (HTTP/1.1 initial) was obsoleted in 2014 by the RFC 7230–7235 suite.
  - The RFC 7230–7235 suite was replaced in June 2022 by the RFC 9110 (Semantics), RFC 9111 (Caching), and RFC 9112 (HTTP/1.1 specifics) trio.
  - RFC 9112 defines HTTP/1.1 message syntax and connection management currently.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "qwen/qwen3-32b", "insight": "RFC 9111 (Caching) is highlighted as part of the 2022 split into version-specific and generic components, alongside RFC 9110 and 9112."}
  - {"model": "qwen/qwen3-32b", "insight": "Motivates modularity (2014 split) by stating it allows 'each protocol version to progress independently,' directly linking to HTTP/2 and HTTP/3 development."}

**blind_spots:**
  - No model addresses whether any 2023–2024 RFCs have reintegrated HTTP/1.1 with other versions or revised the RFC 911x suite.
  - No discussion on how the modularization impacts backward compatibility or implementation practices for HTTP/1.1 server development.

**partial_coverage:**
  - {"models": ["qwen/qwen3-32b"], "point": "Mentions RFC 9111 (HTTP Caching) as part of the 2022 revision suite, which other models either omit (z-ai/glm-4.7-flash) or group with RFC 9110."}


---
## BASELINE (одиночная модель, без fusion)

### B_cn  (model=deepseek-v4-pro | cost=$0.0034 | 23.0s)
As of 2022–2024, HTTP/1.1 is defined by **RFC 9112** (titled *HTTP/1.1*), together with the shared semantic and caching layers in **RFC 9110** (*HTTP Semantics*) and **RFC 9111** (*HTTP Caching*).  

Here’s the succession:

1. **RFC 2616** (1999) – the original single-document definition of HTTP/1.1.  
2. **RFC 7230–7235** (June 2014) – a set of six documents that replaced RFC 2616, splitting the protocol into separate, clearer parts:  
   - RFC 7230 – Message Syntax and Routing  
   - RFC 7231 – Semantics and Content  
   - RFC 7232 – Conditional Requests  
   - RFC 7233 – Range Requests  
   - RFC 7234 – Caching  
   - RFC 7235 – Authentication  
3. **RFC 9110, 9111, 9112** (June 2022) – these obsoleted the 723x series and restructured HTTP into version-agnostic semantics (RFC 9110), caching (RFC 9111), and the HTTP/1.1 wire format (RFC 9112). (HTTP/2 and HTTP/3 are defined in separate RFCs 9113 and 9114, respectively.)

So the current normative specification for the HTTP/1.1 message format and connection management is **RFC 9112**, while the semantics (methods, headers, status codes) live in **RFC 9110** and caching rules in **RFC 9111**.

### B_west  (model=gpt-5.2 | cost=$0.0130 | 14.4s)
As of **2022–2024**, HTTP/1.1 is defined by the **HTTP core** RFCs published in 2022, chiefly:

- **RFC 9112 (2022)** — *HTTP/1.1* (message syntax, parsing, connection management, etc.)
- plus the shared core documents it depends on:
  - **RFC 9110 (2022)** — *HTTP Semantics* (methods, status codes, headers semantics, etc.)
  - **RFC 9111 (2022)** — *HTTP Caching*

So, “HTTP/1.1” today is effectively **RFC 9112 + RFC 9110 (+ RFC 9111 for caching behavior)**.

## Succession from RFC 2616 → current

### 1) RFC 2616 (1999) was replaced by the RFC 7230–7235 set (2014)
RFC 2616 was split/updated into a suite of documents published in 2014:

- **RFC 7230** — HTTP/1.1 Message Syntax and Routing  
- **RFC 7231** — Semantics and Content  
- **RFC 7232** — Conditional Requests  
- **RFC 7233** — Range Requests  
- **RFC 7234** — Caching  
- **RFC 7235** — Authentication  

Collectively, these **obsoleted RFC 2616** (and also obsoleted/updated related older RFCs like RFC 6266, RFC 2817, etc., but the key point is 2616 → 723x).

### 2) RFC 7230–7235 (2014) were replaced by the RFC 9110–9114 set (2022)
In 2022, the HTTP core specs were revised and reorganized again into:

- **RFC 9110** — HTTP Semantics  
  - *obsoletes:* **RFC 7231, 7232, 7233, 7235** (and more minor related docs)
- **RFC 9111** — HTTP Caching  
  - *obsoletes:* **RFC 7234**
- **RFC 9112** — HTTP/1.1  
  - *obsoletes:* **RFC 7230** (and also lists **RFC 2616** as obsolete)
- (for completeness, same “core” family:)
  - **RFC 9113** — HTTP/2 (obsoletes RFC 7540)
  - **RFC 9114** — HTTP/3 (obsoletes RFC 9000)

## In one line (the chain)
**RFC 2616 (1999)** → **RFC 7230–7235 (2014)** → **RFC 9110/9111/9112 (2022)** (with **9112** being the “HTTP/1.1” document).
