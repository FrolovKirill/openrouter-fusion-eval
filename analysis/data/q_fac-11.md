# fac-11 — Two's complement 8-bit range
**Block:** factual  |  **difficulty:** hard

**Prompt:**
In 8-bit two's complement representation: (1) what is the exact range of representable integers? (2) What is the 8-bit binary representation of the most negative number? (3) Why is there no positive counterpart to the most negative number?

**Expected answer (эталон):**
(1) -128 to +127. (2) Most negative is -128 = 10000000₂. (3) There are 256 bit patterns total: one is 0, leaving 255 for positive/negative — split as 127 positive and 128 negative. The two's complement of -128 overflows back to -128 (10000000 → invert → 01111111 → +1 → 10000000), so +128 cannot be represented.

---
## FUSION-конфиги (judge-анализ; responses вынесены в resp_*.md)

### C1_west_closed
_западный закрытый фронтир_  
panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2 | cost=$0.0978 | 172.8s | ptok=15222 ctok=2969 | retries=0

**consensus:**
  - 8-bit two’s-complement integers range exactly from −128 to +127 inclusive (i.e., −2^7 to 2^7−1).
  - The most negative representable value is −128 and its 8-bit pattern is 10000000.
  - There is no representable +128 in 8-bit two’s complement, so −128 has no positive counterpart; attempting to negate −128 overflows (in fixed 8-bit arithmetic) and yields 10000000 again.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "x-ai/grok-4.3", "insight": "Frames the overflow on negating the minimum as a carry/overflow phenomenon at the sign bit (carry into but not out / overflow on two’s-complement negation), tying the no-+128 fact to fixed-width ALU behavior."}

**blind_spots:**
  - No response explicitly states the defining value-decoding rule for two’s complement (e.g., interpreting bits as an unsigned value minus 2^n when MSB=1, or as a weighted sum with MSB weight −2^(n−1)), which would make the conclusions fully derivable from first principles.
  - No response distinguishes mathematical integers from fixed-width modular arithmetic: two’s-complement bit patterns form Z/(2^n)Z under addition; the ‘negation of −128 equals itself’ is a modulo-256 artifact plus an out-of-range interpretation issue.
  - No response discusses real-world language/ISA handling of this overflow (e.g., CPU overflow flags vs. language-level undefined/defined behavior), which matters for why abs(INT_MIN) can be problematic in practice.
  - No response contrasts with alternative signed encodings (sign-magnitude, ones’ complement) to highlight that symmetry can be achieved only by introducing a second zero or different trade-offs.

**partial_coverage:**
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "States the general n-bit two’s-complement range formula: −(2^(n−1)) to (2^(n−1))−1."}
  - {"models": ["google/gemini-3.1-pro-preview", "x-ai/grok-4.3"], "point": "Gives an explicit worked negation procedure (invert bits + add 1) showing 10000000 maps back to itself under 8-bit wraparound."}

### C2_cn_open
_открытый китайский фронтир (умн+умн)_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507 | cost=$0.0397 | 215.0s | ptok=18722 ctok=3697 | retries=0

**consensus:**
  - The exact range of representable integers in 8-bit two's complement is -128 to +127.
  - The most negative number, -128, is represented in binary as 10000000.
  - There is no positive counterpart (+128) because the total number of distinct bit patterns (256) must include zero, leaving 127 patterns for positive numbers and 128 for negative numbers, which results in an asymmetry favoring one extra negative value.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "moonshotai/kimi-k2.6", "insight": "The absence of a positive counterpart to -128 is not a bug but a deliberate consequence of using a single representation for zero; sign-magnitude systems waste a pattern on negative zero, whereas two's complement reclaims that pattern to extend the negative range by one, making the representation more efficient."}
  - {"model": "z-ai/glm-5.1", "insight": "In the modular arithmetic model of two's complement, +128 and -128 are congruent modulo 256, meaning they occupy the same residue class and thus the same bit pattern, which explains why +128 cannot have a distinct representation."}

**blind_spots:**
  - None of the models addressed the real-world software implications of the non-negatable most negative number, such as how languages like C define signed integer overflow as undefined behavior, potentially leading to security vulnerabilities or optimizer-induced bugs when negating INT_MIN.
  - No model discussed the hardware design perspective on why two's complement simplifies arithmetic logic units (ALUs) by eliminating conditional logic for addition/subtraction based on sign.
  - The historical context of why two's complement became the standard (e.g., System/360 adoption, PDP minicomputers) was only lightly touched by external sources, but not within the model responses, limiting ontological grounding in engineering causality.
  - The mathematical generalization to n-bit systems was mentioned, but no model derived the range from first principles using modular arithmetic or group theory, which would ground the explanation in abstract algebra.

