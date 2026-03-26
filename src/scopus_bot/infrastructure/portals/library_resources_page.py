from playwright.sync_api import Page


class LibraryResourcesPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open_resources_in_new_tab(self) -> Page:
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(2000)

        self.page.screenshot(path="debug_extranet_before_resources.png")
        print("Extranet URL:", self.page.url)

        resources_button = self.page.get_by_text(
            "Base de Datos y Libros Electrónicos",
            exact=False,
        ).first

        resources_button.wait_for(state="visible", timeout=15000)

        with self.page.context.expect_page() as new_page_info:
            resources_button.click()

        new_page = new_page_info.value
        new_page.wait_for_load_state("domcontentloaded")
        return new_page

    def scroll_until_scopus_visible(self, max_scrolls: int = 12) -> None:
        for attempt in range(max_scrolls):
            scopus_text = self.page.get_by_text("SCOPUS", exact=False).first
            if scopus_text.is_visible():
                print(f"Scopus found on scroll attempt {attempt + 1}")
                return

            self.page.mouse.wheel(0, 1400)
            self.page.wait_for_timeout(1000)

        self.page.screenshot(path="debug_scopus_not_found.png")
        raise RuntimeError("Scopus entry was not found after scrolling")

    def open_scopus_in_new_tab(self) -> Page:
        scopus_entry = self.page.get_by_text("SCOPUS", exact=False).first
        scopus_entry.wait_for(state="visible", timeout=5000)

        with self.page.context.expect_page() as new_page_info:
            scopus_entry.click()

        new_page = new_page_info.value
        new_page.wait_for_load_state("domcontentloaded")
        return new_page