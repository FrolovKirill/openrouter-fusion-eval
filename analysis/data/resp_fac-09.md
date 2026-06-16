# fac-09 — HTTP/1.1 current defining RFC  (raw panel responses + judge-синтез)
**Prompt:** HTTP/1.1 was originally defined in RFC 2616 (1999). What RFC currently defines HTTP/1.1 as of 2022–2024? Walk through the succession: what replaced RFC 2616, and what then replaced that?

> ВНИМАНИЕ: responses релеятся caller'ом (qwen3-235b), не verbatim — атрибуция модели местами заменена ролью ('Panel Model A'); текст ответа реальный.


======================================================================
## C1_west_closed  (panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - RFC 2616 (1999) is obsolete; it was obsoleted in 2014 by the HTTP/1.1 “bis” split into RFCs 7230, 7231, 7232, 7233, 7234, and 7235 (RFC Editor metadata for RFC 2616 and RFC 7230).
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

### RAW PANEL RESPONSES (что панель реально сказала):

**[openai/gpt-5.2]:**
{
  "consensus": "RFC 2616 (1999) was obsoleted in 2014 by the HTTP/1.1 “bis” document set RFC 7230, 7231, 7232, 7233, 7234, and 7235. That 2014 set was then obsoleted in 2022 by the current HTTP core specifications: RFC 9110 (HTTP Semantics), RFC 9111 (HTTP Caching), and RFC 9112 (HTTP/1.1 message syntax/connection management). As of 2022–2024, HTTP/1.1 is defined by RFC 9112 together with RFC 9110 and RFC 9111.",
  "contradictions": [],
  "unique_insights": [
    "RFC 9112 explicitly states: “HTTP/1.1 is defined by: This document; ‘HTTP Semantics’ [HTTP] (RFC 9110); ‘HTTP Caching’ [CACHING] (RFC 9111).”",
    "The 2022 revision splits what RFC 7230 previously combined: RFC 9112 covers HTTP/1.1 messaging/connection management, while RFC 9110 takes over the generic architecture/semantics portions (and also obsoletes RFC 7231/7232/7233/7235).",
    "RFC 9111 obsoletes RFC 7234 (caching) as part of the same 2022 refresh."
  ],
  "blind_spots": [
    "Does not enumerate non-core updates like RFC 2817 (CONNECT/TLS upgrade) or later updates such as RFC 9931 updating RFC 9112, because the question focuses on what defines HTTP/1.1 and the replacement succession of RFC 2616."
  ],
  "partial_coverage": [
    "Does not discuss HTTP/2 or HTTP/3 specifications since the question is specifically about HTTP/1.1."
  ],
  "responses": [
    {
      "model": "panel_a",
      "answer": "As of 2022–2024, the active HTTP/1.1 specification is RFC 9112 (HTTP/1.1). However, RFC 9112 is only the HTTP/1.1 wire format and connection management; it relies on RFC 9110 (HTTP Semantics) and RFC 9111 (HTTP Caching) for the shared semantics and caching rules.\n\nSuccession:\n1) RFC 2616 (1999) was made obsolete in 2014 by the HTTP/1.1 bis split into six RFCs:\n   - RFC 7230 (message syntax and routing)\n   - RFC 7231 (semantics and content)\n   - RFC 7232 (conditional requests)\n   - RFC 7233 (range requests)\n   - RFC 7234 (caching)\n   - RFC 7235 (authentication)\n\n2) The 2014 set was then replaced in 2022 by the HTTP core suite:\n   - RFC 9112 obsoletes RFC 7230 (the HTTP/1.1 messaging/connection parts)\n   - RFC 9110 obsoletes RFC 7231/7232/7233/7235 and the non-HTTP/1.1-specific parts of RFC 7230\n   - RFC 9111 obsoletes RFC 7234"
    },
    {
      "model": "panel_b",
      "answer": "HTTP/1.1 is currently defined (2022–2024) by RFC 9112 (HTTP/1.1), together with RFC 9110 (HTTP Semantics) and RFC 9111 (HTTP Caching).\n\nReplacement chain:\n- RFC 2616 → obsoleted by RFC 7230–7235 (June 2014).\n- RFC 7230–7235 → obsoleted by RFC 9110/9111/9112 (June 2022), with RFC 9112 being the dedicated HTTP/1.1 document and RFC 9110/9111 carrying semantics and caching."
    },
    {
      "model": "panel_c",
      "answer": "RFC 2616 (1999) was replaced by the 2014 HTTP/1.1 revision split across RFC 7230, 7231, 7232, 7233, 7234, and 7235. In 2022, those were replaced by RFC 9110 (semantics), RFC 9111 (caching), and RFC 9112 (HTTP/1.1). Therefore, as of 2022–2024, cite RFC 9112 (and also RFC 9110 + RFC 9111) for HTTP/1.1."
    }
  ]
}

**[google/gemini-3.1-pro-preview]:**
{
  "consensus": "The transition of HTTP/1.1 specifications moves sequentially from RFC 2616 to the RFC 7230 series, and culminating most recently in RFC 9110 and RFC 9112.",
  "contradictions": "There are no conflicting facts regarding the official IETF succession timeline for these protocols.",
  "unique_insights": "The 2022 standards updates deliberately abstracted core HTTP semantics (RFC 9110) away from version-specific messaging formats like HTTP/1.1 (RFC 9112).",
  "blind_spots": "No significant omissions identified in resolving the straightforward standard progression.",
  "partial_coverage": "The historical overview fully addresses the requested succession.",
  "responses": [
    "HTTP/1.1 was originally defined by RFC 2616 in 1999. In 2014, it was replaced by a six-part suite known as the RFC 7230 series (RFCs 7230 through 7235). As of June 2022, those documents were rendered obsolete by RFC 9110 (which defines general HTTP semantics applicable to all versions) and RFC 9112 (which exclusively defines the HTTP/1.1 messaging format and syntax)."
  ]
}

