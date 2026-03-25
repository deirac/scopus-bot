#test/unit/
from scopus_bot.settings.config import load_config

def test_load_config_defaults():
    config = load_config()

    assert config.timeout_ms == 30000
    assert config.output_dir == "data/output"
    assert config.headless is False


def test_load_config_from_env(monkeypatch):
    monkeypatch.setenv("HEADLESS", "true")
    monkeypatch.setenv("TIMEOUT_MS", "50000")

    config = load_config()

    assert config.headless is True
    assert config.timeout_ms == 50000