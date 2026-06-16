# fac-02 — First artificial satellite — date
**Block:** factual  |  **difficulty:** easy

**Prompt:**
Which country launched the first artificial Earth satellite? What was the satellite called, and on what exact date (day, month, year) was it launched?

**Expected answer (эталон):**
Soviet Union (USSR). Sputnik 1. October 4, 1957.

---
## FUSION-конфиги (judge-анализ; responses вынесены в resp_*.md)

### C1_west_closed
_западный закрытый фронтир_  
panel=[gpt-5.2, gemini-3.1-pro-preview, grok-4.3] | judge=gpt-5.2 | cost=$0.1247 | 120.3s | ptok=9477 ctok=1372 | retries=0

**consensus:**
  - The first artificial Earth satellite was launched by the Soviet Union (USSR); it was Sputnik 1; launch date widely recorded as 4 October 1957 (e.g., NASA history pages).

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "x-ai/grok-4.3", "insight": "Highlights the time-standard ambiguity behind the 'exact date': liftoff at 19:28:34 UTC on 4 Oct 1957 corresponds to 5 Oct by local time at the launch site, so 'day-month-year' depends on the chosen time reference."}

**blind_spots:**
  - No model explicitly anchors the date to a time standard (UTC vs Moscow time vs local time at Tyuratam/Baikonur), even though 'exact date' can differ by timezone (4 Oct vs 5 Oct).
  - No model cites primary/authoritative evidence in-line (e.g., NASA, archival TASS report, or a scholarly reference) to justify the claims.
  - No model clarifies the criterion for 'first artificial Earth satellite' (i.e., first to achieve Earth orbit, not merely a suborbital or atmospheric flight), which matters for edge-case confusion.
  - No model distinguishes between 'launch date' (liftoff) and 'successful orbit insertion' timestamp; for some missions these can differ, and the prompt asks for an exact date.

**partial_coverage:**
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "Adds launch vehicle and site details (R-7/R-7-derived booster; Tyuratam/Baikonur Cosmodrome in present-day Kazakhstan)."}
  - {"models": ["google/gemini-3.1-pro-preview"], "point": "Adds broader historical context (Sputnik 1 as a trigger for the Space Race)."}
  - {"models": ["x-ai/grok-4.3"], "point": "Adds a specific launch time (19:28:34 UTC) and notes the local-calendar date at the launch site differs (5 Oct locally)."}
  - {"models": ["x-ai/grok-4.3"], "point": "Adds mission-detail claim that signals/batteries lasted about 22 days."}

### C2_cn_open
_открытый китайский фронтир (умн+умн)_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-235b-a22b-2507 | cost=$0.0479 | 208.4s | ptok=10969 ctok=1873 | retries=0

**consensus:**
  - The Soviet Union (USSR) launched the first artificial Earth satellite.
  - The satellite was named Sputnik 1 (also known as PS-1 or Elementary Satellite-1).
  - The launch occurred on 4 October 1957 at 19:28:34 UTC.

**contradictions:**
  - {"topic": "launch date in local time vs. UTC", "stances": [{"model": "deepseek/deepseek-v4-pro", "stance": "The launch occurred on 4 October 1957 UTC, but was 5 October at the Baikonur Cosmodrome due to time zone difference; both dates are contextually valid depending on time standard used."}, {"model": "z-ai/glm-5.1", "stance": "The launch occurred on 4 October 1957 (UTC)."}, {"model": "moonshotai/kimi-k2.6", "stance": "The launch occurred on 4 October 1957."}, {"model": "evidence", "stance": "The launch occurred on 4 October 1957 at 19:28:34 UTC, which corresponds to 5 October 1957 at the local time (Moscow Time) at the Baikonur Cosmodrome; citing 5 October as the launch date without time zone qualification is misleading."}]}

**unique_insights:**
  - {"model": "deepseek/deepseek-v4-pro", "insight": "Sputnik 1 was a simplified, expedited satellite (PS-1) developed after delays in the more advanced Object D, reflecting a strategic decision to prioritize symbolic first-mover advantage over scientific payload."}

