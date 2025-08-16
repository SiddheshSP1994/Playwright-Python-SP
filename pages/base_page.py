from __future__ import annotations
from typing import Optional
from playwright.sync_api import Page, Locator, expect

class BasePage:
    def __init__(self, page: Page, default_timeout_ms: int = 10000) -> None:
        self.page = page
        self.default_timeout_ms = default_timeout_ms

    def goto(self, url: str) -> None:
        self.page.goto(url, wait_until="domcontentloaded")

    def wait_for_url_contains(self, fragment: str, timeout_ms: Optional[int] = None) -> None:
        timeout = timeout_ms or self.default_timeout_ms
        self.page.wait_for_url(f"**{fragment}**", timeout=timeout)

    def el(self, selector: str) -> Locator:
        return self.page.locator(selector)

    def by_test_id(self, test_id: str) -> Locator:
        return self.page.get_by_test_id(test_id)

    def by_role(self, role: str, name: Optional[str] = None) -> Locator:
        return self.page.get_by_role(role=role, name=name) if name else self.page.get_by_role(role=role)

    def wait_visible(self, locator: Locator, timeout_ms: Optional[int] = None) -> None:
        timeout = timeout_ms or self.default_timeout_ms
        locator.wait_for(state="visible", timeout=timeout)

    def wait_hidden(self, locator: Locator, timeout_ms: Optional[int] = None) -> None:
        timeout = timeout_ms or self.default_timeout_ms
        locator.wait_for(state="hidden", timeout=timeout)

    def click(self, locator: Locator) -> None:
        self.wait_visible(locator); locator.click()

    def fill(self, locator: Locator, value: str, clear: bool = True) -> None:
        self.wait_visible(locator)
        if clear: locator.fill("")
        locator.fill(value)

    def expect_text(self, locator: Locator, expected: str, timeout_ms: Optional[int] = None) -> None:
        timeout = timeout_ms or self.default_timeout_ms
        expect(locator).to_have_text(expected, timeout=timeout)

    def expect_contains_text(self, locator: Locator, fragment: str, timeout_ms: Optional[int] = None) -> None:
        timeout = timeout_ms or self.default_timeout_ms
        expect(locator).to_contain_text(fragment, timeout=timeout)
