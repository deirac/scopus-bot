from playwright.sync_api import Page


class TdeaLoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def visit(self, url: str) -> None:
        self.page.goto(url)
        self.page.wait_for_load_state("domcontentloaded")

    def open_login_modal(self) -> None:
        button = self.page.get_by_role(
            "button",
            name="Iniciar sesión con cuenta local",
        )
        button.wait_for(state="visible", timeout=10000)
        button.click()

    def wait_for_login_modal(self) -> None:
        self.page.locator("#modalInicioSesion").wait_for(
            state="visible",
            timeout=5000,
        )

    def fill_username(self, username: str) -> None:
        self.page.locator("#modalInicioSesion #username").fill(username)

    def fill_password(self, password: str) -> None:
        self.page.locator("#modalInicioSesion #password").fill(password)

    def submit(self) -> None:
        self.page.locator("#ingresar").click()

    def wait_for_post_login_page(self) -> None:
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(2000)

    def login(self, url: str, username: str, password: str) -> None:
        self.visit(url)
        self.open_login_modal()
        self.wait_for_login_modal()
        self.fill_username(username)
        self.fill_password(password)
        self.submit()
        self.wait_for_post_login_page()