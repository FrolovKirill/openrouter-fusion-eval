# sci-04 — Neuromorphic chip efficiency claim
**Block:** scientific

**Prompt:**
A semiconductor startup claims their neuromorphic chip achieves 1000x better energy efficiency than NVIDIA H100 for transformer inference at equivalent throughput for 70B parameter models. What would you need to see in their technical documentation to take this seriously? What are the top 3 ways such claims typically fall apart under scrutiny?

---
## FUSION-конфиги (judge-анализ; responses вынесены в resp_*.md)

### C1_west_closed
_западный закрытый фронтир_  
panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2 | cost=$0.1022 | 190.6s | ptok=18083 ctok=3705 | retries=0

**consensus:**
  - Apples-to-apples benchmarking details are required (model variant, batch size, sequence/context length, decoding vs prefill mix, latency constraints, precision/quantization, sparsity settings, kernel/library versions) because H100 results vary widely with configuration.
  - Energy claims must be supported by end-to-end power measurements (board/system-level power including memory, I/O, interconnect, host contributions as relevant), not “compute core” or “MAC array” power alone.
  - Documentation must account for memory capacity/bandwidth and data-movement energy (weights + activations/KV-cache), since transformer inference is often dominated by memory and interconnect rather than arithmetic.

**contradictions:**
  - {"topic": "Does a 70B model necessarily require multi-chip partitioning due to weight size?", "stances": [{"model": "google/gemini-3.1-pro-preview", "stance": "Implied yes: 70B at FP16 is ~140GB, so it is “virtually guaranteed” to be split across multiple chips; interconnect cost then becomes central."}, {"model": "evidence", "stance": "Not necessarily: weight-only size can be reduced via quantization (e.g., ~70GB at 8-bit, ~35GB at 4-bit), so single-accelerator deployments can be feasible on 80GB-class devices; multi-chip becomes workload/precision/overhead dependent (also KV-cache and runtime buffers matter)."}]}
  - {"topic": "Is the “memory wall” an absolute lower bound that makes 1000× efficiency effectively impossible regardless of architecture?", "stances": [{"model": "google/gemini-3.1-pro-preview", "stance": "Frames memory movement energy as the dominating, dictating minimum power budget “regardless of compute core architecture,” making 1000× highly suspect."}, {"model": "x-ai/grok-4.3", "stance": "Treats memory/data-movement as a common gap but not an absolute impossibility; focuses on what must be documented and measured."}, {"model": "evidence", "stance": "Data movement is typically dominant for LLM inference, but not strictly architecture-invariant: gains can come from changing where weights live (on-chip SRAM/NVM), reducing bytes moved (quantization/compression/sparsity/speculative methods), or changing the algorithm; still, 1000× vs a well-optimized H100 remains extraordinary and demands unusually strong proof."}]}
  - {"topic": "Neuromorphic architectural fit for transformer inference (dense matmuls, softmax, autoregressive decode)", "stances": [{"model": "google/gemini-3.1-pro-preview", "stance": "Suggests a fundamental mismatch (neuromorphic excels at sparse/event-driven workloads; transformers are dense/synchronous), so parity claims often rely on modified models/assumptions."}, {"model": "x-ai/grok-4.3", "stance": "Notes the conflict as a frequent issue but frames it as an engineering/benchmarking risk (e.g., softmax/attention inefficiency, assumed sparsity) rather than a strict impossibility."}]}
  - {"topic": "Response completeness (non-answer vs substantive criteria)", "stances": [{"model": "openai/gpt-5.2", "stance": "Provides no evaluation criteria; only states inability to use a tool."}, {"model": "google/gemini-3.1-pro-preview", "stance": "Provides substantive documentation requirements and common failure modes."}, {"model": "x-ai/grok-4.3", "stance": "Provides substantive documentation requirements and common failure modes."}]}

**unique_insights:**
  - {"model": "x-ai/grok-4.3", "insight": "Neuromorphic-specific “spike encoding overhead” should be accounted for in throughput and energy: if continuous activations/attention are encoded into spikes/events, the representation overhead can erase claimed gains unless rigorously measured end-to-end."}

