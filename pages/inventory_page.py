from pages.base_page import BasePage


class InventoryPage(BasePage):
    """The products / inventory page shown after a successful login."""

    TITLE = ".title"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"

    def title_text(self) -> str:
        return self.page.locator(self.TITLE).inner_text()

    def add_item_to_cart(self, item_slug: str):
        """item_slug example: 'sauce-labs-backpack'."""
        self.page.click(f"#add-to-cart-{item_slug}")

    def cart_count(self) -> int:
        badge = self.page.locator(self.CART_BADGE)
        return int(badge.inner_text()) if badge.count() > 0 else 0
