from scopus_bot.infrastructure.browser.browser_session import BrowserSession
from scopus_bot.infrastructure.portals.library_resources_page import LibraryResourcesPage
from scopus_bot.infrastructure.portals.scopus_search_page import ScopusSearchPage
from scopus_bot.infrastructure.portals.tdea_login_page import TdeaLoginPage
from scopus_bot.settings.config import load_config


class RunBasicSearchUseCase:
    def execute(self, query: str) -> None:
        config = load_config()

        if not config.portal_url:
            raise ValueError("PORTAL_URL is not configured")
        if not config.scopus_username:
            raise ValueError("SCOPUS_USERNAME is not configured")
        if not config.scopus_password:
            raise ValueError("SCOPUS_PASSWORD is not configured")

        session = BrowserSession(headless=config.headless)

        try:
            initial_page = session.start()

            login_page = TdeaLoginPage(initial_page)
            login_page.login(
                url=config.portal_url,
                username=config.scopus_username,
                password=config.scopus_password,
            )

            resources_page = LibraryResourcesPage(initial_page)
            resources_tab = resources_page.open_resources_in_new_tab()

            resources_portal = LibraryResourcesPage(resources_tab)
            resources_portal.scroll_until_scopus_visible()
            scopus_tab = resources_portal.open_scopus_in_new_tab()

            search_page = ScopusSearchPage(scopus_tab)
            search_page.search(query)

            scopus_tab.screenshot(path="debug_search_results.png")
            print("Search URL:", scopus_tab.url)

        finally:
            session.close()