**blind_spots:**
  - No model pins down what “equivalent throughput” must mean for LLMs (separating prefill vs decode, tokens/s at a specified latency SLO, context length, batch size distribution, and real serving traces). This is often where claims hide (e.g., enormous batch with unusable latency).
  - None demand a strict baseline definition for H100 (exact GPU SKU 80GB vs 94GB, power limit, clocks, TensorRT-LLM version, KV-cache precision, FP8/INT8 usage, kernel fusions, speculative decoding). Without this, “1000× vs H100” can be a strawman baseline.
  - Insufficient attention to accuracy comparability: not just “no perplexity drop,” but task-level evals under the same quantization/approximation, including robustness across prompts and long-context behavior; also reporting calibration/drift effects for analog/spiking implementations.
  - No one explicitly requires inclusion of KV-cache memory traffic/energy (often dominant in decode at long context) and how/where KV-cache is stored (HBM/DDR/SRAM) for the claimed regime.
  - No discussion of measurement protocol details needed to prevent power-reporting artifacts (wall-plug vs rail power, sampling rate, warm-up/steady-state, inclusion of PSU losses, cooling/pumps/fans if comparing system energy, confidence intervals across runs).
  - No deep treatment of scalability and packaging constraints: multi-chip partition strategy, collective ops, link bandwidth/latency, serialization overheads, and whether the interconnect energy breaks the claim at 70B deployment scale.
  - Reliability/manufacturability gaps are largely unaddressed: yield, variability, aging, temperature sensitivity (especially for analog/neuromorphic), required calibration frequency, and how these affect sustained efficiency in production.
  - Economic/practical deployment factors are omitted: cost per token including capex, board count, memory type availability, ecosystem integration (framework support, monitoring, failure modes), and whether the solution is datacenter-viable at required throughput.

**partial_coverage:**
  - {"models": ["x-ai/grok-4.3"], "point": "Calls out process node/die size/on-chip memory hierarchy as required context for energy-efficiency plausibility; mentions spike-encoding overheads as a neuromorphic-specific accounting item."}
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "Explicitly demands a mapping strategy for attention/softmax/autoregressive decoding onto spiking/analog primitives and warns about projecting from tiny tiles to multi-chip systems without interconnect energy."}
  - {"models": ["google/gemini-3.1-pro-preview", "x-ai/grok-4.3"], "point": "Emphasize software-stack/compilation/reproducibility needs (open benchmark code, ability to run standard PyTorch/TensorRT-like graphs, avoidance of hand-tuned one-off demos) as a common place claims fail."}
  - {"models": ["x-ai/grok-4.3"], "point": "Explicitly requests third-party/independent validation and NDA-free reproducibility as a seriousness threshold."}

### C2_cn_open
_открытый китайский фронтир (умн+умн)_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507 | cost=$0.1807 | 488.0s | ptok=20343 ctok=4346 | retries=0

**consensus:**
  - Measurement boundaries must include full system-level power (chip, board, rack, cooling, host CPU) to be comparable.
  - Model architecture, precision, sparsity, and accuracy must be identical between the neuromorphic chip and H100 for a valid comparison.
  - Throughput claims must specify batch size, sequence length, and latency constraints to avoid cherry-picking favorable conditions.
  - Claims require verification against standardized benchmarks like MLPerf Inference or NeuroBench for credibility.
  - Apples-to-oranges comparisons—such as using a spiking or matrix-free architecture versus a dense transformer—are invalid and misleading.

**contradictions:**
  - {"topic": "Memory feasibility for 70B models on neuromorphic chips", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "A 70B model (~140 GB) would not fit on any existing neuromorphic chip; multi-chip scaling introduces inter-chip communication bottlenecks."}, {"model": "kimi-k2.6", "stance": "Future research steps involve mapping larger LLMs like 70B to correspondingly larger NorthPole appliances, implying on-chip storage per layer via quantization and distributed mapping."}, {"model": "evidence", "stance": "IBM NorthPole research is actively developing 70B model scaling using 16-card appliances with on-chip storage of weights and KV cache at INT4 precision, making such deployment plausible via pipelined layer distribution."}]}
  - {"topic": "Magnitude of neuromorphic efficiency gains over GPUs", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "Historic neuromorphic gains are 14–26×; 1000× efficiency over H100 is implausible without radical breakthroughs."}, {"model": "kimi-k2.6", "stance": "1000× efficiency is extraordinary and collapses under scrutiny; IBM NorthPole achieved only 72.7× on a 3B model."}, {"model": "evidence", "stance": "IBM NorthPole achieves 72.7× better energy efficiency than H100 on a 3B model, and explicitly plans 70B model deployment—providing credible near-term path for 10–100× gains, but not 1000×, consistent with physical and scaling limits."}]}

