from typing import Final
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

# BOT TOKEN
TELEGRAM_BOT_TOKEN: Final[str] = os.getenv("TELEGRAM_BOT_TOKEN") or ""
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is missing in environment variables.")

# BOT USERNAME
TELEGRAM_BOT_USERNAME: Final[str] = os.getenv("TELEGRAM_BOT_USERNAME") or ""
if not TELEGRAM_BOT_USERNAME:
    raise ValueError("TELEGRAM_BOT_USERNAME is missing in environment variables.")
