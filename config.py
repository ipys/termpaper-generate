"""
Central configuration — all secrets come from environment variables.
Copy .env.example → .env and fill in your values before running.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# ── Telegram ──────────────────────────────────────────────────────────────────
TELEGRAM_BOT_TOKEN: str = os.environ["TELEGRAM_BOT_TOKEN"]

# ── Gemini ────────────────────────────────────────────────────────────────────
GEMINI_API_KEY: str = os.environ["GEMINI_API_KEY"]
GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

# ── Document ──────────────────────────────────────────────────────────────────
# Approximate words Gemini should target per page (used to scale prompts)
WORDS_PER_PAGE: int = 300
MIN_PAGES: int = 3
MAX_PAGES: int = 8

# Path to the default university logo (bundled with the project)
DEFAULT_LOGO_PATH: str = os.path.join(os.path.dirname(__file__), "assets", "default_logo.png")

# Output directory for generated documents
OUTPUT_DIR: str = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)
