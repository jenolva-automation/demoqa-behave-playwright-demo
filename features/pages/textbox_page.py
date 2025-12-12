from playwright.sync_api import Page
from playwright.sync_api import expect

class TextBoxPage:
    def __init__(self, page: Page):
        self.page = page
        self.textbox_text = page.get_by_text("Text Box")
        self.fullName_text = page.get_by_text("Full Name")
        self.fullName_textbox = page.get_by_role("textbox", name="Full Name")
        self.email_text = page.get_by_text("Email")
        self.email_textbox = page.get_by_role("textbox", name="name@example.com")
        self.currentAddress_text = page.get_by_text("Current Address")
        self.currentAaddress_textbox = page.get_by_role("textbox", name="Current Address")
        self.permanentAddress_text = page.get_by_text("Permanent Address")
        self.permanentAddress_textbox = page.locator("#permanentAddress")
        self.submit_button = page.get_by_role("button", name="Submit")
        
    def textbox_text_assert_visible(self) -> bool:
        return expect(self.textbox_text).to_be_visible()
        
    def click_textbox_text(self):
        self.textbox_text.click()    
        
    def fullName_text_assert_visible(self) -> bool:
        return expect(self.fullName_text).to_be_visible()
    def fullName_textbox_assert_visible(self) -> bool:
        return expect(self.fullName_textbox).to_be_visible()
    
    def email_text_assert_visible(self) -> bool:
        return expect(self.email_text).to_be_visible()
    def email_textbox_assert_visible(self) -> bool:
        return expect(self.email_textbox).to_be_visible()
    
    def currentAddress_text_assert_visible(self) -> bool:
        return expect(self.currentAddress_text).to_be_visible()
    def currentAddress_textbox_assert_visible(self) -> bool:
        return expect(self.currentAaddress_textbox).to_be_visible()
    def currentAddress_textbox_assert_empty(self) -> bool:
        return expect(self.currentAaddress_textbox).to_be_empty()
    
    def permanentAddress_text_assert_visible(self) -> bool:
        return expect(self.permanentAddress_text).to_be_visible()
    def permanentAddress_textbox_assert_visible(self) -> bool:
        return expect(self.permanentAddress_textbox).to_be_visible()
    def permanentAddress_textbox_assert_empty(self) -> bool:
        return expect(self.permanentAddress_textbox).to_be_empty()
    
    def enter_fullName(self, fullName: str):
        self.fullName_textbox.fill(fullName)
        
    def enter_email(self, email: str):
        self.email_textbox.fill(email)
        
    def enter_currentAddress(self, currentAddress: str):
        self.currentAaddress_textbox.fill(currentAddress)
    
    def enter_permanentAddress(self, permanentAddress: str):
        self.permanentAddress_textbox.fill(permanentAddress)
        
    def submit_button_assert_visible(self):
        return expect(self.submit_button).to_be_visible()
        
    def fullName_textbox_assert_empty(self):
        return expect(self.fullName_textbox).to_be_empty()
        
    def email_textbox_assert_empty(self):
        return expect(self.email_textbox).to_be_empty()