**[x-ai/grok-4.3]:**
```json
{
  "consensus": "RFC 9112 (June 2022, STD 99) is the current specification defining HTTP/1.1 messaging, syntax, and connection management. It obsoletes the relevant portions of RFC 7230 (with other parts of the 723x series moved to RFC 9110/9111).",
  "contradictions": [],
  "unique_insights": [
    "RFC 9112 explicitly states it obsoletes portions of RFC 7230, while RFC 9110 obsoletes the remaining parts of RFC 7230.",
    "HTTP/1.1 is now defined across three companion documents: RFC 9110 (Semantics), RFC 9111 (Caching), and RFC 9112 (Message syntax)."
  ],
  "blind_spots": [],
  "partial_coverage": [],
  "responses": {
    "search": "Results confirm RFC 9112 (published June 2022) as the current HTTP/1.1 definition, obsoleting parts of RFC 7230. Multiple sources (rfc-editor.org, datatracker) list it as STD 99."
  }
}
```

======================================================================
## C2_cn_open  (panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - HTTP/1.1 is currently defined by RFC 9112, RFC 9110, and RFC 9111 as of 2022–2024.
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

### RAW PANEL RESPONSES (что панель реально сказала):

**[deepseek/deepseek-v4-pro]:**
As of 2022–2024, HTTP/1.1 is defined by **RFC 9112** (“HTTP/1.1”, STD 99, June 2022). However, RFC 9112 no longer stands alone; it works together with two companion documents:

- **RFC 9110** (“HTTP Semantics”) – core methods, status codes, headers, etc.
- **RFC 9111** (“HTTP Caching”)

Together, RFCs 9110, 9111, and 9112 form the current Internet Standard for HTTP/1.1.

---

### The succession step‑by‑step

#### 1. Original HTTP/1.1 definition
- **RFC 2068** (January 1997) – first specification.
- **RFC 2616** (June 1999) – major revision, widely referenced for 15 years.

#### 2. First replacement – the six‑part decomposition (June 2014)
RFC 2616 was declared obsolete and replaced by a family of six documents:

| RFC | Title |
|-----|-------|
| RFC 7230 | HTTP/1.1: Message Syntax and Routing |
| RFC 7231 | HTTP/1.1: Semantics and Content |
| RFC 7232 | HTTP/1.1: Conditional Requests |
| RFC 7233 | HTTP/1.1: Range Requests |
| RFC 7234 | HTTP/1.1: Caching |
| RFC 7235 | HTTP/1.1: Authentication |

This rewrite clarified ambiguous language and tightened security without changing the protocol.

#### 3. Second replacement – the 2022 restructure (current state)
In June 2022, the IETF restructured HTTP again to separate the **protocol semantics** (shared by all HTTP versions) from the **version‑specific wire formatting**.

| RFC | Title | What it covers |
|-----|-------|----------------|
| **RFC 9112** | HTTP/1.1 | Message syntax, parsing, connection management (obsoletes the remaining parts of RFC 7230) |
| RFC 9110 | HTTP Semantics | Methods, status codes, header fields (obsoletes RFCs 7231–7235, 2818, 7538, 7615, 7694, and portions of 7230) |
| RFC 9111 | HTTP Caching | Cache behaviour (replaces RFC 7234) |

**Key point:** RFC 9112 is the direct successor to RFC 7230’s HTTP/1.1 messaging parts. Together with 9110 and 9111, it completely replaces the 2014 RFCs (7230–7235), which in turn had replaced RFC 2616.

---

**Summary chain:**
RFC 2616 (1999) → RFCs 7230‑7235 (2014) → RFCs 9110‑9112 (2022, current).

**[z-ai/glm-5.1]:**
Now I have a thorough picture of the full succession. Let me verify one more piece — the caching RFC:## The Succession of HTTP/1.1 RFCs

### Step 1: RFC 2616 → RFC 7230–7235 (2014)

In 2014, the single monolithic **RFC 2616** (1999) was obsoleted and the specification was **split into six separate documents**, each covering a distinct concern of HTTP/1.1:

| RFC | Title |
|---|---|
| **RFC 7230** | Message Syntax and Routing |
| **RFC 7231** | Semantics and Content |
| **RFC 7232** | Conditional Requests |
| **RFC 7233** | Range Requests |
| **RFC 7234** | Caching |
| **RFC 7235** | Authentication |

This decomposition was intentional — it separated the concerns so that each could be revised and understood independently, rather than having everything tangled in one enormous document.

---

### Step 2: RFC 7230–7235 → RFC 9110, 9111, 9112 (June 2022)

In June 2022, the six-document set was **reorganized and consolidated into three documents**, further refactoring the boundary between version-independent semantics and version-specific wire syntax:

| RFC | STD # | Title | What It Obsoletes |
|---|---|---|---|
| **RFC 9110** | STD 97 | **HTTP Semantics** | RFCs 7231, 7232, 7233, 7235, 2818, 7538, 7615, 7694, and *portions* of 7230 |
| **RFC 9111** | STD 98 | **HTTP Caching** | RFC 7234 |
| **RFC 9112** | STD 99 | **HTTP/1.1** | The remaining portions of RFC 7230 (messaging syntax & connection management) |

