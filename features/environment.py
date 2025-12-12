#Configuration file to define hooks and setup/teardown functions run in features, scenarios or steps

# Hook to run before all features - creates a Playwright instance
def before_all(context):
    print("DEBUG: before_all hook is running!")
    from playwright.sync_api import sync_playwright
    context.playwright = sync_playwright().start()
    print("DEBUG: Playwright started successfully")
    

# Hook to run before each scenario - launches a new browser and page    
def before_scenario(context, scenario):
    print("DEBUG: before_scenario hook is running!")
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    print("DEBUG: Browser and page created successfully")
        
# Hook to run after each scenario - closes the browser
def after_scenario(context, scenario):
    if hasattr(context, 'browser'):
        context.browser.close()
        
# Hook to run after all features - stops the Playwright instance
def after_all(context):
    if hasattr(context, 'playwright'):
        context.playwright.stop()
    