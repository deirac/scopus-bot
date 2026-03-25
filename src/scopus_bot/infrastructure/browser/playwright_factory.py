from playwright.sync_api import sync_playwright


class PlaywrightFactory:
    def __init__(self, headless: bool = True):
        self.headless = headless

    def launch_browser(self):
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=self.headless)
        context = browser.new_context()
        page = context.new_page()

        return playwright, browser, context, page