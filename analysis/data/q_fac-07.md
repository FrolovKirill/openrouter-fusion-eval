# fac-07 — Transformer base model architecture
**Block:** factual  |  **difficulty:** medium

**Prompt:**
In the original 'Attention Is All You Need' paper (Vaswani et al., 2017): what are the exact architectural parameters of the BASE (not large) Transformer model? Specify: number of encoder layers, number of decoder layers, number of attention heads, and model dimension (d_model).

**Expected answer (эталон):**
6 encoder layers + 6 decoder layers. 8 attention heads (h=8). d_model = 512.

---
## FUSION-конфиги (judge-анализ; responses вынесены в resp_*.md)

### C1_west_closed
_западный закрытый фронтир_  
panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2 | cost=$0.1291 | 74.5s | ptok=10051 ctok=1530 | retries=0

**consensus:**
  - Encoder has 6 layers (N=6), verified in Vaswani et al. (2017) Section 3.1: “The encoder is composed of a stack of N = 6 identical layers.”
  - Decoder has 6 layers (N=6), verified in Vaswani et al. (2017) Section 3.1: “The decoder is also composed of a stack of N = 6 identical layers.”
  - Multi-head attention uses 8 heads (h=8), verified in Vaswani et al. (2017) (also shown in Table 3 base row).
  - Model dimension is d_model = 512, verified in Vaswani et al. (2017) Section 3.1 and Table 3 base row.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "google/gemini-3.1-pro-preview", "insight": "Notes the implied/stated per-head key/value size for BASE (d_k = d_v = 64) and connects it to d_model/h."}
  - {"model": "x-ai/grok-4.3", "insight": "Highlights that the BASE architecture values are explicitly tabulated (Table 3 as the base row), not merely described narratively."}

**blind_spots:**
  - No response precisely cites where each parameter appears in the paper (e.g., Section 3.1 for N and d_model; Table 3 for the base row hyperparameters).
  - No response clarifies that “h=8” applies to each multi-head attention module (encoder self-attn; decoder self-attn; decoder cross-attn), not a global count of heads for the whole model.
  - No response mentions that the arXiv paper has multiple versions but the BASE architectural hyperparameters (6/6 layers, 8 heads, d_model=512) remain consistent across versions, which matters for robust verification.

**partial_coverage:**
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "Adds per-head dimensions for BASE: d_k = d_v = 64 (since 512/8), which the paper states explicitly as well as being derivable."}
  - {"models": ["x-ai/grok-4.3"], "point": "Points to Table 3 as the explicit source listing BASE hyperparameters (base row: N=6, d_model=512, h=8)."}

### C2_cn_open
_открытый китайский фронтир (умн+умн)_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507 | cost=$0.0536 | 136.6s | ptok=10187 ctok=1585 | retries=0

**consensus:**
  - Number of encoder layers is 6
  - Number of decoder layers is 6
  - Number of attention heads is 8
  - Model dimension (d_model) is 512

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "z-ai/glm-5.1", "insight": "Explicitly connects the architecture values to Section 3.1 of the paper, reinforcing textual and tabular consistency."}

**blind_spots:**
  - The exact vocabulary size (37,000 tokens) used in the base model, mentioned in Section 5.1
  - The distinction that d_k and d_v are derived from d_model/h (512/8), not independently chosen
  - The fact that parameter sharing occurs between embedding and pre-softmax layers, affecting parameter count
  - The training details such as warmup steps (4000), optimizer (Adam with β₁=0.9, β₂=0.98), and learning rate schedule
  - The use of sinusoidal positional encodings in the base model, with learned embeddings performing similarly

**partial_coverage:**
  - {"models": ["deepseek/deepseek-v4-pro", "z-ai/glm-5.1"], "point": "Feed-forward inner-layer dimension (d_ff) is 2048"}
  - {"models": ["deepseek/deepseek-v4-pro", "z-ai/glm-5.1", "moonshotai/kimi-k2.6"], "point": "Per-head key and value dimensions (d_k, d_v) are 64"}
  - {"models": ["deepseek/deepseek-v4-pro", "z-ai/glm-5.1"], "point": "Dropout rate (P_drop) is 0.1"}
  - {"models": ["deepseek/deepseek-v4-pro", "z-ai/glm-5.1"], "point": "Label smoothing (ε_ls) is 0.1"}
  - {"models": ["deepseek/deepseek-v4-pro", "z-ai/glm-5.1"], "point": "Total parameter count is approximately 65 million"}

### C5_smartpanel_dumbjudge
_умная панель + глупый судья_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b | cost=$0.0643 | 113.2s | ptok=9043 ctok=1259 | retries=0

**consensus:**
  - Number of encoder layers: 6
  - Number of decoder layers: 6
  - Number of attention heads: 8
  - Model dimension (d_model): 512

**contradictions:**
  _(пусто)_

**unique_insights:**
  _(пусто)_

**blind_spots:**
  _(пусто)_

**partial_coverage:**
  _(пусто)_

### C5inv_dumbpanel_smartjudge
_глупая панель + умный судья (qwen-2.5-7b → gemma-3-12b-it)_  
panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1 | cost=$0.0357 | 74.3s | ptok=11263 ctok=1831 | retries=0