The key architectural change here is that **HTTP semantics (methods, status codes, headers) were extracted into RFC 9110 as a version-independent core**, while **RFC 9112 covers only the HTTP/1.1-specific wire format** (message syntax, framing, parsing, connection management). This allows HTTP/2 and HTTP/3 to share the same semantics (RFC 9110) while having their own mapping documents.

---

### The Current Answer (2022–2024)

**HTTP/1.1 is currently defined by the combination of three RFCs:**

1. **RFC 9110** (HTTP Semantics) — the version-independent core
2. **RFC 9111** (HTTP Caching) — caching behavior
3. **RFC 9112** (HTTP/1.1) — the HTTP/1.1-specific message syntax, parsing, and connection management

As RFC 9112 itself states: *"HTTP/1.1 is defined by: this document, 'HTTP Semantics' [HTTP], and 'HTTP Caching' [CACHING]."*

**[moonshotai/kimi-k2.6]:**
As of June 2022, HTTP/1.1 is defined by **RFC 9112** (STD 99), titled *HTTP/1.1*.

The succession is:

1. **RFC 2616** (1999) — the original HTTP/1.1 specification.

2. **RFC 2616 → RFC 7230–7235** (June 2014)  
   RFC 2616 was split and replaced by a family of six documents:
   - **RFC 7230** — Message Syntax and Routing  
   - **RFC 7231** — Semantics and Content  
   - **RFC 7232** — Conditional Requests  
   - **RFC 7233** — Range Requests  
   - **RFC 7234** — Caching  
   - **RFC 7235** — Authentication

3. **RFC 7230–7235 → RFC 9110 / 9111 / 9112** (June 2022)  
   The 2014 RFCs were themselves obsoleted by a revised trio that separates semantics, caching, and HTTP/1.1 messaging:
   - **RFC 9110** — *HTTP Semantics* (obsoletes RFC 7231, 7232, 7233, 7235, and the non-messaging portions of RFC 7230)  
   - **RFC 9111** — *HTTP Caching* (obsoletes RFC 7234)  
   - **RFC 9112** — *HTTP/1.1* (obsoletes the messaging and connection-management portions of RFC 7230)

So today, if you want the core definition of HTTP/1.1 message syntax, parsing, and connection management, the canonical reference is **RFC 9112**, together with **RFC 9110** for semantics and **RFC 9111** for caching.

======================================================================
## C5_smartpanel_dumbjudge  (panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - RFC 2616 (1999) was replaced by RFCs 7230–7235 (2014)
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

### RAW PANEL RESPONSES (что панель реально сказала):

**[deepseek/deepseek-v4-pro]:**
Based on my research, here is the complete succession of RFCs defining HTTP/1.1:

---

## The RFC Succession for HTTP/1.1

### 1. RFC 2616 (June 1999)
The widely referenced classic. Defined HTTP/1.1 as a single, monolithic document. **Status: Obsolete.**

### 2. RFCs 7230–7235 (June 2014) — First Replacement
RFC 2616 was decomposed into a six-part suite, each addressing a distinct aspect:

| RFC | Title |
|-----|-------|
| **RFC 7230** | Message Syntax and Routing |
| **RFC 7231** | Semantics and Content |
| **RFC 7232** | Conditional Requests |
| **RFC 7233** | Range Requests |
| **RFC 7234** | Caching |
| **RFC 7235** | Authentication |

Together, these obsoleted RFC 2616 (and RFC 2145 on HTTP versioning).

### 3. RFCs 9110–9112 (June 2022) — Current Definition (as of 2022–2024)
The 2014 suite was restructured again to separate **HTTP semantics** (shared across HTTP/1.1, HTTP/2, HTTP/3) from **version-specific messaging syntax**:

| RFC | Title | What It Obsoletes |
|-----|-------|--------------------|
| **RFC 9110** | HTTP Semantics | RFCs 2818, 7231, 7232, 7233, 7235, 7538, 7615, 7694, and portions of 7230 |
| **RFC 9111** | HTTP Caching | RFC 7234 |
| **RFC 9112** | **HTTP/1.1** (message syntax, parsing, connection management) | Portions of RFC 7230 |

---

## The Bottom Line

**As of 2022–2024, HTTP/1.1 is defined by RFC 9112** (also designated **STD 99** — an Internet Standard). It is co-authored/edited by Roy T. Fielding, Mark Nottingham, and Julian Reschke, and was published in June 2022.

In short:

> **RFC 2616 (1999)** → **RFCs 7230–7235 (2014)** → **RFCs 9110–9112 (2022, current)**

RFC 9112 is the document you want when looking for the authoritative HTTP/1.1 specification today. (It has one minor update so far: RFC 9931, which adds security considerations for optimistic protocol transitions.)

**[z-ai/glm-5.1]:**
## The RFC Succession for HTTP/1.1

### Step 1: RFC 2616 (June 1999) → RFCs 7230–7235 (June 2014)

The original **RFC 2616** was a single, monolithic document covering all of HTTP/1.1. In 2014, it was **obsoleted** and the specification was **split into six separate documents**, each focusing on a specific concern:

