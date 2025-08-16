from __future__ import annotations
from playwright.sync_api import Page
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage, ShippingInfo

class CheckoutFlow:
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url
        self.products = ProductsPage(page)
        self.cart = CartPage(page)
        self.checkout = CheckoutPage(page)

    def buy_single_item(self, product_name: str, shipping: ShippingInfo) -> None:
        self.products.open(self.base_url)
        self.products.add_to_cart(product_name)
        self.products.open_cart()
        self.cart.expect_item(product_name)
        self.cart.checkout()
        self.checkout.fill_shipping(shipping)
        self.checkout.place_order()
        self.checkout.expect_order_confirmed()