**consensus:**
  - Base model has N=6 encoder layers, verified in Section 3.1: 'The encoder is composed of a stack of N=6 identical layers'
  - Base model has N=6 decoder layers, verified in Section 3.1: 'The decoder is also composed of a stack of N=6 identical layers'
  - Base model has h=8 attention heads, verified in Section 3.2.2: 'In this work we employ h=8 parallel attention layers, or heads'
  - Base model has d_model=512, verified in Section 3.1: 'all sub-layers in the model, as well as the embedding layers, produce outputs of dimension d_model=512'
  - These four values are confirmed by the base model row in Table 3: N=6, d_model=512, h=8

**contradictions:**
  - {"topic": "Whether the paper explores the impact of varying architectural parameters", "stances": [{"model": "google/gemma-3-12b-it", "stance": "Claims the paper 'doesn't explore the impact of varying these parameters on model performance'"}, {"model": "evidence", "stance": "Table 3 explicitly varies number of heads (rows A), number of layers (rows C), d_model/d_ff (rows B/C), dropout (rows D), and positional encoding (row E), measuring BLEU and perplexity for each variation"}]}

**unique_insights:**
  - {"model": "z-ai/glm-4.7-flash", "insight": "Provided the complete Table 3 base model row including derived dimensions d_k=d_v=d_model/h=64, offering the full parameterization context rather than just the four requested values"}

**blind_spots:**
  - No model noted that the same N=6 applies to both encoder and decoder stacks (i.e., N is shared, not independently specified), which is a subtle architectural detail — the paper uses a single N for both
  - No model provided the 'big' model parameters as a contrasting reference point (N=6, d_model=1024, d_ff=4096, h=16), which would contextualize the base model's relative scale
  - No model mentioned the total parameter count of the base model (65M), which is listed in Table 3 and provides a useful summary metric of architectural scale

**partial_coverage:**
  - {"models": ["z-ai/glm-4.7-flash"], "point": "Cited additional base model parameters from Table 3 not requested in the question: d_ff=2048, d_k=64, d_v=64"}
  - {"models": ["z-ai/glm-4.7-flash"], "point": "Explicitly referenced Table 3 as the source for the base model configuration, providing a specific citation location"}

### C6_echo
_контроль: эхо-камера_  
panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507 | cost=$0.0617 | 705.2s | ptok=81639 ctok=19400 | retries=0

**consensus:**
  - The BASE Transformer model in the 'Attention Is All You Need' paper has 6 encoder layers.
  - The BASE Transformer model has 6 decoder layers.
  - The BASE Transformer model uses 8 attention heads.
  - The model dimension (d_model) of the BASE Transformer is 512.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "qwen/qwen3-235b-a22b-2507", "insight": "Section 3.1 of the paper explicitly states that all sub-layers and embedding layers produce outputs of dimension d_model=512, providing a functional rationale for consistent dimensionality throughout the model."}

**blind_spots:**
  - No model addressed that the 'BASE' configuration is not the only one evaluated — the paper contrasts it with the 'Big' model (d_model=1024, h=16, etc.), and conducts ablation studies in Table 3 rows (A)-(E) varying N, d_k, d_v, and positional encoding methods.
  - No model noted that the architectural choices (e.g., N=6, d_model=512) were selected based on English-to-German translation performance on newstest2013, and may not generalize as optimal for other tasks or modalities.
  - None considered that while d_model=512 and h=8 imply d_k=d_v=64 via d_k = d_model/h, this relationship is derived, not independently specified in the paper’s base configuration.
  - No mention was made of subsequent research challenging or validating the optimality of these base parameters in later models (e.g., in T5, BERT, or modern variants with different depth-width trade-offs).

**partial_coverage:**
  - {"models": ["qwen/qwen3-235b-a22b-2507"], "point": "Table 3 in the original paper also specifies d_ff=2048, d_k=64, d_v=64, and dropout rate P_drop=0.1 for the base model, which are related architectural hyperparameters."}
  - {"models": ["qwen/qwen3-235b-a22b-2507"], "point": "The total number of parameters for the base model is approximately 65 million, as listed in Table 3."}
  - {"models": ["qwen/qwen3-235b-a22b-2507"], "point": "The vocabulary size used in the base model is approximately 37,000 tokens, derived from byte-pair encoding."}

### C3_cn_small
_всё мелкое_  
panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b | cost=$0.0194 | 137.0s | ptok=8483 ctok=1115 | retries=1

**consensus:**
  - The BASE Transformer model from Vaswani et al. (2017) has 6 encoder layers, 6 decoder layers, 8 attention heads, and a model dimension (d_model) of 512. This information is verified against the original paper's Table 3 and Section 3.1.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "z-ai/glm-4.7-flash", "insight": "Explicitly references both Section 3.1 and Table 3 in the 2017 paper as the source for parameters, grounding claims in specific textual locations."}

**blind_spots:**
  - None of the models discuss the empirical validation or theoretical justification for these specific parameter choices in the original paper, such as trade-offs between computational cost and performance.

**partial_coverage:**
  _(пусто)_


---
## BASELINE (одиночная модель, без fusion)

### B_cn  (model=deepseek-v4-pro | cost=$0.0006 | 5.4s)
In the base Transformer model from "Attention Is All You Need" (Vaswani et al., 2017), the parameters are:

- **Encoder layers:** 6
- **Decoder layers:** 6
- **Attention heads:** 8
- **Model dimension (d_model):** 512

### B_west  (model=gpt-5.2 | cost=$0.0013 | 2.1s)
For the **Transformer BASE** model in *“Attention Is All You Need”* (Vaswani et al., 2017), the architectural parameters are:

- **Number of encoder layers:** 6  
- **Number of decoder layers:** 6  
- **Number of attention heads (per multi-head attention):** 8  
- **Model dimension (d_model):** 512
