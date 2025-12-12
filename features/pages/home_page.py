from playwright.sync_api import Page
from playwright.sync_api import expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://demoqa.com"
        self.elements_heading = page.get_by_role("heading", name="Elements") 
        
        
    def navigate(self):
        self.page.goto(self.base_url)
        
    def elements_heading_expect_visible(self) -> bool:
        return expect(self.elements_heading).to_be_visible()    
        
        
    def click_elements_heading(self):
        self.elements_heading.click()    
        
        