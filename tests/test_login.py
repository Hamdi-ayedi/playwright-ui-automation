import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_valid_login(page: Page):
    """A valid user lands on the Products page."""
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    expect(page.locator(inventory.TITLE)).to_have_text("Products")
    assert "/inventory.html" in page.url


@pytest.mark.regression
def test_locked_out_user_is_rejected(page: Page):
    """A locked-out user sees an explicit error message."""
    login = LoginPage(page)
    login.load()
    login.login("locked_out_user", "secret_sauce")

    assert "locked out" in login.error_text().lower()


@pytest.mark.regression
def test_wrong_password_is_rejected(page: Page):
    """Bad credentials never reach the inventory page."""
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "wrong_password")

    assert "username and password do not match" in login.error_text().lower()
    assert "/inventory.html" not in page.url