**unique_insights:**
  - {"model": "kimi-k2.6", "insight": "The 'chip-only' trick is a common failure mode: startups quote core array power (in mW ) while H100 baseline uses full rack/PDU power, creating an illusion of 100000× gains when system-level accounting eliminates most of the advantage."}
  - {"model": "deepseek/deepseek-v4-pro", "insight": "Energy-per-token must be compared at identical task accuracy; many neuromorphic approaches sacrifice precision (e.g., binarized networks) that degrade output quality, making gains illusory when accuracy is normalized."}

**blind_spots:**
  - None of the models addressed the feasibility of manufacturing yield, cost-per-chip, or total cost of ownership for a neuromorphic system, which are fundamental to commercial viability.
  - No response considered the impact of software maturity and developer ecosystem lock-in, where even energy-efficient hardware fails due to lack of tooling, libraries, or model conversion support.
  - Thermal throttling and long-term reliability under sustained inference workloads were not discussed, despite being critical for datacenter deployment.
  - The role of quantization (e.g., INT4, FP8) on both H100 and neuromorphic systems was underanalyzed; H100 with FP8 achieves ~0.08 tokens/sec/W for 70B models, setting a high bar.
  - No mention of the necessity of end-to-end benchmark reproducibility: open datasets, code, and containerized environments to validate claims independently.

**partial_coverage:**
  - {"models": ["deepseek/deepseek-v4-pro"], "point": "Host overhead—such as tokenization and data orchestration—can dominate energy use if the neuromorphic chip is used as a co-processor."}
  - {"models": ["kimi-k2.6"], "point": "Software stack maturity and framework support are underappreciated: lack of integration with frameworks like PyTorch/TensorRT-LLM undermines practical deployment."}

### C5_smartpanel_dumbjudge
_умная панель + глупый судья_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b | cost=$0.2023 | 364.7s | ptok=31999 ctok=7048 | retries=0

**consensus:**
  - Full system-level power measurement is required, not just chip power
  - Model architecture and accuracy parity must be identical to the H100 baseline
  - Throughput comparisons must specify batch sizes, latency constraints, and context lengths
  - KV cache memory bandwidth dominates energy costs for 70B models
  - Neuromorphic sparsity provides limited benefit for dense transformer attention

**contradictions:**
  - {"topic": "Architectural compatibility of spiking neural networks (SNNs) with transformers", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "SNN conversions above 300M parameters degrade beyond acceptable thresholds"}, {"model": "z-ai/glm-5.1", "stance": "SNNs have inductive bias toward low-frequency mappings, making them poor at long-range dependencies"}, {"model": "moonshotai/kimi-k2.6", "stance": "SNNs can slash compute but often trade substantial accuracy and generality"}]}
  - {"topic": "Energy efficiency scaling with parameter count", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "1000x efficiency requires 70B transformer with published accuracy parity"}, {"model": "z-ai/glm-5.1", "stance": "Scaling from 370M to 70B parameters involves unknown non-linear effects"}, {"model": "moonshotai/kimi-k2.6", "stance": "Efficiency gains from sparsity do not reduce memory bandwidth costs for 70B weights"}]}

**unique_insights:**
  - {"model": "z-ai/glm-5.1", "insight": "H100 cluster-level power per GPU reaches ~1500W vs. 700W chip TDP"}
  - {"model": "moonshotai/kimi-k2.6", "insight": "Data movement consumes ~90% of inference energy in conventional systems"}
  - {"model": "deepseek/deepseek-v4-pro", "insight": "Mapping efficiencies below 1% for standard neural networks on neuromorphic chips"}

