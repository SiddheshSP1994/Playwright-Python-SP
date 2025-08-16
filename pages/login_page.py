from __future__ import annotations
from playwright.sync_api import Page, Locator
from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.username_input: Locator = self.by_test_id("login-username")
        self.password_input: Locator = self.by_test_id("login-password")
        self.submit_btn: Locator   = self.by_role("button", name="Sign In")
        self.error_banner: Locator = self.by_test_id("login-error")

    def open(self, base_url: str) -> None:
        self.goto(f"{base_url}/login")
        self.wait_visible(self.username_input)

    def login(self, username: str, password: str) -> None:
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.submit_btn)

    def expect_error(self, message: str) -> None:
        self.expect_contains_text(self.error_banner, message)
