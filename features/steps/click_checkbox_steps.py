from behave import given, when, then, step
from features.pages.elements_page import ElementsPage
from features.pages.checkbox_page import CheckBoxPage
import os
from datetime import datetime
import allure

def take_screenshot(context, name):
    """Helper function to take screenshots with timestamp and attach to Allure"""
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshots/{name}_{timestamp}.png"
    
    # Take screenshot and get binary data
    screenshot_bytes = context.page.screenshot(path=filename, full_page=True)
    
    # Attach to Allure report
    allure.attach(
        screenshot_bytes,
        name=name,
        attachment_type=allure.attachment_type.PNG
    )
    
    print(f"Screenshot saved: {filename} and attached to Allure report")
    return filename

@when('the user clicks Check Box text')
def step_click_check_box_text(context):
    print("Clicking on Check Box text")
    
    elementsPage = ElementsPage(context.page)
    elementsPage.checkBox_listitem_assert_visible()
    elementsPage.click_checkBox_listitem()

@then('the Check Box text and fields will be visible')
def step_checkbox_items_visible(context):
    print("Asserting that Check Box text and fields are visible")
    checkboxPage = CheckBoxPage(context.page)
    checkboxPage.checkBox_text_assert_visible()
    checkboxPage.assert_checkbox_fields_visible()
    
@when('the user clicks the Home checkbox from unchecked state')
def step_click_home_checkbox_unchecked(context):
    print(f"Clicking Home checkbox from unchecked state")
    checkboxPage = CheckBoxPage(context.page)
    
    # Screenshot before action
    take_screenshot(context, "before_home_checkbox_click")
    
    # Verify it's unchecked first
    current_state = checkboxPage.get_checkbox_state("Home")
    print(f"Home checkbox current state: {current_state}")
    # Click to check it
    checkboxPage.click_checkbox_by_name("Home")
    
    # Screenshot after action
    take_screenshot(context, "after_home_checkbox_click")
    
    after_state = checkboxPage.get_checkbox_state("Home")
    print(f"Home checkbox state after click: {after_state}")
    assert after_state == 'checked', "Home checkbox should be checked after clicking"
    
@then('all labels should be displayed in the output section')
def step_assert_labels_under_home_visible(context):
    print("Asserting that all labels are displayed in the output section")
    
    # Take a screenshot before assertion
    context.page.screenshot(path="screenshots/before_output_check.png")
    
    checkboxPage = CheckBoxPage(context.page)
    # Look for the result/output section that shows selected checkbox values
    checkboxPage.assert_checkbox_output_visible()
    
    # Expand the checkbox tree first to make nested items visible
    checkboxPage.expand_all_checkboxes()
    
    # Then check that tree items are visible in the react-checkbox-tree
    checkboxPage.assert_text_visible_tree()
    
    # Take a screenshot after successful assertion
    context.page.screenshot(path="screenshots/after_output_check.png")
    print("Screenshots saved: before_output_check.png and after_output_check.png")

@then('all labels under Home should be displayed in the output')
def step_all_labels_under_home_displayed_alt(context):
    print("Asserting that all labels under Home are displayed in the output")
    take_screenshot(context, "home_labels_output_check")
    
    checkboxPage = CheckBoxPage(context.page)
    checkboxPage.assert_checkbox_output_visible()
