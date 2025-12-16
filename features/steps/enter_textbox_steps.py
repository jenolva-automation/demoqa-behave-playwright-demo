from behave import given, when, then, step
from features.pages.elements_page import ElementsPage
from features.pages.textbox_page import TextBoxPage

@when('the user clicks on Elements text')
def step_click_elements_text(context):
    print("Clicking on Elements text")
    elementsPage = ElementsPage(context.page)
    elementsPage.elements_text_assert_visible()     
    elementsPage.click_elements_text()

@when('the user clicks on Text Box text')
def step_click_text_box_text(context):
    print("Clicking on Text Box text")
    
    elementsPage = ElementsPage(context.page)
    elementsPage.textBox_listitem_assert_visible()
    elementsPage.click_textBox_listitem()

@then('the form text, textbox fields and submit button be visible')
def step_expect_form_fields_visible(context):
    print("Asserting that form text, textbox fields and submit button are visible")
    textboxPage = TextBoxPage(context.page)
    textboxPage.textbox_text_assert_visible()
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
    
    
@then('the Text Box text is visible')
def step_expect_textbox_text_visible(context):
    print("Asserting that Text Box text is visible")
    textboxPage = TextBoxPage(context.page)
    textboxPage.textbox_text_assert_visible()

@when('the user enters "{fullName}" into Full Name textbox')
def step_enter_fullName(context, fullName):
    print(f"Entering '{fullName}' into Full Name textbox")
    textboxPage = TextBoxPage(context.page)
    textboxPage.enter_fullName(fullName)
    
@when('the user enters "{email}" into Email textbox')
def step_enter_email(context, email):
    print(f"Entering '{email}' into Email textbox")
    textboxPage = TextBoxPage(context.page)
    textboxPage.enter_email(email)
    
@when('the user enters "{currentAddress}" into Current Address textbox')
def step_enter_currentAddress(context, currentAddress):
    print(f"Entering '{currentAddress}' into Current Address textbox")
    textboxPage = TextBoxPage(context.page)
    textboxPage.enter_currentAddress(currentAddress)
    
@when('the user enters "{permanentAddress}" into Permanent Address textbox')
def step_enter_permanentAddress(context, permanentAddress):
    print(f"Entering '{permanentAddress}' into Permanent Address textbox")
    textboxPage = TextBoxPage(context.page)
    textboxPage.enter_permanentAddress(permanentAddress)

@when('the user clicks on Submit button')
def step_click_submit_button(context):
    print("Clicking on Submit button")
    textboxPage = TextBoxPage(context.page)
    textboxPage.submit_button.click()
    
@then('the entered full name: "{fullName}" in textbox should be displayed in the name output')
def step_verify_fullName_output(context, fullName):
    print("Verifying Full Name output")
    textboxPage = TextBoxPage(context.page)
    textboxPage.fullName_output_assert_contains_text(fullName)

@then('the entered email: "{email}" in textbox should be displayed in the email output')
def step_verify_email_output(context, email):
    print("Verifying Email output")
    textboxPage = TextBoxPage(context.page)
    textboxPage.email_output_assert_contains_text(email)
    
@then('the entered current address: "{currentAddress}" in textbox should be displayed in the output')
def step_verify_currentAddress_output(context, currentAddress):
    print("Verifying Current Address output")
    textboxPage = TextBoxPage(context.page)
    textboxPage.currentAddress_output_assert_contains_text(currentAddress)
    
@then('the entered permanent address: "{permanentAddress}" in textbox should be displayed in the output')
def step_verify_permanentAddress_output(context, permanentAddress): 
    print("Verifying Permanent Address output")
    textboxPage = TextBoxPage(context.page)
    textboxPage.permanentAddress_output_assert_contains_text(permanentAddress)