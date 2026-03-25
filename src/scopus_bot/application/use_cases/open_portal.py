from scopus_bot.infrastructure.browser.browser_session import BrowserSession
from scopus_bot.infrastructure.portals.base_page import BasePage


class OpenPortalUseCase:
    def __init__(self, headless: bool = True) -> None:
        self.headless = headless

    def execute(self, url: str) -> str:
        session = BrowserSession(headless=self.headless)
        try:
            page = session.start()
            portal_page = BasePage(page)
            portal_page.visit(url)
            return portal_page.title()
        finally:
            session.close()