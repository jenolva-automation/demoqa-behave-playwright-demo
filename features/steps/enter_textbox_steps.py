from behave import given, when, then
from features.pages.elements_page import ElementsPage
from features.pages.textbox_page import TextBoxPage

@when('the user clicks on Elements text')
def step_click_elements_text(context):
    print("Clicking on Elements text")
    elementsPage = ElementsPage(context.page)
    elementsPage.elements_text_assert_visible()     
    elementsPage.click_elements_text()
    
  
@then('the Text Box text should be visible')
def step_expect_textbox_text_visible(context):
    print("Asserting that Text Box text is visible")
    textboxPage = TextBoxPage(context.page)
    
    # Wait for page to load before assertion
    context.page.wait_for_load_state("networkidle")
    textboxPage.textbox_text_assert_visible()
    
    
    
def step_expect_textbox_text_visible(context):
    print("Asserting that Text Box text is visible")
    textboxPage = TextBoxPage(context.page)
    
    # Wait for page to load before assertion
    context.page.wait_for_load_state("networkidle")
    textboxPage.textbox_text_assert_visible()
    
    
@then('the form text, textbox fields and submit button be visible')
def step_expect_form_fields_visible(context):
    print("Asserting that form text, textbox fields and submit button are visible")
    textboxPage = TextBoxPage(context.page)
    textboxPage.fullName_text_assert_visible()
    textboxPage.fullName_textbox_assert_visible()
    textboxPage.email_text_assert_visible()
    textboxPage.email_textbox_assert_visible()
    textboxPage.currentAddress_text_assert_visible()
    textboxPage.currentAddress_textbox_assert_visible()
    textboxPage.permanentAddress_text_assert_visible()
    textboxPage.permanentAddress_textbox_assert_visible()
    textboxPage.submit_button_assert_visible()
    
@then('the form text fields are empty')
def step_expect_form_fields_empty(context):
    print("Asserting that form text fields are empty")
    textboxPage = TextBoxPage(context.page)
    textboxPage.fullName_textbox_assert_empty()
    textboxPage.email_textbox_assert_empty()
    textboxPage.currentAddress_textbox_assert_empty()
    textboxPage.permanentAddress_textbox_assert_empty()
    
    
