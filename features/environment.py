#Configuration file to define hooks and setup/teardown functions run in features, scenarios or steps

# Hook to run before all features - creates a Playwright instance
def before_all(context):
    # Skip browser setup during dry runs
    if context.config.dry_run:
        print("Dry run detected - skipping browser setup")
        return
        
    print("Before_all hook is running!")
    from playwright.sync_api import sync_playwright
    context.playwright = sync_playwright().start()
    print("Playwright started successfully")
    

# Hook to run before each scenario - launches a new browser and page    
def before_scenario(context, scenario):
    # Skip browser setup during dry runs
    if context.config.dry_run:
        print("Dry run detected - skipping browser setup")
        return
        
    print("Before_scenario hook is running!")
    # Debug mode options
    context.browser = context.playwright.chromium.launch(
        headless=False,          # Show browser
        slow_mo=1000,           # Slow down actions by 1000ms
        devtools=True           # Open DevTools
    )
    context.page = context.browser.new_page()
    print("Browser and page created successfully")

# Hook to run after each scenario - handles cleanup and failure screenshots
def after_scenario(context, scenario):
    print("After_scenario hook is running!")
    
    # Take screenshot if scenario failed
    if scenario.status == "failed":
        import os
        from datetime import datetime
        import allure
        
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/FAILED_{scenario.name.replace(' ', '_')}_{timestamp}.png"
        
        # Take screenshot and get binary data
        screenshot_bytes = context.page.screenshot(path=filename, full_page=True)
        
        # Attach failure screenshot to Allure report
        allure.attach(
            screenshot_bytes,
            name=f"FAILURE: {scenario.name}",
            attachment_type=allure.attachment_type.PNG
        )
        
        print(f"❌ Failure screenshot saved: {filename} and attached to Allure report")
    
    # Close browser
    context.browser.close()
    print("Browser closed successfully")
        
# Hook to run after each scenario - closes the browser
def after_scenario(context, scenario):
    if hasattr(context, 'browser'):
        context.browser.close()
        
# Hook to run after all features - stops the Playwright instance
def after_all(context):
    if hasattr(context, 'playwright'):
        context.playwright.stop()
    