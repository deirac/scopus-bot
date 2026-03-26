from playwright.sync_api import Page


class ScopusSearchPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def wait_until_ready(self) -> None:
        self.page.wait_for_load_state("networkidle")

    def search(self, query: str) -> None:
        self.wait_until_ready()
        search_input = self.page.locator("input").first
        search_input.fill(query)