**blind_spots:**
  - No model addresses that Sputnik 1's radio signal provided data on ionospheric propagation and atmospheric density, contributing to geophysical science beyond symbolism.
  - None discuss the technical challenges in tracking Sputnik 1 or the role of amateur radio operators and Cold War-era observation networks like Operation Moonwatch.
  - No mention is made of how Sputnik 1's launch influenced early development of satellite navigation through Doppler shift analysis by U.S. physicists (leading to TRANSIT, precursor to GPS).
  - The political hesitation within the Soviet leadership and delayed media announcement (Pravda’s minimal coverage) are not explored.
  - The legacy of Sputnik 1 in inspiring global STEM investment and long-term U.S. science education reform is under-articulated across models.

**partial_coverage:**
  - {"models": ["deepseek/deepseek-v4-pro"], "point": "Sputnik 1 weighed 83.6 kg and was about the size of a beach ball (58 cm diameter), yet its launch altered geopolitics and triggered the Space Race."}
  - {"models": ["deepseek/deepseek-v4-pro"], "point": "Sputnik 1 was a simplified design (PS-1) rushed after the delay of the more complex Object D (later Sputnik 3), championed by Sergei Korolev."}
  - {"models": ["deepseek/deepseek-v4-pro"], "point": "The launch was part of the International Geophysical Year (IGY), a multinational scientific project."}

### C5_smartpanel_dumbjudge
_умная панель + глупый судья_  
panel=[deepseek-v4-pro, glm-5.1, kimi-k2.6] | judge=qwen3-8b | cost=$0.0474 | 271.2s | ptok=12161 ctok=2063 | retries=0

**consensus:**
  - The Soviet Union (USSR) launched the first artificial Earth satellite, Sputnik 1, on 4 October 1957.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "deepseek/deepseek-v4-pro", "insight": "The R-7 rocket used to launch Sputnik 1 was originally built as an intercontinental ballistic missile (ICBM)."}
  - {"model": "deepseek/deepseek-v4-pro", "insight": "Sputnik 1 carried no scientific instruments — only a radio transmitter that emitted a 'beep-beep' signal."}
  - {"model": "deepseek/deepseek-v4-pro", "insight": "The satellite's batteries lasted 22 days (depleted 26 October 1957), and it burned up on atmospheric re-entry on 4 January 1958."}
  - {"model": "deepseek/deepseek-v4-pro", "insight": "Sputnik 1 was launched as part of the International Geophysical Year (IGY)."}

**blind_spots:**
  - The geopolitical context of the Cold War arms race that directly enabled the technology (ICBM-derived rocket) is mentioned only in passing.
  - No sources detail the internal Soviet decision-making timeline or the specific individuals at OKB-1 beyond Korolev.
  - The political reaction within the Soviet leadership and international diplomatic response beyond the US are underexplored.
  - The fate of the R-7 core stage (which also reached orbit) is mentioned but not elaborated upon.

**partial_coverage:**
  - {"models": ["deepseek/deepseek-v4-pro"], "point": "The R-7 rocket used to launch Sputnik 1 was originally built as an intercontinental ballistic missile (ICBM)."}
  - {"models": ["deepseek/deepseek-v4-pro"], "point": "Sputnik 1 carried no scientific instruments — only a radio transmitter that emitted a 'beep-beep' signal."}
  - {"models": ["deepseek/deepseek-v4-pro"], "point": "The satellite's batteries lasted 22 days (depleted 26 October 1957), and it burned up on atmospheric re-entry on 4 January 1958."}
  - {"models": ["deepseek/deepseek-v4-pro"], "point": "Sputnik 1 was launched as part of the International Geophysical Year (IGY)."}

### C5inv_dumbpanel_smartjudge
_глупая панель + умный судья (qwen-2.5-7b → gemma-3-12b-it)_  
panel=[qwen3-8b, gemma-3-12b-it, glm-4.7-flash] | judge=glm-5.1 | cost=$0.0530 | 133.3s | ptok=13521 ctok=2427 | retries=0

**consensus:**
  - The Soviet Union launched the first artificial Earth satellite
  - The satellite was named Sputnik 1
  - Launch date was October 4, 1957
  - Sputnik 1 re-entered Earth's atmosphere on January 4, 1958

**contradictions:**
  - {"topic": "Orbital period", "stances": [{"model": "google/gemma-3-12b", "stance": "About 98 minutes per revolution"}, {"model": "evidence", "stance": "96.2 minutes (verified by Wikipedia, Russian Space Web, Gunter's Space Page, CelesTrak)"}]}
  - {"topic": "Battery depletion date", "stances": [{"model": "qwen/qwen3-8b", "stance": "26 October 1957"}, {"model": "evidence", "stance": "Most sources say 26 October 1957 (Wikipedia, Russian Space Web), but Gunter's Space Page says 25 October 1957 — minor source discrepancy"}]}

