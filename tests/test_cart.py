import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def logged_in_inventory(page: Page) -> InventoryPage:
    """Reusable fixture: log in and return the inventory page object."""
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")
    return InventoryPage(page)


@pytest.mark.smoke
def test_add_single_item_to_cart(logged_in_inventory: InventoryPage):
    logged_in_inventory.add_item_to_cart("sauce-labs-backpack")
    assert logged_in_inventory.cart_count() == 1


@pytest.mark.regression
def test_add_multiple_items_to_cart(logged_in_inventory: InventoryPage):
    logged_in_inventory.add_item_to_cart("sauce-labs-backpack")
    logged_in_inventory.add_item_to_cart("sauce-labs-bike-light")
    logged_in_inventory.add_item_to_cart("sauce-labs-bolt-t-shirt")
    assert logged_in_inventory.cart_count() == 3
