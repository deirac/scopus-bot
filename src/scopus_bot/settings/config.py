from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[3]
ENV_FILE = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_FILE)


@dataclass
class AppConfig:
    headless: bool = False
    timeout_ms: int = 30000
    output_dir: str = "data/output"
    portal_url: str = ""
    scopus_username: str = ""
    scopus_password: str = ""


def load_config() -> AppConfig:
    return AppConfig(
        headless=os.getenv("HEADLESS", "false").lower() == "true",
        timeout_ms=int(os.getenv("TIMEOUT_MS", "30000")),
        output_dir=os.getenv("OUTPUT_DIR", "data/output"),
        portal_url=os.getenv("PORTAL_URL", ""),
        scopus_username=os.getenv("SCOPUS_USERNAME", ""),
        scopus_password=os.getenv("SCOPUS_PASSWORD", ""),
    )