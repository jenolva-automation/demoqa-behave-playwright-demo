from behave import when

@when('the user clicks on Text Box text')
def step_click_text_box(context):
    print("Clicking on Text Box text")
    context.page.get_by_text("Text Box").click()