| RFC | Title |
|-----|-------|
| **RFC 7230** | HTTP/1.1 Message Syntax and Routing |
| **RFC 7231** | HTTP/1.1 Semantics and Content *(explicitly marked "Obsoletes: 2616")* |
| **RFC 7232** | HTTP/1.1 Conditional Requests |
| **RFC 7233** | HTTP/1.1 Range Requests |
| **RFC 7234** | HTTP/1.1 Caching |
| **RFC 7235** | HTTP/1.1 Authentication |

The key change was **modularization** — rather than one giant RFC, the protocol was decomposed into independently maintainable pieces.

---

### Step 2: RFCs 7230–7235 → RFCs 9110, 9111, 9112 (June 2022)

The 723x series was itself **obsoleted in June 2022** by a new trio of RFCs, which reorganized the split along slightly different lines — separating **semantics** (shared across all HTTP versions) from **version-specific messaging** and **caching**:

| New RFC | Title | What it obsoletes |
|---------|-------|-------------------|
| **RFC 9110** | **HTTP Semantics** | RFCs 2818, **7231**, **7232**, **7233**, **7235**, 7538, 7615, 7694, and *portions of* **7230** |
| **RFC 9111** | **HTTP Caching** | **RFC 7234** |
| **RFC 9112** | **HTTP/1.1** | Remaining *portions of* **RFC 7230** (the HTTP/1.1 messaging and connection management parts) |

The critical design shift here: **RFC 9110 (Semantics)** extracts the parts of the protocol that are **common to all HTTP versions** (1.1, 2, and 3), so that each version-specific spec (like RFC 9112 for HTTP/1.1, RFC 9113 for HTTP/2, RFC 9114 for HTTP/3) can reference the same core semantics without duplicating them.

---

### Summary: The Full Chain

```
RFC 2616 (1999)          — single monolithic HTTP/1.1 spec
       ├
       ▼  split into 6 docs
RFC 7230–7235 (2014)     — modular, but semantics still version-labeled "HTTP/1.1"
       ├
       ▼  reorganized into 3 docs
RFC 9110, 9111, 9112 (2022) — version-agnostic semantics + separate messaging/caching
```

**As of 2022–2024, HTTP/1.1 is defined by the combination of:**

- **RFC 9110** — HTTP Semantics (STD 97)
- **RFC 9111** — HTTP Caching (STD 98)
- **RFC 9112** — HTTP/1.1 (STD 99)

All three were published in **June 2022** and carry **Internet Standard (STD)** status — the highest maturity level in the IETF standards track.

**[moonshotai/kimi-k2.6]:**
As of 2022–2024, HTTP/1.1 is defined by **RFC 9112: HTTP/1.1** (STD 99), which specifies message syntax, parsing, and connection management. It works together with **RFC 9110: HTTP Semantics** (STD 97) and **RFC 9111: HTTP Caching** (STD 98) to cover the full protocol.

Succession:

1. **RFC 2616** (June 1999) — The original HTTP/1.1 specification.

2. **Replaced in 2014 by the RFC 723x series**:
   - **RFC 7230**: Message Syntax and Routing
   - **RFC 7231**: Semantics and Content
   - **RFC 7232**: Conditional Requests
   - **RFC 7233**: Range Requests
   - **RFC 7234**: Caching
   - **RFC 7235**: Authentication
   
   Collectively, RFCs 7230–7235 obsoleted RFC 2616 (and RFC 2145).

3. **Replaced in June 2022 by the RFC 911x series**:
   - **RFC 9110** obsoletes RFCs 7231, 7232, 7233, 7235, and the non-messaging portions of RFC 7230.
   - **RFC 9111** obsoletes RFC 7234.
   - **RFC 9112** obsoletes the messaging and connection-management portions of RFC 7230.

Thus, the current definition is the **RFC 9110 / 9111 / 9112** family, with **RFC 9112** being the document that specifically carries the “HTTP/1.1” title.

======================================================================
## C5inv_dumbpanel_smartjudge  (panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - RFC 2616 was replaced by the RFC 7230-7235 series (six RFCs) in 2014.
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

### RAW PANEL RESPONSES (что панель реально сказала):

**[qwen/qwen3-8b]:**
{
  "consensus": "The original HTTP/1.1 was defined in RFC 2616 (1999). It was later split into seven separate RFCs (7230-7235) in 2014, which collectively define HTTP/1.1. These were superseded by RFC 7540 (HTTP/2, 2015), which was then replaced by RFC 9114 (HTTP/3, 2022). As of 2022–2024, HTTP/3 (RFC 9114) is the current standard.",
  "contradictions": [],
  "unique_insights": [
    "RFC 2616 was split into seven RFCs (7230-7235) to modularize HTTP/1.1 specifications.",
    "HTTP/2 (RFC 7540) introduced binary framing and multiplexing, replacing the text-based HTTP/1.1.",
    "HTTP/3 (RFC 9114) replaced HTTP/2 by using QUIC as its transport protocol, improving performance and security."
  ],
  "blind_spots": [
    "The exact timeline of adoption and deprecation of RFCs may vary across implementations.",
    "Some legacy systems may still use older versions of HTTP/1.1 or intermediate RFCs."
  ],
  "partial_coverage": [
    "The answer focuses on RFC numbers and protocol versions but does not detail technical differences between HTTP/1.1, HTTP/2, and HTTP/3."
  ],
  "responses": [
    {
      "model": "mistralai/mistral-7b-instruct",
      "answer": "HTTP/1.1 is currently defined by the seven RFCs (7230-7235) that split RFC 2616 into modular components. These were superseded by RFC 7540 (HTTP/2) in 2015, which was later replaced by RFC 9114 (HTTP/3) in 2022. As of 2022–2024, RFC 9114 defines HTTP/3."
    },
    {
      "model": "google/gemma-7b",
      "answer": "RFC 2616 was replaced by RFC 7230-7235 (modularizing HTTP/1.1), then by RFC 7540 (HTTP/2), and finally by RFC 9114 (HTTP/3). The current standard as of 2022–2024 is HTTP/3, defined in RFC 9114."
    },
    {
      "model": "meta-llama/llama-3-8b-instruct",
      "answer": "RFC 2616 was split into RFCs 7230-7235, which defined HTTP/1.1. These were replaced by RFC 7540 (HTTP/2), which was superseded by RFC 9114 (HTTP/3). As of 2022–2024, HTTP/3 (RFC 9114) is the current standard."
    }
  ]
}

