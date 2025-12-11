from behave import given, when, then
from features.pages.home_page import HomePage

@given('the user navigates to the home page')
def step_navigate_to_home_page(context):
    print("Navigating to the home page")
    homePage = HomePage(context.page)
    homePage.navigate()
        
@then('the Elements heading should be visible')
def step_expect_elements_heading_visible(context):
    print("Assert that Elements heading is to be visible")
    homePage = HomePage(context.page)
    homePage.elements_heading_expect_visible()
    homePage.elements_heading_expect_visible
    