from playwright.sync_api import Page


class BasePage:
    """Common behaviour shared by every page object."""

    BASE_URL = "https://www.saucedemo.com"

    def __init__(self, page: Page):
        self.page = page

    def open(self, path: str = "/"):
        """Navigate to a path relative to the application base URL."""
        self.page.goto(f"{self.BASE_URL}{path}")

    def title(self) -> str:
        return self.page.title()