**[google/gemma-3-12b-it]:**
```json
{
  "consensus": "The evolution of HTTP/1.1's defining RFCs follows a clear succession: RFC 2616 was replaced by RFC 7230, which in turn was updated by RFC 9110. RFC 9110 is the current standard defining HTTP/1.1 as of 2022-2024.",
  "contradictions": [],
  "unique_insights": [
    "The progression highlights a shift towards more modular and extensible HTTP standards, with RFC 7230 introducing concepts like persistent connections and pipelining, and RFC 9110 further refining and solidifying these.",
    "The updates weren't complete overhauls but rather incremental improvements and clarifications, reflecting the ongoing evolution of the web and its needs."
  ],
  "blind_spots": [
    "The analysis doesn't delve into the specific technical changes introduced by each RFC revision.",
    "It doesn't discuss the impetus behind these revisions (e.g., new performance requirements, security concerns)."
  ],
  "partial_coverage": [
    "While the sequence of RFCs is clear, the detailed changes within each RFC are not elaborated upon.",
    "The context surrounding why each RFC was needed isn't fully explored."
  ],
  "responses": [
    {
      "panel_model": "Model A",
      "full_answer": "HTTP/1.1 was initially defined in RFC 2616 (1999).  It was later superseded by RFC 7230, which provided updates and clarifications to the protocol. Most recently, RFC 9110 replaced RFC 7230, serving as the current standard for HTTP/1.1 as of 2022-2024.  Thus the succession is RFC 2616 -> RFC 7230 -> RFC 9110."
    },
    {
      "panel_model": "Model B",
      "full_answer": "The defining RFC for HTTP/1.1 has evolved over time. Initially, it was RFC 2616. This was replaced by RFC 7230, which introduced updates to address issues and improve the protocol. The most current RFC that defines HTTP/1.1 is RFC 9110, as of the period 2022-2024.  Therefore the sequence is: RFC 2616 -> RFC 7230 -> RFC 9110."
    },
    {
      "panel_model": "Model C",
      "full_answer": "RFC 2616 originally established HTTP/1.1. However, RFC 2616 was later replaced by RFC 7230, which brought about several improvements and updates to the protocol. Following that, RFC 9110 took over as the current standard defining HTTP/1.1 as of 2022-2024.  The succession, therefore, is RFC 2616 -> RFC 7230 -> RFC 9110."
    }
  ]
}
```

**[z-ai/glm-4.7-flash]:**
```json
{
  "consensus": "As of 2022-2024, HTTP/1.1 is defined by RFC 9110-9115, which replaced RFC 7230-7235, which in turn replaced RFC 2616. The current specifications are Internet Standards (STD 97-101).",
  "contradictions": null,
  "unique_insights": "The 2022 restructuring (RFC 9110-9115) separated HTTP semantics (RFC 9110) and caching (RFC 9111) from HTTP/1.1 message syntax (RFC 9112), allowing each major protocol version to progress independently while sharing core semantics. This is the first time HTTP/1.1 has been defined as a separate document from the core semantics.",
  "blind_spots": null,
  "partial_coverage": null,
  "responses": [
    {
      "model": "claude-3-5-sonnet-20241022",
      "answer": "As of 2022-2024, HTTP/1.1 is defined by RFC 9110-9115, which replaced RFC 7230-7235, which in turn replaced RFC 2616. The current specifications are Internet Standards (STD 97-101).\n\nThe succession is:\n1. RFC 2616 (1999) - Original HTTP/1.1 specification\n2. RFC 7230-7235 (2014) - Six-part decomposition that replaced RFC 2616\n3. RFC 9110-9115 (2022) - Current specifications that replaced RFC 7230-7235\n\nThe 2022 restructuring (RFC 9110-9115) separated HTTP semantics (RFC 9110) and caching (RFC 9111) from HTTP/1.1 message syntax (RFC 9112), allowing each major protocol version to progress independently while sharing core semantics. This is the first time HTTP/1.1 has been defined as a separate document from the core semantics."
    }
  ]
}
```

======================================================================
## C6_echo  (panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - HTTP/1.1 was originally defined in RFC 2616 (1999).
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

### RAW PANEL RESPONSES (что панель реально сказала):

**[qwen/qwen3-235b-a22b-2507]:**
HTTP/1.1 was originally defined in RFC 2616 in 1999. This was replaced in June 2014 by a revised set of six RFCs (collectively updating and obsoleting RFC 2616), with the core message syntax and routing defined primarily in RFC 7230. As of June 2022, RFC 9112 is the current specification that defines HTTP/1.1 message syntax, connection management, and related aspects. RFC 9112 obsoletes the portions of RFC 7230 related to HTTP/1.1 messaging, completing the update series started by the RFC 7230–7235 revisions. Thus, the succession is: RFC 2616 → RFC 7230 (part of RFC 7230–7235) → RFC 9112.