**partial_coverage:**
  - {"models": ["deepseek/deepseek-v4-pro", "z-ai/glm-5.1"], "point": "The modular arithmetic explanation that +128 ≡ -128 (mod 256), meaning both values map to the same bit pattern under 8-bit two's complement, was explicitly detailed by z-ai/glm-5.1 and touched on by deepseek/deepseek-v4-pro."}
  - {"models": ["z-ai/glm-5.1"], "point": "z-ai/glm-5.1 uniquely emphasized the overflow detection mechanism during negation (carry in but no carry out of the sign bit) as a concrete hardware-level indicator of the impossibility of representing +128."}
  - {"models": ["moonshotai/kimi-k2.6"], "point": "moonshotai/kimi-k2.6 included meta-level observations about the panel consensus and unique insights across models, framing the asymmetry as a deliberate design trade-off to have a single zero representation, which avoids the inefficiency of ±0 in sign-magnitude systems."}

### C5_smartpanel_dumbjudge
_умная панель + глупый судья_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b | cost=$0.0138 | 146.0s | ptok=12082 ctok=2015 | retries=0

**consensus:**
  - The range is [-128, 127]
  - The most negative number is 10000000
  - No positive counterpart for -128 due to zero's slot and 8-bit limitation

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
panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1 | cost=$0.0340 | 319.4s | ptok=18234 ctok=3604 | retries=1

**consensus:**
  - The 8-bit two's complement range is -128 to 127.
  - The most negative number is -128, represented as 10000000 in binary.
  - There is no positive counterpart to -128 because +128 exceeds the maximum representable positive value of 127.

**contradictions:**
  - {"topic": "Explanation for the asymmetry between positive and negative ranges", "stances": [{"model": "qwen/qwen3-8b", "stance": "Claims 'the positive range (0-127) has one more value than the negative range (-1 to -128)' — this is factually incorrect; both ranges contain exactly 128 values each."}, {"model": "evidence", "stance": "0-127 has 128 values; -1 to -128 has 128 values. They are equal. The real asymmetry is that the most negative number (-128) lacks a positive counterpart, while every other negative number has one."}]}
  - {"topic": "Binary representation of 128 and two's complement derivation for -128", "stances": [{"model": "google/gemma-3-12b-it (panel model 2)", "stance": "Claims 'the binary representation of 128 (01000000), invert it (10111111), and add 1 (10000000).' Three errors: 01000000 is 64 not 128; 10111111 + 1 = 11000000 not 10000000; +128 cannot be represented in 8-bit two's complement, so the standard negation algorithm cannot be applied to it."}, {"model": "evidence", "stance": "01000000 = 64 in unsigned binary. 128 would be 10000000 in unsigned, but in two's complement that pattern is already -128. The negation algorithm applied to 64 gives 11000000 = -64, not -128."}]}

**unique_insights:**
  - {"model": "z-ai/glm-4.7-flash (Model C)", "insight": "Flipping the sign bit of 10000000 produces 00000000 (=0), not +128 — this directly exposes why sign-magnitude intuition fails for two's complement and reveals the encoding's fundamental asymmetry."}
  - {"model": "z-ai/glm-4.7-flash", "insight": "The 'positive counterpart' is a mathematical abstraction that fails under fixed-width constraints; -128 is the negation of +128, but +128 cannot be encoded within 8 bits, making the counterpart relation physically impossible in this representation."}

**blind_spots:**
  - No model explains the ROOT CAUSE of the asymmetry: zero occupies exactly one bit pattern in two's complement (unlike sign-magnitude's two zeros), so with 2^8=256 patterns, zero takes 1, leaving 255 for non-zero values split as 128 negative + 127 positive — zero 'steals' one slot from what would otherwise be +128.
  - No model provides the algebraic interpretation of two's complement: value = -b7×2^7 + Σ(bi×2^i for i=0..6), which makes the asymmetry a direct mathematical consequence: minimum = -2^7 = -128, maximum = 2^7 - 1 = 127.
  - No model mentions the self-negation paradox: in 8-bit two's complement, the two's complement negation of 10000000 yields 10000000 (itself), meaning -(-128) = -128 due to overflow — a direct demonstration of why the positive counterpart is structurally impossible.
  - No model discusses practical consequences such as undefined behavior when negating INT_MIN in C/C++, or the historical design rationale favoring two's complement (single zero, unified adder circuitry for signed/unsigned arithmetic).

**partial_coverage:**
  - {"models": ["z-ai/glm-4.7-flash"], "point": "+128 requires 9 bits (100000000) to represent, which exceeds the 8-bit fixed-width constraint — the most precise mechanistic explanation for why the positive counterpart is impossible."}
  - {"models": ["z-ai/glm-4.7-flash"], "point": "Flipping the sign bit of 10000000 yields 00000000 (=0), not +128, demonstrating that naive sign-magnitude reasoning fails in two's complement."}
  - {"models": ["google/gemma-3-12b-it"], "point": "Visual mapping of bit patterns: positive numbers 00000001–01111111, negative numbers 10000000–11111111, showing the complete allocation of the 256 bit patterns."}

### C6_echo
_контроль: эхо-камера_  
panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507 | cost=$0.0447 | 239.6s | ptok=18890 ctok=3739 | retries=0

