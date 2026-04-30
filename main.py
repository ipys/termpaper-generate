"""
Entry point — configure logging, build the Application, register handlers,
and start polling.

Usage:
    python main.py
"""
import logging
import sys

from telegram import BotCommand
from telegram.ext import Application, CommandHandler

from config import TELEGRAM_BOT_TOKEN
from handlers import build_conversation_handler


# ── Logging ────────────────────────────────────────────────────────────────────
logging.basicConfig(
    format="%(asctime)s | %(levelname)-8s | %(name)s — %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
    stream=sys.stdout,
)
# Quieten noisy libraries
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# ── Bot commands (shown in Telegram menu) ─────────────────────────────────────
BOT_COMMANDS = [
    BotCommand("start",  "Generate a new term paper"),
    BotCommand("cancel", "Cancel the current operation"),
]


# ── Post-init: register bot commands ──────────────────────────────────────────
async def post_init(application: Application) -> None:
    await application.bot.set_my_commands(BOT_COMMANDS)
    logger.info("Bot commands registered.")


# ── Main ───────────────────────────────────────────────────────────────────────
def main() -> None:
    logger.info("Starting Academic Term Paper Bot…")

    app = (
        Application.builder()
        .token(TELEGRAM_BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    app.add_handler(build_conversation_handler())

    logger.info("Bot is running. Press Ctrl-C to stop.")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
