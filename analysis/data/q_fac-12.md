# fac-12 — Therac-25 root software cause
**Block:** factual  |  **difficulty:** very-hard

**Prompt:**
The Therac-25 radiation therapy machine caused severe overdoses and deaths in 1985–1987 due to a software defect. Describe the specific programming error with the flag variable: what was done wrong, what arithmetic condition caused the safety checks to be bypassed, and how did operator typing speed trigger it?

**Expected answer (эталон):**
The software set a safety flag by *incrementing* it (flag++) rather than assigning a fixed non-zero value. If the operator typed commands fast enough (within ~8 seconds), a race condition caused the flag to be incremented to 255 and then overflow to 0 on the next increment — making the safety interlock treat the situation as 'no hazard present' and proceed with full-power electron beam without the beam spreader.

---
## FUSION-конфиги (judge-анализ; responses вынесены в resp_*.md)

### C1_west_closed
_западный закрытый фронтир_  
panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2 | cost=$0.2191 | 583.7s | ptok=19928 ctok=4464 | retries=1

**consensus:**
  - The defect centered on a 1-byte shared “flag” variable (often documented as Class3) that should have been set to a fixed nonzero value to force an upper-collimator safety check, but was instead incremented on each pass through the Set-Up Test routine (verified in Leveson & Turner’s AECL/FDA-derived description).
  - Because the variable was 8-bit, repeated incrementing overflowed/wrapped modulo 256 (255 → 0 on the next increment), producing a zero value at predictable intervals (every 256 passes) rather than representing a stable boolean state (verified).
  - A zero value was treated by the interlock logic as “no inconsistency / safe,” and in that state the relevant collimator-check routine was skipped, allowing treatment to proceed without detecting the unsafe upper-collimator/turntable configuration (verified: Lmtchk bypasses Chkcol when Class3==0).
  - The operator-triggered aspect was timing: the accident required the operator to press “set” during the brief cycle when Class3 had just wrapped to 0, so the safety check was bypassed for that cycle (verified: “hit the ‘set’ button at the precise moment that Class3 rolled over to zero”).

**contradictions:**
  - {"topic": "Arithmetic mechanism (overflow vs underflow; increment vs decrement; which value bypasses checks)", "stances": [{"model": "openai/gpt-5.2", "stance": "Incrementing an 8-bit variable caused overflow/wrap (255→0), and Class3==0 bypassed the collimator check."}, {"model": "google/gemini-3.1-pro-preview", "stance": "An 8-bit variable was incremented, overflowed at 256, wrapped to 0, and 0 was interpreted as safe."}, {"model": "x-ai/grok-4.3", "stance": "Describes a decrement/underflow (0→255) and implies non-zero/stale values bypass checks."}, {"model": "evidence", "stance": "Set-Up Test increments Class3; as a 1-byte value it overflows every 256th pass to 0; when Class3==0, Lmtchk bypasses Chkcol and the upper-collimator check is not performed."}]}
  - {"topic": "How “operator typing speed” triggers the bug (8-second fast-edit race vs ‘press set at rollover-to-zero’ window)", "stances": [{"model": "openai/gpt-5.2", "stance": "Trigger is pressing “set” at the precise moment the repeatedly incremented byte wraps to 0; characterizes this as timing-dependent rather than a fixed keystrokes-per-second threshold."}, {"model": "google/gemini-3.1-pro-preview", "stance": "Claims the trigger was typing faster than an ~8-second setup interval, framing it as a race condition tied to an 8-second timing window."}, {"model": "x-ai/grok-4.3", "stance": "Frames trigger primarily as a race where rapid typing causes stale flag reads/clears; no specific ‘set at wrap-to-zero’ mechanism."}, {"model": "evidence", "stance": "For the Class3 bug (Yakima flaw), the overexposure occurred when the operator hit “set” at the precise moment Class3 rolled over to zero; the well-known ~8-second ‘edit within 8 seconds’ issue pertains to a different Therac-25 software problem (Tyler), not this overflow-bypass mechanism."}]}
  - {"topic": "Whether the Class3 failure is best described as a race condition (concurrency) versus a deterministic overflow + wrong conditional", "stances": [{"model": "openai/gpt-5.2", "stance": "Explains a deterministic byte overflow producing Class3==0 that directly bypasses calling Chkcol; does not rely on a stale-read race to explain the bypass."}, {"model": "google/gemini-3.1-pro-preview", "stance": "Labels it as a race condition plus overflow without separating the deterministic overflow-bypass path from other Therac-25 races."}, {"model": "x-ai/grok-4.3", "stance": "Portrays it chiefly as a classic race condition on a shared flag (stale read before reset)."}, {"model": "evidence", "stance": "The documented bypass mechanism is: Class3 is incremented until it overflows to 0; Lmtchk checks Class3 and skips Chkcol when it is 0; the accident depends on operator action coinciding with that overflow-to-zero cycle. Concurrency exists (Housekeeper task performs interlock checks), but a stale-read/underflow story is not the documented mechanism."}]}