**consensus:**
  - The range of representable integers in 8-bit two's complement is from -128 to +127.
  - The 8-bit binary representation of the most negative number (-128) is 10000000.
  - There is no positive counterpart to -128 because +128 cannot be represented within 8 bits, as the maximum positive value is +127, and the bit pattern 10000000 is already assigned to -128.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "qwen/qwen3-235b-a22b-2507", "insight": "The representation 10000000 is unique in that its two's complement is itself, highlighting an inherent overflow condition in the negation of the most negative number."}
  - {"model": "qwen/qwen3-235b-a22b-2507", "insight": "The asymmetry in the two's complement range (128 negative values vs. 127 positive) arises because zero occupies one slot, leaving an odd number of nonzero values, which forces one negative number (-128) to be its own additive inverse."}

**blind_spots:**
  - No model explicitly discusses the historical or engineering rationale for choosing two's complement over alternatives like one's complement or sign-magnitude beyond arithmetic simplicity and single zero representation.
  - None address the behavior of modern processors when operations overflow on the most negative number, such as how CPU flags (e.g., overflow flag) are set during negation of -128.
  - No model mentions that the lack of a positive counterpart to -128 is a general property of all even-bit two's complement systems, not specific to 8 bits.
  - There is no discussion of how programming languages handle this edge case, e.g., undefined behavior in C when negating INT_MIN, or how safe integer libraries mitigate it.

**partial_coverage:**
  - {"models": ["qwen/qwen3-235b-a22b-2507"], "point": "The two's complement of -128 is itself, demonstrating overflow when negation is attempted."}
  - {"models": ["qwen/qwen3-235b-a22b-2507"], "point": "The most significant bit in two's complement has a negative weight of -2^(n-1), which directly explains why 10000000 equals -128."}

### C3_cn_small
_всё мелкое_  
panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b | cost=$0.0176 | 305.0s | ptok=14467 ctok=2662 | retries=0

**consensus:**
  - The 8-bit two's complement range of integers is from -128 to 127 inclusive.
  - The 8-bit binary representation of the most negative number (-128) is 10000000.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "z-ai/glm-4.7-flash", "insight": "The bit pattern 10000000 has a dual conflict: it represents both the unsigned value 128 and the signed value -128 in 8-bit two's complement, forcing an implicit design choice to prioritize negative overflow."}

**blind_spots:**
  - No model explicitly contrasts two's complement with alternative representations (e.g., one's complement or sign-magnitude) to contextualize its asymmetry.
  - The practical reasons for two's complement's design (e.g., simplification of arithmetic hardware) are not addressed.
  - The necessity of 9 bits for +128 is stated descriptively but not abstractly generalized to how bit allocation defines representable ranges across widths.

**partial_coverage:**
  - {"models": ["qwen3-32b"], "point": "The asymmetry arises because zero is allocated only one representation (00000000), leaving 128 positive and 128 non-negative values but 128 negative representations."}
  - {"models": ["z-ai/glm-4.7-flash"], "point": "Negating -128 via two's complement (inversion + addition) results in the same bit pattern (10000000), demonstrating the lack of a positive counterpart."}


---
## BASELINE (одиночная модель, без fusion)

### B_cn  (model=deepseek-v4-pro | cost=$0.0007 | 8.2s)
**1. Exact range of representable integers:**  
From **‑128** to **127** (inclusive).  

**2. 8‑bit binary representation of the most negative number:**  
`10000000` (represents –128).  

**3. Why is there no positive counterpart to the most negative number?**  
In two’s complement, the negative of a number is obtained by inverting all bits and adding 1. Applying this to `10000000` gives `01111111 + 1 = 10000000`—it negates to itself. The value is –128, so its positive counterpart would be +128. However, with 8 bits the largest positive integer is `01111111` = +127. The pattern `00000000` is reserved for zero, and the remaining 128 patterns are split asymmetrically: one for –128 and 127 for the positive numbers 1…127. Thus +128 falls outside the representable range, leaving –128 without a matching positive number.

### B_west  (model=gpt-5.2 | cost=$0.0041 | 5.8s)
1) **Exact range (8-bit two’s complement):**  
\[
-2^{7} \text{ to } 2^{7}-1 \;=\; -128 \text{ to } +127
\]

2) **8-bit binary of the most negative number (-128):**  
\[
1000\;0000_2
\]

3) **Why there’s no positive counterpart (+128 doesn’t exist):**  
With 8 bits there are \(2^8 = 256\) total patterns. In two’s complement, half are negative and half are non-negative, but **zero takes one of the non-negative slots**. That leaves:
- **128** negative values: \(-128\) through \(-1\)
- **128** non-negative values: \(0\) through \(+127\)

So there are **more negative values by one**. The bit pattern for \(-128\) is `10000000`; trying to negate it (take two’s complement) gives:
- invert: `01111111`
- add 1: `10000000` (wraps back to itself in 8 bits)

So \(-128\) is its own negation in 8-bit arithmetic, and **+128 is not representable** (it would require a 9th bit).
