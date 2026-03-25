from dataclasses import dataclass
import os


@dataclass
class AppConfig:
    headless: bool = False
    timeout_ms: int = 30000
    output_dir: str = "data/output"


def load_config() -> AppConfig:
    return AppConfig(
        headless=os.getenv("HEADLESS", "false").lower() == "true",
        timeout_ms=int(os.getenv("TIMEOUT_MS", "30000")),
        output_dir=os.getenv("OUTPUT_DIR", "data/output"),
    )
