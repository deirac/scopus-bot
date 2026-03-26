from scopus_bot.infrastructure.browser.browser_session import BrowserSession
from scopus_bot.infrastructure.portals.library_resources_page import LibraryResourcesPage
from scopus_bot.infrastructure.portals.tdea_login_page import TdeaLoginPage
from scopus_bot.settings.config import load_config


class OpenScopusPortalUseCase:
    def execute(self) -> None:
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

            initial_page.screenshot(path="debug_after_login.png")
            print("URL after login:", initial_page.url)

            resources_page = LibraryResourcesPage(initial_page)
            resources_tab = resources_page.open_resources_in_new_tab()

            resources_tab.screenshot(path="debug_resources_tab.png")
            print("Resources tab URL:", resources_tab.url)

            resources_portal = LibraryResourcesPage(resources_tab)
            resources_portal.scroll_until_scopus_visible()
            scopus_tab = resources_portal.open_scopus_in_new_tab()

            scopus_tab.wait_for_load_state("networkidle")
            scopus_tab.screenshot(path="debug_scopus_landing.png")
            print("Scopus URL:", scopus_tab.url)

            scopus_tab.wait_for_timeout(5000)

        finally:
            session.close()