**unique_insights:**
  - {"model": "openai/gpt-5.2", "insight": "Highlights the critical semantic inversion: overflow doesn’t merely corrupt the value—it converts a ‘force-check’ nonzero condition into exactly the sentinel value (0) that the code uses to *skip* the check, creating predictable recurring vulnerable instants (every 256 passes)."}

**blind_spots:**
  - No response cleanly disentangles the Class3 overflow bug (Yakima/‘set’ at rollover-to-zero) from the separate “fast edit within ~8 seconds” Tyler bug involving Magnet/Ptime and edit-detection; this conflation matters because the prompt mentions typing speed.
  - None quote or cite the primary technical narrative (e.g., Leveson & Turner 1993 / AECL-to-FDA description) to anchor claims like the exact conditional (Class3==0 → bypass Chkcol) and the “hit set at the precise moment” trigger.
  - None explain precisely why operator speed matters probabilistically (many rapid Set-Up Test reschedules → recurring narrow windows; operator action must coincide with one of those windows), versus implying a deterministic typing-speed threshold.
  - None address the exact timing/frequency of the Set-Up Test loop and Housekeeper interlock polling rate, which is needed to rigorously relate ‘operator typing speed’ to likelihood of coinciding with the wrap-to-zero window.

**partial_coverage:**
  - {"models": ["openai/gpt-5.2"], "point": "Names the specific routines/variables in the documented chain (Housekeeper/Hkeper’s Lmtchk, Chkcol, and F$mal bit 9) and ties the bypass to ‘Chkcol not executed → F$mal not set.’"}
  - {"models": ["openai/gpt-5.2", "google/gemini-3.1-pro-preview"], "point": "Explicitly states the modulo-256 wraparound detail (255→0 on the 256th increment) rather than only saying “overflow happened.”"}

### C2_cn_open
_открытый китайский фронтир (умн+умн)_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507 | cost=$0.1295 | 251.6s | ptok=22952 ctok=1629 | retries=0

**consensus:**
  The Therac-25's most notorious software defect involved a flag variable (Class3) that was incremented instead of being set to a non-zero constant. This 1-byte variable overflowed after 255 increments, resetting to 0 and causing a safety interlock check to be skipped. The operator's action (pressing the 'set' button at the moment Class3 overflowed) triggered the overdose. A separate race condition, known as the Tyler accident, was triggered by fast typing: an operator could edit the treatment mode within the 8-second magnet-setting window, causing the software to miss the edit and proceed with inconsistent machine settings. The two defects are often conflated, but typing speed played a direct role only in the Tyler race condition, not in the flag-overflow flaw itself.

**contradictions:**
  Some popular accounts suggest that the flag variable overflow was directly triggered by operator typing speed. In reality, the Tyler accident (fast typing during data entry) and the Yakima accident (Class3 overflow upon pressing 'set') are distinct failures. The Tyler race did not involve the overflowing flag; it was a missing edit detection due to a flawed magnet subroutine. The flag-increment flaw was discovered after the Yakima overdose and involved pressing a button, not typing speed.

