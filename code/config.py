from pathlib import Path

OPENROUTER_BASE = "https://openrouter.ai/api/v1/chat/completions"

# ─── Caller-проводник (фиксирован) ─────────────────────────────────────────────
# Вызывает fusion как tool и цитирует его структурный результат дословно.
# Дёшев ($0.09/$0.10 за M), способен к точному relay. temp 0 для минимума стохастики.
CALLER_MODEL = "qwen/qwen3-235b-a22b-2507"
TEMPERATURE = 0.0

# System-промпт «проводника»: вызвать fusion и вывести его структуру дословно как JSON.
RELAY_SYSTEM = (
    "You have access to a multi-model deliberation tool (fusion). "
    "Step 1: call the tool with the user's question. "
    "Step 2: the tool returns a structured analysis with these fields: "
    "consensus, contradictions, unique_insights, blind_spots, partial_coverage, "
    "and responses (each panel model's full answer). "
    "Your ONLY job is to output that structured analysis VERBATIM as a single JSON object. "
    "Do NOT summarize, do NOT add your own opinion, do NOT write your own answer. "
    "Output raw JSON only, nothing else."
)

# ─── Конфиги эксперимента ──────────────────────────────────────────────────────
# panel = analysis_models, judge = fusion-internal judge (parameters.model).
# Порядок CORE важен: дешёвые/важные раньше — при упоре в budget cap хвост не выполнится.
# 2×2 «ум панели × ум судьи» на открытых китайцах: C2(умн/умн) C5(умн/глуп) C5inv(глуп/умн) ≈C3(мелк/мелк).
CORE_CONFIGS = {
    "C3_cn_small": {
        "panel": ["qwen/qwen3.6-27b", "z-ai/glm-4.7-flash", "qwen/qwen3-32b"],
        "judge": "qwen/qwen3-32b",
        "note": "всё мелкое",
    },
    "C5inv_dumbpanel_smartjudge": {
        "panel": ["qwen/qwen3-8b", "google/gemma-3-12b-it", "z-ai/glm-4.7-flash"],
        "judge": "z-ai/glm-5.1",
        "note": "глупая панель + умный судья (qwen-2.5-7b → gemma-3-12b-it: старый qwen без tool-use эндпоинта падал в fusion)",
    },
    "C6_echo": {
        "panel": ["qwen/qwen3-235b-a22b-2507", "qwen/qwen3-235b-a22b-2507", "qwen/qwen3-235b-a22b-2507"],
        "judge": "qwen/qwen3-235b-a22b-2507",
        "note": "контроль: эхо-камера",
    },
    "C5_smartpanel_dumbjudge": {
        "panel": ["deepseek/deepseek-v4-pro", "z-ai/glm-5.1", "moonshotai/kimi-k2.6"],
        "judge": "qwen/qwen3-8b",
        "note": "умная панель + глупый судья",
    },
    "C2_cn_open": {
        "panel": ["deepseek/deepseek-v4-pro", "z-ai/glm-5.1", "moonshotai/kimi-k2.6"],
        "judge": "qwen/qwen3-235b-a22b-2507",
        "note": "открытый китайский фронтир (умн+умн)",
    },
    "C1_west_closed": {
        "panel": ["openai/gpt-5.2", "google/gemini-3.1-pro-preview", "x-ai/grok-4.3"],
        "judge": "openai/gpt-5.2",
        "note": "западный закрытый фронтир",
    },
}

# Baseline без fusion — запускаются ПОСЛЕ core, только если остался бюджет.
BASELINE_CONFIGS = {
    "B_cn": {"single": "deepseek/deepseek-v4-pro", "note": "одиночка-китаец без fusion"},
    "B_west": {"single": "openai/gpt-5.2", "note": "одиночка-западник без fusion"},
}

# ─── Параметры вызовов ─────────────────────────────────────────────────────────
MAX_TOOL_CALLS = 1          # минимум (web вшит, 0 невалиден). Range 1-16.
MAX_TOKENS = 20000          # запас на дословное цитирование структуры ВКЛЮЧАЯ responses.
                            # ВАЖНО: при 5000 хвост responses обрезался у ~30% вызовов → JSON невалиден.
                            # Анализ-поля идут до responses, поэтому _extract_structure доп. салважит
                            # обрезанный JSON (см. runner). Видели completion до ~18k токенов.
REQUEST_TIMEOUT_S = 900.0   # вызов может идти до 11+ мин (мелкие модели + web-циклы, видели 686с)
CONCURRENCY = 20            # параллельных вызовов. OR RPS-лимит = баланс в $ → держи баланс ≥ $20.
                            # Тюнится флагом --concurrency.
MAX_RETRIES = 3             # ретраи на транзиентные сбои (JSON/5xx/timeout/Provider error)
RETRY_BACKOFF_S = 5.0

# ─── Бюджетный предохранитель ─────────────────────────────────────────────────
# Жёсткий стоп по СУММЕ usage.cost наших вызовов (НЕ по балансу — параллельные сессии
# мешают). Новые вызовы не стартуют после превышения; in-flight доезжают.
BUDGET_CAP_USD = 18.0

# ─── Пути ─────────────────────────────────────────────────────────────────────
# Код лежит в code/, данные (questions/, results/) — на уровень выше, в корне fusion/.
BASE_DIR = Path(__file__).parent.parent
QUESTIONS_DIR = BASE_DIR / "questions"
RESULTS_DIR = BASE_DIR / "results"