**blind_spots:**
  - Impact of different inference frameworks (TensorRT-LLM vs. PyTorch) on energy measurements
  - Recent developments in analog compute-in-memory for dense matrix operations
  - Commercial viability of multi-chip scaling for 70B models
  - Role of software optimizations in production inference serving
  - Energy costs of inter-chip communication for tensor parallelism

**partial_coverage:**
  - {"models": ["z-ai/glm-5.1"], "point": "Lack of specific documentation standards for VC due-diligence teams"}
  - {"models": ["moonshotai/kimi-k2.6"], "point": "Process node and silicon area transparency requirements"}

### C5inv_dumbpanel_smartjudge
_глупая панель + умный судья (qwen-2.5-7b → gemma-3-12b-it)_  
panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1 | cost=$0.1240 | 235.4s | ptok=21343 ctok=4425 | retries=0

**consensus:**
  - System-level power measurement (including host, memory, interconnect, cooling) is essential; chip-only metrics are misleading for cross-vendor comparisons.
  - Precision/format asymmetry is a common failure mode—comparing low-precision neuromorphic output to higher-precision GPU output inflates efficiency claims.
  - Cherry-picked or narrow workloads that favor neuromorphic architectures (sparse, event-driven) over dense transformer workloads invalidate general claims.
  - Transparent, reproducible methodology with explicit measurement boundaries, workload specifications, and what is excluded is required for any extraordinary claim.
  - The 1000x magnitude is far beyond what any documented neuromorphic result has achieved for transformer inference, requiring extraordinary evidence.

**contradictions:**
  - {"topic": "Typical neuromorphic energy efficiency gains", "stances": [{"model": "glm-4.7-flash", "stance": "Neuromorphic chips typically achieve 2-3x energy efficiency improvements at best."}, {"model": "evidence", "stance": "NorthPole achieves 72.7x over H100 for 3B-parameter LLM inference (HPEC 2024); Loihi 2 achieves 5600x for spike-native continual learning tasks. The 2-3x figure only applies to Loihi 2 running LLMs vs edge GPUs, not the full range of neuromorphic results."}]}
  - {"topic": "H100 energy efficiency for 70B models", "stances": [{"model": "glm-4.7-flash", "stance": "H100 achieves 0.08-0.14 tokens/second per watt for 70B models."}, {"model": "evidence", "stance": "H100 SXM5 with TP=8 achieves ~7.41 tok/W for 70B at 8K context (1/W Law paper, arxiv 2603.17280); the 0.08 figure applies to single PCIe GPU configurations that are memory-constrained, not production deployments."}]}
  - {"topic": "NorthPole efficiency over H100", "stances": [{"model": "qwen3-8b", "stance": "NorthPole achieves 5x energy efficiency over H100."}, {"model": "evidence", "stance": "The 5x figure is from the Science paper for ResNet50 (image classification); the 72.7x figure is from HPEC 2024 for 3B-parameter LLM inference at a specific low-latency operating point. These are different workloads and operating regimes—conflating them is misleading."}]}

**unique_insights:**
  - {"model": "glm-4.7-flash", "insight": "The neuromorphic 'memory wall': on-chip SRAM limitations make it extremely difficult to handle the large state vectors required for transformer inference, and the KV cache mechanism for autoregressive generation is fundamentally at odds with neuromorphic architectures that store parameters and states locally in neuro-cores."}
  - {"model": "qwen3-8b", "insight": "TDP vs actual power draw discrepancy: manufacturer TDP specs diverge significantly from real-world power consumption, which is workload-dependent, and there is no universal standard for energy efficiency reporting in AI inference."}

