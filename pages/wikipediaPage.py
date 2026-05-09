from playwright.sync_api import Page,expect

class WikipediaPage:
    def __init__(self, page: Page):
        self.page=page
        self.search_input = "#searchInput"
        self.search_button = "button[type='submit']"

    def goto(self):
        self.page.goto("https://wikipedia.com")
    
    def search(self, term:str):
        self.page.locator(self.search_input).fill(term)
        self.page.locator(self.search_button ).click()

    def expect_loaded(self):
        expect(self.page.locator("#www-wikipedia-org")).to_be_visible()