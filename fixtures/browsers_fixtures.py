from pathlib import Path

import pytest
from datetime import datetime
from playwright.sync_api import sync_playwright
from pages.wikipediaPage import WikipediaPage

@pytest.fixture(scope="function")
def browser(request):
    with sync_playwright() as pw:
        browser_type = request.config.getoption("--browser-type")
        browser = getattr(pw, browser_type).launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser, request):
    context=browser.new_context()
    page = context.new_page()
    yield page

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        Path("screenshots").mkdir(exist_ok=True)
        ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        page.screenshot(path=f"screenshots/{request.node.name}_{ts}.png")
    context.close()

@pytest.fixture
def wikipedia(page):
    return WikipediaPage(page)

