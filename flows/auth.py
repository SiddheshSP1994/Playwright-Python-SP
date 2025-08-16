from __future__ import annotations
from typing import Tuple
from playwright.sync_api import Page
from pages.login_page import LoginPage

class AuthFlow:
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url
        self.login_page = LoginPage(page)

    def login_via_ui(self, username: str, password: str) -> None:
        self.login_page.open(self.base_url)
        self.login_page.login(username, password)

    def expect_login_failed(self, message: str) -> None:
        self.login_page.expect_error(message)

    def login_and_return_context(self, username: str, password: str) -> Tuple[str, str]:
        self.login_via_ui(username, password)
        return (username, self.page.context.storage_state(path=None))
