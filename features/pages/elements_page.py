from playwright.sync.api import Page
from playwright.sync.api import expect

class ElementsPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements_text = page.get_by_text("Elements")
        
    def elements_text_assert_visible(self) -> bool:
        return expect(self.elements_text).to_be_visible()
        
        