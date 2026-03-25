from scopus_bot.infrastructure.browser.playwright_factory import PlaywrightFactory


def test_browser_launch():
    factory = PlaywrightFactory(headless=True)

    playwright, browser, context, page = factory.launch_browser()

    page.goto("https://example.com")

    assert "Example" in page.title()

    browser.close()
    playwright.stop()