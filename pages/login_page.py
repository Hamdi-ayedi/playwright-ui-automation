from pages.base_page import BasePage


class LoginPage(BasePage):
    """The Swag Labs login screen (https://www.saucedemo.com)."""

    # Locators are kept here so a UI change is fixed in ONE place.
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = '[data-test="error"]'

    def load(self):
        self.open("/")

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def error_text(self) -> str:
        return self.page.locator(self.ERROR_MESSAGE).inner_text()
