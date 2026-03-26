from scopus_bot.infrastructure.browser.browser_session import BrowserSession
from scopus_bot.infrastructure.portals.tdea_login_page import TdeaLoginPage
from scopus_bot.settings.config import load_config


class LoginToPortalUseCase:
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
            page = session.start()
            login_page = TdeaLoginPage(page)
            login_page.login(
                url=config.portal_url,
                username=config.scopus_username,
                password=config.scopus_password,
            )
        finally:
            session.close()