"""Global fixtures and utilities for Playwright‑Pytest lab.

This file defines session‑scoped fixtures to manage the Playwright browser
instance and create new pages for each test.  It can be extended with
additional fixtures for authenticated sessions, API clients or custom
configuration.
"""
import os
import pytest
from playwright.sync_api import sync_playwright, Browser, Page


@pytest.fixture(scope="session")
def playwright_instance():
    """Start and yield a Playwright instance for the entire session."""
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance: "sync_playwright") -> Browser:
    """Launch a headless Chromium browser for the session.

    Modify this fixture to choose a different browser or make it dynamic
    based on command line options.
    """
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser: Browser) -> Page:
    """Create a new browser page for each test function."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()