**blind_spots:**
  - Context length's massive impact on energy efficiency: the 1/W Law shows tok/W for 70B on H100 drops ~12x from 4K to 64K context. A 1000x claim could be manufactured by comparing a neuromorphic chip at short context against an H100 at very long context, or vice versa.
  - Multi-chip scaling energy costs: running 70B models on neuromorphic hardware requires partitioning across many chips (NorthPole needs 288 cards for some configurations). Inter-chip communication energy and latency are never accounted for in per-chip efficiency claims.
  - Accuracy/quality equivalence under extreme quantization: neuromorphic hardware typically requires aggressive quantization (NorthPole uses w4a4; Loihi 2 uses ternary weights). Comparing this to FP16/BF16 GPU output is not 'equivalent throughput' if output quality differs. No model demands quality-matched benchmarks.
  - Batch size asymmetry: GPU energy efficiency improves dramatically with batch size (25-40% reduction in energy per token from batch 32 to 256). Neuromorphic claims may exploit GPU batch=1 scenarios while using internally parallel neuromorphic processing.
  - Prefill vs decode phase distinction: these phases have fundamentally different compute/memory profiles. NorthPole's efficiency advantage applies primarily to decode; claims may cherry-pick one phase or misrepresent combined performance.
  - Compilation and model adaptation overhead: mapping standard transformer architectures to neuromorphic hardware requires extensive model transformation (e.g., MatMul-free architectures, spike encoding). The engineering cost and fidelity loss of this adaptation are never quantified in efficiency claims.

**partial_coverage:**
  - {"models": ["glm-4.7-flash"], "point": "KV cache management is particularly challenging for neuromorphic hardware: autoregressive generation requires maintaining large state vectors across tokens, and if off-chip memory access is needed, energy benefits largely evaporate."}
  - {"models": ["qwen3-8b"], "point": "NeuroBench methodology provides a multidimensional benchmarking framework (task quality, latency, power, model footprint) with explicitly defined measurement boundaries."}
  - {"models": ["glm-4.7-flash"], "point": "Software ecosystem immaturity—lack of mature tooling, limited talent pool, and incompatibility with PyTorch/CUDA—is a major practical barrier that efficiency claims ignore."}
  - {"models": ["qwen3-8b"], "point": "NorthPole's efficiency gains are attributable to architecture optimizing memory bottlenecks (eliminating off-chip memory, intertwining compute with on-chip memory), not fabrication node advantages (12nm vs 4nm)."}
  - {"models": ["gemma-3-12b-it"], "point": "Accuracy trade-offs are often obscured—significant energy savings on neuromorphic hardware frequently come at the cost of reduced model quality, and quality-matched comparisons are rare."}

### C6_echo
_контроль: эхо-камера_  
panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507 | cost=$0.0595 | 328.7s | ptok=34071 ctok=2215 | retries=0

**consensus:**
  - To take the startup's energy efficiency claim seriously, rigorous technical documentation is required, including detailed benchmarks using standard models like ResNet-50 or transformer variants for LLMs, verification of co-optimized hardware and software, and full system power reporting. Common pitfalls that invalidate such claims involve benchmarking different tasks or models, unfair power measurement (excluding system overhead), and model-hardware co-design that doesn't generalize. Real-world advantages of neuromorphic chips like IBM NorthPole and Intel Loihi 2 are workload-specific, excelling in energy efficiency (up to 25–72x) and latency (sub-millisecond) under specific conditions due to architectural innovations like compute-in-memory and event-driven processing, but they require specific model types (e.g., SNNs or MatMul-free LLMs) and often do not generalize across arbitrary architectures or tasks.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - The efficiency of neuromorphic claims critically depends on the equivalence of models and tasks: benchmarks pitting an SNN or MatMul-free model against a transformer on different input conditions (e.g., sparse vs. dense data) are invalid. True claims require identical models deployed on both hardware types, as demonstrated by the MatMul-free LLM comparison across Loihi 2 and H100.
  - Power measurement is often manipulated—leadership claims use only chip or dynamic power, whereas credible reports must include full system power (including memory, interconnect, and scheduling), which significantly reduces the apparent efficiency gains. NorthPole claims include board-level power, making them more trustworthy.
  - Architectural specialization (e.g., IBM’s compute-in-memory or Intel’s event-driven SNNs) provides efficiency only when matched with specific workloads. These benefits diminish or reverse under dense data loads where GPUs saturate due to abundant parallel cores, revealing the fundamental limitation of neuromorphic hardware: advantage is context-bound, not universal.
  - Model-hardware co-design is a major blind spot—efficiency gains are often only possible via tightly customized microcode, quantization schemes, or software pipelining incompatible with standard deep learning frameworks. This leads to vastly inflated 'efficiency' numbers that collapse under any portability or real-world generalization requirement.