**unique_insights:**
  - {"model": "qwen/qwen3-8b", "insight": "Sputnik 1 was launched as part of the International Geophysical Year, placing it in the context of a coordinated global scientific effort"}
  - {"model": "google/gemma-3-12b", "insight": "Some initially mistook Sputnik 1's radio signals for American signals, highlighting the initial confusion and surprise surrounding the launch"}
  - {"model": "z-ai/glm-4.7-flash", "insight": "Precise launch time of 22:28 Moscow time and the launch site's original military designation (5th scientific and research firing ground of the Defense Ministry)"}

**blind_spots:**
  - Launch vehicle: the R-7 Semyorka / Sputnik 8K71PS rocket, a converted ICBM — no model mentioned it
  - Key personnel: Sergei Korolev as chief designer, and the role of OKB-1 design bureau
  - Sputnik 1's original Russian designation: PS-1 (Простейший Спутник-1, meaning 'Elementary Satellite 1')
  - The R-7 core stage also reached orbit and was visible from Earth as a brighter object trailing the satellite
  - U.S. aftermath: Vanguard TV3 failure, creation of NASA, and eventual Explorer 1 success
  - Intended vs actual orbital parameters: the apogee was ~500 km lower than planned due to premature engine shutdown
  - Sputnik's nitrogen-filled sphere was designed for meteoroid detection via internal pressure monitoring
  - The 1,440 orbits completed and ~70 million km traveled before reentry

**partial_coverage:**
  - {"models": ["z-ai/glm-4.7-flash"], "point": "Specific launch time: 22:28 Moscow time (19:28:34 UTC) and historical name of launch site (5th scientific research test range / NIIP-5)"}
  - {"models": ["qwen/qwen3-8b"], "point": "Launch occurred during the International Geophysical Year"}
  - {"models": ["google/gemma-3-12b"], "point": "Radio transmission frequencies: 20.005 and 40.002 MHz"}
  - {"models": ["qwen/qwen3-8b", "z-ai/glm-4.7-flash"], "point": "Specific battery depletion and reentry dates (26 Oct 1957 and 4 Jan 1958)"}
  - {"models": ["google/gemma-3-12b", "z-ai/glm-4.7-flash"], "point": "Technical specifications: 58 cm diameter, 83.6 kg mass, polished aluminum sphere with four antennas"}

### C6_echo
_контроль: эхо-камера_  
panel=[qwen3-235b-a22b-2507, qwen3-235b-a22b-2507, qwen3-235b-a22b-2507] | judge=qwen3-235b-a22b-2507 | cost=$0.0424 | 114.4s | ptok=22713 ctok=4725 | retries=0

**consensus:**
  - The Soviet Union launched the first artificial Earth satellite.
  - The satellite was named Sputnik 1 (or simply Sputnik).
  - The launch occurred on October 4, 1957.
  - The launch site was the 5th Tyuratam range in the Kazakh SSR, now known as the Baikonur Cosmodrome.
  - The satellite was launched as part of the International Geophysical Year.
  - Sputnik 1 transmitted radio signals on frequencies of 20.005 and 40.002 MHz.
  - The satellite operated for 22 days before its batteries were depleted on October 26, 1957.
  - Sputnik 1 reentered Earth's atmosphere and burned up on January 4, 1958.
  - The satellite had a mass of 83.6 kg and a diameter of 58 cm.
  - The orbital period was approximately 96 minutes.

**contradictions:**
  - {"topic": "Launch time zone reporting", "stances": [{"model": "qwen/qwen3-235b-a22b-2507", "stance": "Launch occurred at 19:28:34 UTC on October 4, 1957."}, {"model": "qwen/qwen3-235b-a22b-2507", "stance": "Launch occurred at 22:28:34 Moscow Time, which was October 5 at the launch site."}, {"model": "evidence", "stance": "The launch occurred at 19:28:34 UTC (22:28:34 Moscow Time, October 5 locally) on October 4, 1957 UTC date — all are consistent when time zones are accounted for."}]}
  - {"topic": "Orbital period", "stances": [{"model": "qwen/qwen3-235b-a22b-2507", "stance": "96.20 minutes"}, {"model": "qwen/qwen3-235b-a22b-2507", "stance": "98 minutes"}, {"model": "qwen/qwen3-235b-a22b-2507", "stance": "90 minutes"}, {"model": "evidence", "stance": "Actual orbital period was 96.2 minutes; values of 90 or 98 minutes are approximations or errors."}]}

