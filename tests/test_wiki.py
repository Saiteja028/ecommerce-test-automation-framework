from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.smoke
def test_wikipedia(wikipedia):
    wikipedia.goto()
    wikipedia.expect_loaded()


@pytest.mark.regression
def test_Wiki_seach(wikipedia):
    wikipedia.goto()
    wikipedia.search("Hyderabad")

    