**blind_spots:**
  - The documentation requirement analysis does not consider real-world deployment constraints such as software maturity (e.g., sparse support for SNNs in PyTorch/TensorFlow), developer access to low-level microcode, or availability of production-ready board-level power measurement tools, which are crucial for replicability and adoption.
  - The top 3 pitfalls analysis focuses on measurement and model equivalence but underplays the role of proprietary hardware/software stacks (like Hala Point or NxCore) that make independent validation nearly impossible, especially for startups without public toolchains.

**partial_coverage:**
  - The comparison of NorthPole and Loihi 2 provides strong empirical evidence for neuromorphic advantages but is limited to inference tasks like image classification (ResNet-50, YOLO-v4) and MatMul-free LLMs, and does not address training, scalability, or dynamic workloads like varying batch sizes in production environments.
  - Efficiency claims for LLM inference are illustrated via a MatMul-free model (370M parameters), but the startup claims involve 70B models, representing a 200x scale difference. The documentation and validation standards derived do not explicitly address scalability to such massive models, which may suffer from routing or memory bottlenecks not present in smaller demonstrations.

### C3_cn_small
_всё мелкое_  
panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b | cost=$0.0631 | 769.6s | ptok=48288 ctok=17866 | retries=1

**consensus:**
  - Technical documentation must include detailed energy/accuracy curves, batch size/latency data, and memory bandwidth specifications.
  - Claims of 1000x energy efficiency require fair comparisons (identical quantization, H100 configuration) to avoid methodological flaws.
  - Common claim failures involve on-chip vs. system-level power measurements, memory wall limitations, and mismatch between neuromorphic/SNN optimization and dense transformers.
  - Neuromorphic efficiency gains often depend on architectural innovations (e.g., compute-in-memory) or MatMul-free models, which are not standard for transformers.

**contradictions:**
  - {"topic": "Benchmarks and generalizability", "stances": [{"model": "qwen/qwen3-32b", "stance": "Highlights VDE SPEC and LOKI benchmarks but questions their LLM-specific relevance"}, {"model": "z-ai/glm-4.7-flash", "stance": "Notes IBM NorthPole's 72x transformer claim but rejects 1000x as extraordinary"}, {"model": "evidence", "stance": "Recent papers show 72x efficiency claims remain state-of-the-art, while 1000x violates known physics for memory-bound workloads"}]}

**unique_insights:**
  - {"model": "z-ai/glm-4.7-flash", "insight": "The 72x NorthPole claim demonstrates neuromorphic potential for transformed transformer architectures (MatMul-free), but 1000x would require fundamentally new computation models"}
  - {"model": "qwen/qwen3-32b", "insight": "LOKI's 0.266 pJ/SOP efficiency depends on clock-gated SRAM and task-specific sparsity, which may not scale to LLMs without major architectural trade-offs"}

**blind_spots:**
  - Impact of data center interconnects and distributed inference on claimed efficiency metrics
  - Thermal throttling characteristics under sustained high-throughput workloads
  - Software ecosystem maturity (e.g., PyTorch integration, quantization tools) for neuromorphic systems
  - Cost of transitioning from von Neumann to neuromorphic deployment in existing infrastructure

**partial_coverage:**
  - {"models": ["qwen/qwen3-32b"], "point": "Cites specific benchmarks (LOKI, VDE SPEC, NorthPole, Akida) and scaling bottlenecks in multi-chip systems not mentioned in other responses"}
  - {"models": ["z-ai/glm-4.7-flash"], "point": "Emphasizes software stack maturity and thermal management impact on sustained throughput"}
  - {"models": ["qwen/qwen3.6-27b"], "point": "Focuses on memory architecture (HBM vs system RAM) and CIM validation"}


---
## BASELINE (одиночная модель, без fusion)

### B_cn  (model=deepseek-v4-pro | cost=$0.0041 | 65.0s)
To take such a claim seriously, I’d need to see very specific technical documentation that goes far beyond a single cherry-picked benchmark. Here’s what I’d look for, followed by the most common ways these claims collapse.