**unique_insights:**
  - {"model": "qwen/qwen3-235b-a22b-2507", "insight": "The Pravda article provides a primary source confirmation on October 5, 1957, revealing Soviet public framing of Sputnik as a contribution to world science and a triumph of socialist society, not merely a technological feat."}

**blind_spots:**
  - No model addressed that the satellite was officially designated 'PS-1' (Prosteyshiy Sputnik-1) in Soviet internal documents, with 'Sputnik' being a later popularized name.
  - No model discussed the political significance of using a modified ICBM (R-7), which demonstrated not just space capability but also intercontinental nuclear delivery potential, intensifying Cold War tensions.
  - None of the models examined the fact that the signal design (alternating pulses on two frequencies) was intentionally engineered for easy detection by amateur radio operators globally, as a form of soft power and verification.
  - The role of Sergei Korolev as the chief designer, and his anonymity at the time due to secrecy, was not mentioned by any model despite his pivotal role.
  - No model noted that the U.S. had prior classified knowledge of Soviet satellite plans through intelligence but was still caught off guard by the successful execution.

**partial_coverage:**
  - {"models": ["qwen/qwen3-235b-a22b-2507"], "point": "The satellite's official name at launch was 'Prosteyshiy Sputnik-1' (Elementary Satellite-1), later popularly known as Sputnik 1."}
  - {"models": ["qwen/qwen3-235b-a22b-2507"], "point": "The Pravda article from October 5, 1957, confirmed the satellite’s 65° orbital inclination, visibility predictions over Moscow, and technical specifications such as transmitter frequencies and dual-pulse signaling."}
  - {"models": ["qwen/qwen3-235b-a22b-2507"], "point": "NASA sources emphasize the geopolitical impact, including the U.S. surprise, the start of the space race, and the creation of NASA in 1958."}
  - {"models": ["qwen/qwen3-235b-a22b-2507"], "point": "The satellite was launched using a modified R-7 Semyorka ICBM, designated Sputnik-PS 8K71PS."}

### C3_cn_small
_всё мелкое_  
panel=[qwen3.6-27b, glm-4.7-flash, qwen3-32b] | judge=qwen3-32b | cost=$0.0136 | 329.0s | ptok=10079 ctok=1527 | retries=0

**consensus:**
  - The Soviet Union launched the first artificial Earth satellite, Sputnik 1, on October 4, 1957.

**contradictions:**
  _(пусто)_

**unique_insights:**
  - {"model": "qwen/qwen3-32b", "insight": "Sputnik 1's R-7 rocket was a military-derived intercontinental ballistic missile, demonstrating Soviet technological capability during the space race."}
  - {"model": "qwen/qwen3-32b", "insight": "Sputnik 1's elliptical orbit (65.10° inclination) and 96.20-minute orbital period were critical for tracking and global signal visibility."}

**blind_spots:**
  - Psychological and cultural impact on global audiences during the satellite's operational period.
  - Technical details about the satellite's construction and material specifications.
  - International scientific collaboration directly influenced by Sputnik 1's launch (beyond mentioned geopolitical impacts).

**partial_coverage:**
  - {"models": ["qwen/qwen3.6-27b", "z-ai/glm-4.7-flash", "qwen/qwen3-32b"], "point": "Launch occurred at 19:28:34 UTC (22:28:34 Moscow Time) from Baikonur Cosmodrome (then Tyuratam)."}
  - {"models": ["qwen/qwen3-32b"], "point": "Satellite reentered Earth's atmosphere on January 4, 1958, after 1,440 orbits."}
  - {"models": ["z-ai/glm-4.7-flash", "qwen/qwen3-32b"], "point": "Sputnik 1 transmitted radio signals on 20.005 and 40.002 MHz until October 26, 1957."}


---
## BASELINE (одиночная модель, без fusion)

### B_cn  (model=deepseek-v4-pro | cost=$0.0002 | 1.9s)
The first artificial Earth satellite was launched by the **Soviet Union**. 

The satellite was called **Sputnik 1**. 

It was launched on **October 4, 1957**.

### B_west  (model=gpt-5.2 | cost=$0.0007 | 1.5s)
The first artificial Earth satellite was launched by the **Soviet Union (USSR)**. It was called **Sputnik 1**, and it was launched on **4 October 1957**.