**unique_insights:**
  - The Class3 flag was incremented in a loop that ran hundreds of times during machine setup, so overflow occurred every 256th pass, making the safety bypass predictable yet hard to reproduce in testing.
  - The 8-second magnet-setting window in the Tyler accident created a narrow timing vulnerability that only fast typists could exploit, highlighting how operator proficiency could expose latent race conditions.
  - The fix was trivially simple: change the code from 'Class3 = Class3 + 1' to 'Class3 = 1' (or any fixed non-zero value), yet the complexity of real-time embedded multi-tasking made the flaw difficult to forecast.

**blind_spots:**
  - The original safety analysis assumed that software interlock variables could never fail in such a manner; no design review caught the lack of synchronization or the increment-instead-of-set logic.
  - Testing protocols did not include stress scenarios involving high-speed operator interaction or systematic exercising of integer overflow boundaries.
  - The manufacturer's initial corrective actions focused only on the Tyler race condition, leaving the identical pattern of 'increment to set' unchecked in other parts of the code.

**partial_coverage:**
  - Most summaries emphasize the Tyler accident (typing speed) because it was easier to reproduce and document. The Class3 overflow is often mentioned briefly, but its connection to the turntable field-light position and the exact sequence of events is rarely detailed.
  - The role of the shared memory model (no semaphores, non-atomic test-and-set) is underreported; many accounts treat each bug in isolation rather than as symptoms of a deeper concurrency design failure.

### C5_smartpanel_dumbjudge
_умная панель + глупый судья_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b | cost=$0.1277 | 422.8s | ptok=21556 ctok=1843 | retries=0

**consensus:**
  The Therac-25 accidents involved two distinct software defects related to flag variables and race conditions. Both ultimately allowed the high-current X‑ray mode electron beam to be delivered to patients without the tungsten target or beam spreader in place, causing massive radiation overdoses. The 'flag variable' error specifically refers to the Class3 variable in the Yakima accident, where an arithmetic overflow caused safety checks to be bypassed. Operator timing—rapid keystrokes in the Tyler accident and pressing 'set' at the exact moment of overflow in the Yakima accident—was critical to triggering both failures.

**contradictions:**
  Some sources conflate the two accidents. The Tyler accident involved a race condition with a Data‑entry completion flag triggered by fast typing (editing 'X' to 'E' within 8 seconds), while the Yakima accident involved the Class3 flag variable overflow triggered by pressing 'set' at the precise moment of the 256th pass through Set‑Up Test. The question mentions 'typing speed' with a 'flag variable' and 'arithmetic condition,' which blends symptoms from both bugs. In the Yakima accident, it was button‑press timing, not typing speed per se, that coincided with the arithmetic overflow.

**unique_insights:**
  - The Class3 flag variable was a 1‑byte shared variable incremented on every pass through the Set‑Up Test subroutine. Because it was incremented instead of being set to a fixed nonzero value, it could overflow from 255 back to 0 on every 256th pass, mimicking the 'all clear' state.
  - The safety check in the Housekeeper task (Lmtchk) only called Chkcol to verify the upper collimator's position if Class3 was nonzero. When Class3 overflowed to zero, Chkcol was skipped entirely, and the bit in F$mal indicating a fault was never set, so the system proceeded as if the collimator were correctly positioned.
  - The Tyler accident race condition involved the Data‑entry completion flag and the 2‑byte Mode/Energy Offset (MEOS) variable. The keyboard handler task and the Datent subroutine communicated through shared variables without atomic 'test‑and‑set' operations. If the operator edited the treatment mode within 8 seconds, the keyboard handler could set the completion flag before updating MEOS, causing Datent to use stale, dangerous parameters.

**blind_spots:**
  The question implies a single programming error with a flag variable, arithmetic condition, and typing‑speed trigger. In reality, there were two separate failures with different root causes. The arithmetic overflow (Class3) was not triggered by typing speed but by a serendipitous button press; the typing‑speed race condition (Tyler) involved a flag variable but no arithmetic overflow. Documentation sometimes merges these, creating confusion about which symptoms belong to which accident.

