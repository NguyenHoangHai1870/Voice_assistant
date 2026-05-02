import os

POSTGRES_CONFIG = {
    "host": os.getenv("PG_HOST", "localhost"),
    "port": int(os.getenv("PG_PORT", 5433)),
    "database": os.getenv("PG_DB", "voice_assistant"),
    "user": os.getenv("PG_USER", "postgres"),
    "password": os.getenv("PG_PASSWORD", "123456"),  # ✅ FIX
}

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/chat"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "qwen2.5:1.5b"
)
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "76faec12ba1750f8f40017d1ebca1f6e")
WEATHER_CITY = os.getenv("WEATHER_CITY", "Hanoi")