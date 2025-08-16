from __future__ import annotations
from dataclasses import dataclass
from playwright.sync_api import Page, Locator
from .base_page import BasePage

@dataclass(frozen=True)
class ShippingInfo:
    first_name: str
    last_name: str
    address1: str
    city: str
    zip_code: str
    country: str

class CheckoutPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.first_name: Locator = self.by_test_id("ship-first-name")
        self.last_name: Locator  = self.by_test_id("ship-last-name")
        self.address1: Locator   = self.by_test_id("ship-address1")
        self.city: Locator       = self.by_test_id("ship-city")
        self.zip_code: Locator   = self.by_test_id("ship-zip")
        self.country: Locator    = self.by_test_id("ship-country")
        self.place_order_btn: Locator = self.by_role("button", name="Place Order")
        self.confirmation: Locator = self.by_test_id("order-confirmation")

    def fill_shipping(self, info: ShippingInfo) -> None:
        self.fill(self.first_name, info.first_name)
        self.fill(self.last_name, info.last_name)
        self.fill(self.address1, info.address1)
        self.fill(self.city, info.city)
        self.fill(self.zip_code, info.zip_code)
        self.fill(self.country, info.country)

    def place_order(self) -> None:
        self.click(self.place_order_btn)

    def expect_order_confirmed(self) -> None:
        self.expect_contains_text(self.confirmation, "Thank you")