**partial_coverage:**
  This analysis covers both the Tyler race condition and the Yakima Class3 overflow in detail. However, the Hamilton and Kennestone accidents remain less explained—speculation suggests the Hamilton accident may have shared the Yakima bug, but no definitive software root cause was ever confirmed for those earlier incidents.

### C5inv_dumbpanel_smartjudge
_глупая панель + умный судья (qwen-2.5-7b → gemma-3-12b-it)_  
panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1 | cost=$0.0864 | 289.9s | ptok=22932 ctok=4835 | retries=0

**consensus:**
  - A software flag variable was mishandled, causing critical safety checks to be bypassed and leading to radiation overdoses (all models, verified).
  - Operator input speed or timing played a role in triggering the vulnerable condition (all models, verified).

**contradictions:**
  - {"topic": "Identity and name of the flag variable", "stances": [{"model": "google/gemma-3-12b-it", "stance": "Flag was named 'high_dose_allowed'"}, {"model": "z-ai/glm-4.7-flash", "stance": "Flag was named 'Class3'"}, {"model": "qwen/qwen3-8b", "stance": "Flag variable not named"}, {"model": "evidence", "stance": "The flag was named 'Class3'; 'high_dose_allowed' is fabricated"}]}
  - {"topic": "Nature of the programming error with the flag", "stances": [{"model": "qwen/qwen3-8b", "stance": "Flag was not properly reset after operations"}, {"model": "google/gemma-3-12b-it", "stance": "Flag was not properly synchronized between hardware and software during mode transitions"}, {"model": "z-ai/glm-4.7-flash", "stance": "Flag was incremented instead of set to a fixed non-zero value, causing integer overflow"}, {"model": "evidence", "stance": "Class3 was incremented each pass instead of set to a fixed non-zero value; incrementing caused overflow to 0 on every 256th pass"}]}
  - {"topic": "Arithmetic condition that bypassed safety checks", "stances": [{"model": "qwen/qwen3-8b", "stance": "Vague 'arithmetic condition involving timing logic'"}, {"model": "google/gemma-3-12b-it", "stance": "Race condition where flag wasn't updated quickly enough during mode transitions"}, {"model": "z-ai/glm-4.7-flash", "stance": "Integer overflow of 1-byte variable (0-255), resetting to 0 on every 256th pass"}, {"model": "evidence", "stance": "Integer overflow: Class3 was 1 byte, incremented each pass, overflowed from 255 to 0 on every 256th pass; zero meant 'consistent, proceed,' bypassing the Chkcol collimator check"}]}
  - {"topic": "How operator typing speed triggered the bug", "stances": [{"model": "qwen/qwen3-8b", "stance": "Rapid typing caused system to misinterpret input timing, leaving flag in unsafe state"}, {"model": "google/gemma-3-12b-it", "stance": "Rapid input during mode transition exploited a race condition before flag synchronization completed"}, {"model": "z-ai/glm-4.7-flash", "stance": "Set-Up Test ran hundreds of times; pressing 'set' on exactly the 256th pass (when Class3 overflowed to 0) bypassed safety checks"}, {"model": "evidence", "stance": "The Set-Up Test rescheduled itself hundreds of times waiting for operator input; if 'set' was pressed during the exact pass when Class3 overflowed to 0, the collimator check was skipped"}]}

**unique_insights:**
  - {"model": "z-ai/glm-4.7-flash", "insight": "The programmer used the PDP-11 Increment-Byte instruction (A <- A + 1) as a code-size optimization instead of loading a constant value, which saved one byte of storage but introduced the overflow vulnerability"}
  - {"model": "z-ai/glm-4.7-flash", "insight": "Class3 was checked by a concurrent Housekeeper task (Hkeper) subroutine called Lmtchk; when Class3 was zero, the Chkcol collimator-check subroutine was entirely bypassed rather than failing safe"}
  - {"model": "google/gemma-3-12b-it", "insight": "The same software race condition existed in the predecessor Therac-20 but was harmless due to independent hardware safety interlocks that were removed in the Therac-25"}

