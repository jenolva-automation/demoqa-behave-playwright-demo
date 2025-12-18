from playwright.sync_api import Page
from playwright.sync_api import expect

class ElementsPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements_text = page.get_by_text("Elements")
        
        self.textBox_listitem = page.get_by_role("listitem").get_by_text("Text Box")
        self.checkBox_listitem = page.get_by_role("listitem").get_by_text("Check Box")
        self.radioButton_listitem = page.get_by_role("listitem").get_by_text("Radio Button")
        self.webTables_listitem = page.get_by_role("listitem").get_by_text("Web Tables")
        self.buttons_listitem = page.get_by_role("listitem").get_by_text("Buttons")
        self.links_listitem = page.get_by_role("listitem").get_by_text("Links")
        self.brokenLinks_listitem = page.get_by_role("listitem").get_by_text("Broken Links - Images")
        self.uploadAndDownload_listitem = page.get_by_role("listitem").get_by_text("Upload and Download")
        self.dynamicProperties_listitem = page.get_by_role("listitem").get_by_text("Dynamic Properties")
        
        
        
        
    def elements_text_assert_visible(self) -> bool:
        return expect(self.elements_text).to_be_visible()
        
    def click_elements_text(self):
        self.elements_text.click()
        
    def textBox_listitem_assert_visible(self) -> bool:
        return expect(self.textBox_listitem).to_be_visible()
    
    def click_textBox_listitem(self):
        self.textBox_listitem.click()
        
    def checkBox_listitem_assert_visible(self) -> bool:
        return expect(self.checkBox_listitem).to_be_visible()
    
    def click_checkBox_listitem(self):
        self.checkBox_listitem.click() 
        
        