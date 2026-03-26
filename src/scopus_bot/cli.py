from scopus_bot.application.use_cases.open_scopus_portal import OpenScopusPortalUseCase


def main() -> None:
    use_case = OpenScopusPortalUseCase()
    use_case.execute()


if __name__ == "__main__":
    main()