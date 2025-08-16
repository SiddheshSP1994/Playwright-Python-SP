from __future__ import annotations
from playwright.sync_api import Page, Locator
from .base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page_title: Locator = self.by_role("heading", name="Your Cart")
        self.checkout_btn: Locator = self.by_role("button", name="Checkout")

    def expect_item(self, name: str) -> None:
        self.expect_contains_text(self.page.locator("[data-testid='cart-items']"), name)

    def checkout(self) -> None:
        self.click(self.checkout_btn)
