from typing import Final
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

# BOT TOKEN
DISCORD_BOT_TOKEN: Final[str] = os.getenv("DISCORD_BOT_TOKEN") or ""
if not DISCORD_BOT_TOKEN:
    raise ValueError("DISCORD_BOT_TOKEN is missing in environment variables.")