**[qwen/qwen3-235b-a22b-2507]:**
{
  "consensus": "HTTP/1.1 is currently defined by RFC 9112 as of 2022–2024. This RFC supersedes RFC 7230, which in turn had replaced the original RFC 2616.",
  "contradictions": [],
  "unique_insights": [],
  "blind_spots": [],
  "partial_coverage": [],
  "responses": [
    {
      "model": "google",
      "response": "HTTP/1.1 is currently defined by RFC 9112 as of 2022. RFC 9112 replaces portions of RFC 7230, which had previously replaced RFC 2616. The original RFC 2616 was obsoleted in 2014 by a set of six new RFCs (RFC 7230 to RFC 7235) that separately specified various aspects of HTTP/1.1. In June 2022, further revisions were published by the IETF, now splitting the core HTTP semantics from the HTTP/1.1 message syntax. As of 2022, RFC 9112 defines the HTTP/1.1 message syntax, framing, and connection management, whereas RFC 9110 covers the shared HTTP semantics, which are common to all versions (1.1, 2, and 3). Therefore, RFC 9112 currently defines the HTTP/1.1 message syntax and connection management as part of the complete HTTP/1.1 specification alongside RFC 9110."
    },
    {
      "model": "mistral-large-latest",
      "response": "As of 2022–2024, HTTP/1.1 is no longer defined by a single RFC such as the original RFC 2616. Instead, the specification has been split into multiple RFCs to better modularize its components.\n\nThe current definition of HTTP/1.1 is primarily found in **RFC 9112**, titled \"HTTP/1.1\", published in June 2022. This RFC specifically covers message syntax, parsing, connection management, and related security concerns.\n\nThe evolution is as follows:\n1. **RFC 2616 (1999)** was the original comprehensive specification for HTTP/1.1.\n2. In 2014, RFC 2616 was obsoleted and replaced by a series of six RFCs: **RFC 7230 through RFC 7235**. These documents reorganized the HTTP/1.1 specification into more focused parts:\n   - RFC 7230: HTTP/1.1: Message Syntax and Routing\n   - RFC 7231: HTTP/1.1: Semantics and Content\n   - RFC 7232: Conditional Requests\n   - RFC 7233: Range Requests\n   - RFC 7234: Caching\n   - RFC 7235: Authentication\n\n3. Then, in 2022, a new set of RFCs further refined the structure:\n   - **RFC 9110**: \"HTTP Semantics\" – defines the core request methods, status codes, and general protocol semantics used across HTTP/1.1, HTTP/2, and HTTP/3.\n   - **RFC 9111**: \"HTTP Caching\" – covers HTTP caching, obsoleting parts of RFC 7234.\n   - **RFC 9112**: \"HTTP/1.1\" – defines only the message syntax and connection management specific to HTTP/1.1, obsoleting portions of RFC 7230.\n\nTherefore, the current specification for HTTP/1.1 is defined by **RFC 9112**, with support from RFC 9110 (semantics) and RFC 9111 (caching), forming the modern standard for HTTP/1.1 as of 2022–2024."
    },
    {
      "model": "openai",
      "response": "As of 2022–2024, HTTP/1.1 is currently defined by **RFC 9112**, published in June 2022. This RFC is now part of the Internet Standard STD 99.\n\nThe succession of RFCs defining HTTP/1.1 is as follows:\n\n- **RFC 2616 (1999)**: This was the original RFC that defined HTTP/1.1. It was comprehensive but became outdated and difficult to interpret due to accumulated errata.\n\n- **RFC 7230 – RFC 7237 (2014)**: In 2014, RFC 2616 was obsoleted and replaced by a revised series of RFCs (primarily RFC 7230 through RFC 7235), produced by the HTTPbis working group to clarify and update the original specification. Among these, **RFC 7230** was titled \"HTTP/1.1: Message Syntax and Routing\" and became the main specification for the core HTTP/1.1 message format.\n\n- **RFC 9110 – RFC 9112 (2022)**: In June 2022, the IETF published a final set of updates to consolidate HTTP standards. As part of this update:\n  - **RFC 9110** (“HTTP Semantics”),\n  - **RFC 9111** (“HTTP Caching”),\n  - and **RFC 9112** (“HTTP/1.1”)\n\nwere standardized. **RFC 9112** now defines the HTTP/1.1 message syntax and connection management, directly replacing the portions of RFC 7230 that were specific to HTTP/1.1. Meanwhile, RFC 9110 covers shared HTTP semantics across all versions (1.1, 2, 3).\n\nThus, as of 2024, **RFC 9112** is the current RFC that defines HTTP/1.1, succeeding **RFC 7230**, which had itself replaced **RFC 2616**."
    }
  ]
}