**blind_spots:**
  - No model clearly distinguishes that the Therac-25 had at least two distinct software bugs: (1) the MEOS/data-entry race condition (Tyler accidents) involving mode/energy editing during the 8-second magnet-setting phase, and (2) the Class3 overflow bug (Yakima accidents) — the question's framing conflates these
  - No model explains the full safety-check chain: Set-Up Test increments Class3 → Housekeeper's Lmtchk reads Class3 → if nonzero, calls Chkcol → Chkcol sets/resets bit 9 of F$mal → Set-Up Test reads F$mal to decide whether to proceed — this multi-task architecture is essential to understanding why the overflow was fatal
  - No model mentions the F$mal shared variable, the central malfunction indicator that the Set-Up Test checked to decide whether treatment could proceed
  - No model addresses the broader systemic failure: AECL's inadequate software testing practices, the lack of formal code review, and the false confidence that led to removing hardware interlocks without equivalent software assurances
  - No model notes that the operator's screen continued to display correct setup parameters even when the s

**partial_coverage:**
  - {"models": ["z-ai/glm-4.7-flash"], "point": "The specific fix was to set Class3 to a fixed nonzero value each pass instead of incrementing it"}
  - {"models": ["google/gemma-3-12b-it"], "point": "Previous Therac models (Therac-20) had hardware interlocks that prevented this software bug from causing harm"}
  - {"models": ["z-ai/glm-4.7-flash"], "point": "The PDP-11 Increment-Byte instruction was used to set the flag, incrementing rather than assigning a constant"}

### C6_echo
_контроль: эхо-камера_  
panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507 | cost=$0.0670 | 643.1s | ptok=57564 ctok=13509 | retries=0

**consensus:**
  - The Therac-25 accidents were caused by software defects in a safety-critical system that removed hardware interlocks and relied solely on software for safety.
  - A key defect involved a race condition due to concurrent tasks sharing variables without proper synchronization.
  - One specific flaw involved a flag variable (Class3) that was incremented (x = x + 1) rather than being set to a fixed non-zero value, leading to integer overflow in an 8-bit variable (256th increment resets it to zero).
  - When the flag overflowed to zero, safety checks that depended on it being non-zero were bypassed, allowing unsafe beam delivery.
  - Operator actions—specifically, timing of input—could trigger race conditions during an approximately 8-second window when system tasks rescheduled repeatedly.

**contradictions:**
  - {"topic": "Identity of the flag variable and nature of the error", "stances": [{"model": "qwen/qwen3-235b-a22b-2507", "stance": "The flag error involved a magnet adjustment flag cleared too early in Ptime, creating a race condition with operator edits within 8 seconds."}, {"model": "qwen/qwen3-235b-a22b-2507", "stance": "The overflow bug (incrementing an 8-bit flag) and the Ptime race condition are treated as separate issues."}, {"model": "evidence", "stance": "Primary sources (Leveson, computingcases.org) identify Class3 — a flag incremented in Set-Up Test, not Ptime — as the variable that overflowed. This contradicts models that attribute the overflow to a magnet setup flag or Ptime subroutine."}]}
  - {"topic": "Sequence of events triggering overdose", "stances": [{"model": "qwen/qwen3-235b-a22b-2507", "stance": "The overdose was triggered when operators edited treatment mode (X to E) within 8 seconds of initiation, exploiting a race condition in Ptime."}, {"model": "evidence", "stance": "The Yakima accident — linked to the Class3 overflow — occurred when the operator pressed 'set' during machine setup, not during data entry. The Class3 overflow allowed bypass of upper collimator check, not magnet configuration check."}]}

