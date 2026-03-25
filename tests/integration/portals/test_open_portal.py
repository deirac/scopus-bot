from scopus_bot.application.use_cases.open_portal import OpenPortalUseCase


def test_open_portal_returns_title():
    use_case = OpenPortalUseCase(headless=True)

    title = use_case.execute("https://example.com")

    assert "Example" in title