**[qwen/qwen3-235b-a22b-2507]:**
{"consensus": "As of 2022–2024, HTTP/1.1 is currently defined by RFC 9112, which is part of a revised series that replaced earlier specifications. RFC 2616, originally defining HTTP/1.1 in 1999, was first replaced in 2014 by a six-part series, most notably RFC 7230–7235. In 2022, this series was updated, with RFC 9112 now specifically defining HTTP/1.1 message syntax and connection management, obsoleting the relevant portions of RFC 7230.", "contradictions": [], "unique_insights": [], "blind_spots": [], "partial_coverage": [], "responses": [{"model": "llama-3.1-8b-instruct", "response": "As of 2022–2024, the current RFC that defines HTTP/1.1 is RFC 9112. RFC 9112 obsoletes portions of RFC 7230 related to HTTP/1.1 messaging and connection management.\n\nHere's a walk through the succession from RFC 2616 to the current RFC:\n\n1. RFC 2616 (1999) was the original specification for HTTP/1.1. It was eventually replaced due to its monolithic nature and to address issues and ambiguities discovered over time.\n\n2. In 2014, RFC 2616 was officially obsoleted and replaced by a series of six new RFCs:\n   - RFC 7230 - HTTP/1.1: Message Syntax and Routing\n   - RFC 7231 - HTTP/1.1: Semantics and Content\n   - RFC 7232 - HTTP/1.1: Conditional Requests\n   - RFC 7233 - HTTP/1.1: Range Requests\n   - RFC 7234 - HTTP/1.1: Caching\n   - RFC 7235 - HTTP/1.1: Authentication\n\n   Collectively, these RFCs updated and clarified the HTTP/1.1 specification, with RFC 7230 being the most relevant for message syntax.\n\n3. In June 2022, the IETF revised the HTTP specifications again:\n   - RFC 9110 replaced RFCs 7231, 7232, 7233, 7235, and parts of RFC 7230, covering HTTP semantics\n   - RFC 9111 replaced RFC 7234 for HTTP caching\n   - RFC 9112 specifically replaced the portions of RFC 7230 related to HTTP/1.1 message syntax and connection management and is now the current specification for HTTP/1.1\n\nTherefore, RFC 9112 is now the definitive RFC for HTTP/1.1, having succeeded both RFC 2616 (via the 2014 update) and RFC 7230 (via the 2022 update). RFC 9112 is part of the current set of standards defining HTTP, which also includes RFC 9110 (HTTP Semantics) and RFC 9111 (HTTP Caching)."}, {"model": "qwen2.5-7b-instruct", "response": "As of 2022–2024, the current RFC that defines HTTP/1.1 is RFC 9112. This document specifies the HTTP/1.1 message syntax, message parsing, connection management, and related security concerns.\n\nThe succession is as follows:\n\n1. RFC 2616 (1999) was the original comprehensive specification for HTTP/1.1.\n\n2. RFC 2616 was replaced in 2014 by a series of six RFCs (RFC 7230 through RFC 7235) that collectively updated and clarified HTTP/1.1. More specifically, RFC 7230 (\"HTTP/1.1: Message Syntax and Routing\") took over the core protocol aspects previously defined in RFC 2616.\n\n3. In 2022, this series was further updated. RFC 9112 specifically obsoletes \"portions of RFC 7230\" related to HTTP/1.1 message syntax and connection management, becoming the current specification for these aspects of HTTP/1.1.\n\nThus, the lineage is: RFC 2616 \u2192 RFC 7230 \u2192 RFC 9112. RFC 9112 is now the definitive RFC for the HTTP/1.1 message format and connection handling."}, {"model": "mixtral-8x7b-32768", "response": "As of 2022–2024, the current RFC that defines HTTP/1.1 is RFC 9112. This document specifically obsoletes portions of RFC 7230 related to HTTP/1.1 messaging and connection management.\n\nThe succession is as follows:\n\n1. RFC 2616 (1999) was originally the defining specification for HTTP/1.1.\n\n2. RFC 2616 was replaced by RFC 7230–7235 in 2014. These new RFCs were created to clarify and update the HTTP/1.1 specification. RFC 7230 specifically covered HTTP/1.1 message syntax and routing.\n\n3. The portions of RFC 7230 related to HTTP/1.1 messaging and connection management were then replaced by RFC 9112 in 2022.\n\nTherefore, the current specification for HTTP/1.1 is defined in RFC 9112, which supersedes both RFC 2616 and the relevant parts of RFC 7230."}]}

======================================================================
## C3_cn_small  (panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b)

### JUDGE-СИНТЕЗ (что судья извлёк):
**consensus:**   - RFC 2616 (HTTP/1.1 initial) was obsoleted in 2014 by the RFC 7230–7235 suite.
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

### RAW PANEL RESPONSES (что панель реально сказала):

**[qwen/qwen3.6-27b]:**
As of 2022–2024, **RFC 2616** is obsolete. HTTP/1.1 is currently defined by **RFC 9112** (for HTTP/1.1 specific message syntax and connection management), alongside the version-independent **RFC 9110** (HTTP Semantics) and **RFC 9111** (HTTP Caching).

Here is the step-by-step succession of how the specification evolved from its original definition to the current standards.

### 1. The Original Standard: RFC 2616 (1999)
**"Hypertext Transfer Protocol -- HTTP/1.1"**
*   **Context:** Published in June 1999, this was the first formal specification dedicated solely to HTTP/1.1.
*   **Structure:** It was a massive, monolithic document (over 170 pages) that combined all aspects of the protocol—message formatting, semantics (methods/headers), caching, authentication, and more—into a single specification.

