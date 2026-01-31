from typing import Final
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

# Constants
EMAIL: Final[str] = os.getenv("EMAIL") or ""
if not EMAIL:
    raise ValueError("EMAIL is missing in environment variables.")
PASSWORD: Final[str] = os.getenv("PASSWORD") or ""
if not PASSWORD:
    raise ValueError("PASSWORD is missing in environment variables.")

SMTP_ADDRESS: Final[str] = os.getenv("SMTP_ADDRESS") or ""
if not SMTP_ADDRESS:
    raise ValueError("SMTP_ADDRESS is missing in environment variables.")
SMTP_PORT: Final[str] = os.getenv("SMTP_PORT") or ""
if not SMTP_PORT:
    raise ValueError("SMTP_PORT is missing in environment variables.")
