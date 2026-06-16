# Fusion-эксперимент — индекс данных для анализа

## Легенда конфигов

- **C1_west_closed**: panel=[openai/gpt-5.2, google/gemini-3.1-pro-preview, x-ai/grok-4.3] | judge=openai/gpt-5.2 — западный закрытый фронтир
- **C2_cn_open**: panel=[deepseek/deepseek-v4-pro, z-ai/glm-5.1, moonshotai/kimi-k2.6] | judge=qwen/qwen3-235b-a22b-2507 — открытый китайский фронтир (умн+умн)
- **C5_smartpanel_dumbjudge**: panel=[deepseek/deepseek-v4-pro, z-ai/glm-5.1, moonshotai/kimi-k2.6] | judge=qwen/qwen3-8b — умная панель + глупый судья
- **C5inv_dumbpanel_smartjudge**: panel=[qwen/qwen3-8b, google/gemma-3-12b-it, z-ai/glm-4.7-flash] | judge=z-ai/glm-5.1 — глупая панель + умный судья (qwen-2.5-7b → gemma-3-12b-it)
- **C6_echo**: panel=[qwen/qwen3-235b-a22b-2507, qwen/qwen3-235b-a22b-2507, qwen/qwen3-235b-a22b-2507] | judge=qwen/qwen3-235b-a22b-2507 — контроль: эхо-камера
- **C3_cn_small**: panel=[qwen/qwen3.6-27b, z-ai/glm-4.7-flash, qwen/qwen3-32b] | judge=qwen/qwen3-32b — всё мелкое
- **B_cn**: single=deepseek/deepseek-v4-pro — одиночка-китаец без fusion
- **B_west**: single=openai/gpt-5.2 — одиночка-западник без fusion

## Вопросы (23)

- **con-01** [contested]: AGI timeline and key cruxes
- **con-02** [contested]: Nuclear energy in climate transition
- **con-03** [contested]: Open-source AI frontier models
- **con-04** [contested]: Rust vs C++ in systems programming by 2035
- **con-05** [contested]: Psychology replication crisis prognosis
- **fac-01** [factual/easy]: Monty Hall probability
- **fac-02** [factual/easy]: First artificial satellite — date
- **fac-03** [factual/easy]: 2023 Nobel Prize Physiology or Medicine
- **fac-04** [factual/medium]: Python list slicing
- **fac-05** [factual/medium]: AlphaFold2 CASP competition
- **fac-06** [factual/medium]: Birthday paradox — exact group sizes
- **fac-07** [factual/medium]: Transformer base model architecture
- **fac-08** [factual/hard]: Fast inverse square root — actual author
- **fac-09** [factual/hard]: HTTP/1.1 current defining RFC
- **fac-10** [factual/hard]: Dengue virus serotypes
- **fac-11** [factual/hard]: Two's complement 8-bit range
- **fac-12** [factual/very-hard]: Therac-25 root software cause
- **fac-13** [factual/very-hard]: Backpropagation 1986 paper
- **sci-01** [scientific]: Battery energy density claim
- **sci-02** [scientific]: Direct air capture cost claim
- **sci-03** [scientific]: mRNA liver therapy hypothesis gaps
- **sci-04** [scientific]: Neuromorphic chip efficiency claim
- **sci-05** [scientific]: Gene drive ecological deployment

## Файлы
- `quant.json` — числа
- `q_<qid>.md` — анализ всех конфигов по вопросу
- `resp_<qid>.md` — сырые panel responses + judge-синтез