### What the Technical Documentation Must Show

1.  **A Rigorous, Apples-to-Apples Throughput Definition:**
    - **Identical Task:** The comparison must be for an identical, real-world task. It can’t be “our chip doing 8-bit integer math vs. H100 doing 64-bit floating point.” It must be the same model architecture (a standard 70B LLaMA or equivalent), the same dataset, and the same precision (e.g., FP8, INT8, or FP16). If they use a sparse model, the H100 must also run a sparse model.
    - **End-to-End Inference, Not Just Matrix Multiplication:** The throughput must be measured for a complete inference run, including tokenization, embedding lookup, all transformer layers, and final logit generation. A claim based solely on the energy of a single matrix multiply is a non-starter.
    - **Realistic Batch Size:** The benchmark must show the claimed efficiency at a commercially relevant throughput. A common trick is to show extreme energy efficiency at a batch size of 1, where the H100 is severely underutilized. I need to see the efficiency at the batch size that achieves the “equivalent throughput” they claim—for a 70B model, this could be a batch size of 32 or 64, where GPUs are much more efficient.

2.  **A Fully Burdened, System-Level Power Measurement:**
    - **Not Just Chip Power:** The power measurement must be for the entire inference system required to run the model, not just the neuromorphic chip’s TDP. This includes host CPU, DRAM, interconnects, and crucially, any external FPGA or microprocessor needed to manage the neuromorphic chip’s data flow. The H100’s power is always measured at the system level (e.g., a DGX H100’s total power).
    - **Quantized Model and Hardware Link:** The documentation must prove the 70B model is fully quantized and running entirely on the neuromorphic hardware. If the attention mechanism or a critical non-MVM (matrix-vector multiplication) operation runs on a co-processor, that power must be included.

3.  **Proof of Algorithmic Equivalence and Accuracy:**
    - **Accuracy Parity:** The claim is meaningless if the neuromorphic chip achieves its efficiency by sacrificing output quality. The documentation must show that the perplexity on a standard benchmark (e.g., WikiText-2) and the zero-shot accuracy on a suite like MMLU or HellaSwag are within a few percent of the H100 baseline running the same model in FP16.
    - **Deterministic or Tolerable Stochasticity:** Many neuromorphic systems are inherently stochastic. The documentation must explain how they guarantee a consistent, high-quality output for a given prompt, and show the variance in output quality is negligible.

### Top 3 Ways Such Claims Fall Apart Under Scrutiny

The most common failure modes are almost always in the fine print of the comparison:

1.  **The “Apples-to-Oranges” Workload Mismatch:** This is the most pervasive trick. The startup benchmarks a highly specialized, quantized, and pruned version of the 70B model on their chip, while running a dense, unoptimized FP16 model on the H100. A fair comparison would require the H100 to run the exact same optimized model. When the H100 is given the same 4-bit or 8-bit quantized model, its throughput skyrockets and its energy per query plummets, often erasing the claimed 1000x advantage. The claim is not about chip vs. chip, but about a model optimization technique vs. an unoptimized baseline.

2.  **The “Batch Size 1” Trap:** This is the classic startup demo pitfall. A neuromorphic chip might be incredibly energy-efficient when processing a single stream of tokens (batch size 1) because it has no compute overhead. An H100 at batch size 1 is a worst-case scenario, as its massive parallel compute sits idle. The 1000x claim is often true only at this unrepresentative operating point. The moment you scale to a production environment with multiple concurrent users, the H100’s throughput scales almost linearly with batch size, while the neuromorphic chip’s throughput might be capped by its limited on-chip memory or single-core performance. The claimed advantage evaporates at any commercially viable throughput.

3.  **The “System vs. Chip” Power Shell Game:** The startup measures the milliwatts of power dissipated by their neuromorphic core during the matrix-vector multiplications. They then compare this to the 700W peak TDP of an entire H100 SXM module. This ignores the power of the host server, DRAM, and network card required to feed data to the H100, but more critically, it ignores the power of the massive digital control system, SRAM/DRAM, and data-shuffling co-processors required to make their own neuromorphic chip work. A true system-level measurement, where you measure the AC power at the wall for both fully-configured, commercially-relevant systems running the same task, is where the 1000x claim collapses into a much smaller, often negligible, single-digit improvement.

