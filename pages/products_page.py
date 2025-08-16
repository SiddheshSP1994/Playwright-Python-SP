from __future__ import annotations
from playwright.sync_api import Page, Locator
from .base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page_title: Locator = self.by_role("heading", name="Products")
        self.cart_icon: Locator  = self.by_test_id("cart-link")

    def open(self, base_url: str) -> None:
        self.goto(f"{base_url}/products")
        self.wait_visible(self.page_title)

    def product_tile(self, name: str) -> Locator:
        return self.by_test_id(f"product-{name.lower().replace(' ', '-')}")

    def add_button_for(self, name: str) -> Locator:
        return self.product_tile(name).get_by_role("button", name="Add to Cart")

    def add_to_cart(self, name: str) -> None:
        self.click(self.add_button_for(name))

    def open_cart(self) -> None:
        self.click(self.cart_icon)