### 2. The Modularization: RFC 7230–7235 (2014)
**RFC 2616 $\rightarrow$ A Split Suite of 6 RFCs**
*   **Context:** By the early 2010s, maintaining a single giant document for HTTP had become difficult, especially as the IETF began work on HTTP/2. To address this, the IETF decided to split the protocol into modular components.
*   **The Replacement:** In June 2014, RFC 2616 was **obsoleted** by a new suite of RFCs. Instead of one document, the specification was broken down into six smaller ones:
    *   **RFC 7230:** Message Syntax and Routing
    *   **RFC 7231:** Semantics and Content (Methods, Status Codes)
    *   **RFC 7232:** Conditional Requests
    *   **RFC 7233:** Range Requests
    *   **RFC 7234:** HTTP Caching
    *   **RFC 7235:** Authentication

### 3. The Modern Standard: RFC 9110, 9111, and 9112 (2022)
**The 7230–7235 Suite $\rightarrow$ Consolidated RFC 911x Series**
*   **Context:** In 2022, the IETF undertook another major revision to clean up ambiguous language, resolve errors in the 2014 suite, and further separate generic HTTP rules from HTTP/1.1 specific rules.
*   **The Replacement:** The 2014 RFCs were **obsoleted** by the following modern standards, published in June 2022:
    *   **RFC 9112 ("HTTP/1.1"):** This is the current definition of the actual HTTP/1.1 line-based messaging syntax and connection management rules.
    *   **RFC 9110 ("HTTP Semantics"):** Defines the generic parts of HTTP (methods, status codes, header fields) used by HTTP/1.1 (as well as HTTP/2 and HTTP/3).
    *   **RFC 9111 ("HTTP Caching"):** Defines the rules for caching responses.

**Summary of the Evolution:**
1.  **1999:** Everything in one book (**RFC 2616**).
2.  **2014:** Everything split into six chapters (**RFC 7230–7235**).
3.  **2022:** Chapters rewritten and separated by version. HTTP/1.1 specifics live in **RFC 9112**, while shared HTTP semantics live in **RFC 9110**.

**[z-ai/glm-4.7-flash]:**
{"consensus": "RFC 2616 was obsoleted by RFCs 7230-7235 in 2014, and these were further updated by RFCs 9110 and 9112 in 2022. As of 2022-2024, the current definition of HTTP/1.1 is the combination of RFC 9110 (HTTP Semantics) and RFC 9112 (HTTP/1.1).", "contradictions": null, "unique_insights": "The HTTP specification has undergone a major reorganization in 2022, separating the definition of semantics (RFC 9110) from the HTTP/1.1 messaging syntax and connection management (RFC 9112). This allows each major protocol version to progress independently while referring to the same core semantics.", "blind_spots": null, "partial_coverage": null, "responses": [{"model": "gpt-4o", "answer": "RFC 2616 was obsoleted by a series of six RFCs published in 2014: RFC 7230 (Message Syntax and Routing), RFC 7231 (Semantics and Content), RFC 7232 (Conditional Requests), RFC 7233 (Range Requests), RFC 7234 (Caching), and RFC 7235 (Authentication). As of 2022-2024, these RFCs have been further updated and replaced by RFC 9110 (HTTP Semantics) and RFC 9112 (HTTP/1.1), both published in June 2022. RFC 9110 obsoletes RFCs 2818, 7231, 7232, 7233, 7235, 7538, 7615, 7694, and portions of 7230. RFC 9112 obsoletes portions of RFC 7230 related to HTTP/1.1 messaging and connection management."}, {"model": "claude-3-opus", "answer": "RFC 2616 was obsoleted by RFCs 7230-7235 in 2014, which collectively formed the HTTP/1.1 specification. These documents were later updated by RFCs 9110 and 9112 in 2022. RFC 9110 (HTTP Semantics) obsoletes RFCs 2818, 7231, 7232, 7233, 7235, 7538, 7615, 7694, and portions of 7230. RFC 9112 (HTTP/1.1) obsoletes portions of RFC 7230 related to HTTP/1.1 messaging and connection management. The current definition of HTTP/1.1 as of 2022-2024 is the combination of RFC 9110 and RFC 9112."}, {"model": "llama-3-70b", "answer": "RFC 2616 was replaced by a series of six RFCs published in 2014: RFC 7230 (Message Syntax and Routing), RFC 7231 (Semantics and Content), RFC 7232 (Conditional Requests), RFC 7233 (Range Requests), RFC 7234 (Caching), and RFC 7235 (Authentication). These were further updated by RFCs 9110 and 9112 in 2022. RFC 9110 obsoletes RFCs 2818, 7231, 7232, 7233, 7235, 7538, 7615, 7694, and portions of 7230. RFC 9112 obsoletes portions of RFC 7230 related to HTTP/1.1 messaging and connection management. As of 2022-2024, the current definition of HTTP/1.1 is the combination of RFC 9110 and RFC 9112."}]}

**[qwen/qwen3-32b]:**
ool_call>{"consensus": "The current RFC defining HTTP/1.1 is RFC 9112 (June 2022), which obsoletes RFC 7230. RFC 7230 itself replaced RFC 2616 (1999).", "contradictions": [], "unique_insights": [{"model": "tool_response_1", "insight": "RFC 9112 is explicitly noted as obsoleting RFC 7230 and being the current standard for HTTP/1.1 as of 2022."}, {"model": "tool_response_3", "insight": "RFC 9110 (HTTP Semantics) and RFC 9111 (Caching) are part of the 2022 split, with RFC 9112 handling message syntax."}], "blind_spots": ["The response does not address potential newer superseding documents post-2024."], "partial_coverage": ["The historical decomposition of RFC 2616 into 7230–7235 is confirmed, but detailed transition notes are sparse in the provided data."], "responses": ["RFC 9112 replaces RFC 7230, which replaced RFC 2616."]}