### B_west  (model=gpt-5.2 | cost=$0.0211 | 31.6s)
### What you’d need to see in their technical docs to take “1000× better than H100 on 70B transformer inference at equivalent throughput” seriously

#### 1) A precise, apples-to-apples workload definition (tokens/s *and* latency, not just “throughput”)
They must fully specify the inference scenario, because transformer “throughput” changes by orders of magnitude depending on details:

- **Model**: exact model (e.g., Llama-2 70B vs Llama-3 70B), dense vs MoE, any pruning/sparsity, any weight sharing, etc.  
- **Numerics**: weight precision (FP16/FP8/INT8/INT4), activation precision, KV-cache precision, any mixed precision.  
- **Accuracy parity**: perplexity / downstream evals vs a reference implementation. If they use approximations (neuromorphic/nonlinearities), show the quality impact.  
- **Sequence lengths**: prompt length and generation length (e.g., prefill 2k tokens + decode 512 tokens). Prefill vs decode are very different regimes.  
- **Batching**: batch size, number of concurrent sequences, and how they handle continuous batching.  
- **Serving constraints**: latency targets (p50/p95/p99), not just average. Equivalent throughput is meaningless if one system is allowed 10× the latency.  
- **What exactly is measured**: prefill only, decode only, or end-to-end (prefill+decode). “Transformer inference” often quietly means *decode-only*.

What you want is: **tokens/s at stated latency percentiles for a fully specified (prompt_len, gen_len, batch/concurrency) profile**, plus **energy per generated token** for that same profile.

#### 2) Reproducible benchmarking details, including a fair H100 baseline
To compare against H100 credibly, they must show:

- **Exact H100 configuration**: SXM vs PCIe, power limit, clocks, memory size, number of GPUs, interconnect (NVLink), host CPU, RAM.  
- **Software stack on H100**: TensorRT-LLM / vLLM / FasterTransformer, CUDA version, kernels used, attention implementation (FlashAttention, paged attention), quantization method.  
- **A “best known practice” baseline**: If they compare against an unoptimized FP16 PyTorch baseline, that’s not meaningful.  
- **Same model + same accuracy target**: If their chip runs INT4 with quality loss but H100 baseline is FP16, it’s not equivalent. If they use structured sparsity, compare to H100 with sparse kernels enabled where applicable.  
- **Code / scripts / configs**: Enough that a third party could rerun both sides and reproduce tokens/s and joules/token.

Ideally: a public benchmark harness + configs + commit hashes.

#### 3) Real power measurement methodology (not “TDP” and not “core-only”)
A 1000× energy-efficiency claim lives or dies on measurement boundaries.

You’d need:

- **Measurement boundary** clearly defined:  
  - chip-only, module, board, or **wall-plug** (PSU input).  
  - whether **HBM/DRAM** power is included (it must be for transformer inference).  
  - whether host CPU power is included (for a *system* claim, it should be).  
- **Instrumentation**: shunt + ADC specs, sampling rate, calibration, error bars, logging methodology, how they handle transient power during prefill bursts.  
- **Power breakdown**: compute vs memory vs interconnect, plus utilization over time.  
- **Thermal steady-state**: results after warm-up at sustained load (many chips look great for seconds, then throttle).

The key metric you want is **J/token (or tokens/J)** *for the same workload definition* above.

#### 4) Evidence it’s not just a model/simulation extrapolation
For a startup, it’s common that “results” are a mix of partial silicon + simulation.

To take it seriously, you’d want:

- **Silicon-measured performance and power** at the claimed operating point (frequency, voltage, temperature).  
- If any extrapolation is used: clear separation of *measured* vs *projected*, with scaling assumptions justified (memory bandwidth, interconnect, yield/variation, clocking).  
- **Constraints**: on-chip SRAM/HBM size, off-chip bandwidth, KV-cache storage strategy, and how that affects long-context inference.

#### 5) A clear mapping of transformer operations to their “neuromorphic” architecture
Transformers are dominated by GEMMs and memory traffic, plus attention/KV cache behavior.

They need to