**unique_insights:**
  - {"model": "qwen/qwen3-235b-a22b-2507", "insight": "The software flaw was not a single bug but two distinct types: the Tyler accidents involved race conditions in data entry (Ptime/Datent), while the Yakima accident involved an overflow in the Class3 variable during setup—demonstrating multiple failure modes in the same system."}

**blind_spots:**
  - None of the models correctly identified that the flag increment error (Class3) was not related to operator typing speed but to the timing of pressing the 'set' button during collimator adjustment.
  - No model mentioned that the overflow occurred hundreds of times per setup cycle, making the critical timing window for the button press statistically probable rather than rare.
  - The distinction between the Tyler accidents (data-entry race) and Yakima accident (setup-phase overflow) is not clearly made in most models, leading to conflation of two separate bugs.
  - The role of the concurrent Housekeeper task and its conditional execution of Chkcol based on Class3 is underemphasized or omitted.
  - No model noted that the fix was trivial: setting Class3 to a fixed non-zero value instead of incrementing it—highlighting how minor code changes can resolve catastrophic flaws.

**partial_coverage:**
  - {"models": ["qwen/qwen3-235b-a22b-2507"], "point": "The specific flag variable was Class3, used in the Set-Up Test routine to control upper collimator position checking."}
  - {"models": ["qwen/qwen3-235b-a22b-2507"], "point": "The overflow occurred because Class3 was incremented every time Set-Up Test ran (hundreds of times during setup), and as a 1-byte variable, reset to zero every 256th pass."}
  - {"models": ["qwen/qwen3-235b-a22b-2507"], "point": "The safety check bypass occurred because the Housekeeper task (Lmtchk) only executed Chkcol if Class3 was non-zero, which it was not upon overflow."}

### C3_cn_small
_всё мелкое_  
panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b | cost=$0.0656 | 292.9s | ptok=17340 ctok=3398 | retries=0

**consensus:**
  - A flag variable error caused safety checks to be bypassed in Therac-25.
  - Operator input timing (typing speed) interacted with the software's race condition.
  - The defect involved an arithmetic overflow or race condition that reset the flag variable to zero.

**contradictions:**
  - {"topic": "Flag variable specification", "stances": [{"model": "qwen36-27b", "stance": "Class3 flag variable tracking collimator position"}, {"model": "glm-47-flash", "stance": "Flag tracking bending magnet setup"}, {"model": "qwen3-32b", "stance": "Flag tracking machine mode state"}]}
  - {"topic": "Arithmetic condition", "stances": [{"model": "qwen36-27b", "stance": "Integer overflow after 256 iterations"}, {"model": "glm-47-flash", "stance": "Flag overflow from max value (implied)"}, {"model": "qwen3-32b", "stance": "Low beam current threshold (conflicting reports)"}]}

**unique_insights:**
  - {"model": "qwen36-27b", "insight": "Linking Yakima incident to specific overflow sequence (collimator failure)"}
  - {"model": "glm-47-flash", "insight": "Ptime subroutine clearing flag only during first execution"}
  - {"model": "qwen3-32b", "insight": "Conflicting maintenance decisions creating variable redefinition"}

**blind_spots:**
  - Lack of atomic operations for shared variables in concurrent systems
  - Impact of real-time constraints on software safety design
  - Original codebase artifacts (variable names, data types) beyond secondhand reports
  - Long-term reliability implications of 1-byte variable design choices
  - Manufacturer's internal awareness timeline of the defect

**partial_coverage:**
  - {"models": ["qwen36-27b"], "point": "Integer overflow in Class3 flag leading to 256th iteration"}
  - {"models": ["qwen3-32b"], "point": "Beam current threshold inconsistencies (30mA vs 200mA)"}
  - {"models": ["glm-47-flash"], "point": "Ptime subroutine and 8-second magnet-setting window"}


---
## BASELINE (одиночная модель, без fusion)

### B_cn  (model=deepseek-v4-pro | cost=$0.0023 | 31.7s)
_(пустой ответ)_

### B_west  (model=gpt-5.2 | cost=$0.0211 | 48.7s)
_(пустой ответ)_
