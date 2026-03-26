from scopus_bot.settings.config import load_config
from scopus_bot.application.use_cases.login_to_portal import LoginToPortalUseCase


def main() -> None:
    config = load_config()
    print(f"PORTAL_URL cargada: {config.portal_url!r}")
    print(f"USERNAME cargado: {config.scopus_username!r}")
    print(f"ENV detectado")

    use_case = LoginToPortalUseCase()
    use_case.execute()


if __name__ == "__main__":
    main()