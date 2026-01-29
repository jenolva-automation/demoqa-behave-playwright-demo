from playwright.sync_api import Page
from playwright.sync_api import expect


class CheckBoxPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.checkBox_heading = page.get_by_role("heading", name ="Check Box")
        
        self.toggle_button = page.get_by_role("button", name = "Toggle")
        
        self.home_text = "Home"
        self.documents_text = "Documents"
        
        
        
        self.results_list = page.locator("#result .text-success")
        
        
    def checkBox_text_assert_visible(self):
        expect(self.checkBox_heading).to_be_visible()
        
    def click_checkbox_by_name(self, checkbox_name: str):
        self.page.get_by_text(checkbox_name, exact=True).click()
        
    def get_checkbox_state(self, checkbox_name: str) -> str:
        """Returns 'checked', 'unchecked', or 'indeterminate'"""
        checkbox_area = self.page.locator(f'label:has-text("{checkbox_name}")')
        
        if checkbox_area.locator('.rct-icon-check').is_visible():
            return 'checked'
        elif checkbox_area.locator('.rct-icon-uncheck').is_visible():
            return 'unchecked'
        elif checkbox_area.locator('.rct-icon-half-check').is_visible():
            return 'indeterminate'  # Partially checked (some children selected)
        else:
            return 'unknown'
    
    def click_checkbox_area(self, checkbox_name: str):
        """Click the checkbox area directly using the locator approach"""
        checkbox_area = self.page.locator(f'label:has-text("{checkbox_name}")')
        checkbox_area.click()
    
    def smart_checkbox_click(self, checkbox_name: str, desired_state: str = 'checked'):
        """Click checkbox only if it's not already in the desired state"""
        current_state = self.get_checkbox_state(checkbox_name)
        
        if current_state != desired_state:
            self.click_checkbox_area(checkbox_name)
    
    def assert_toggle_button_visible(self):
        """Assert that the toggle button is visible"""
        expect(self.toggle_button).to_be_visible()
    
    def assert_checkbox_tree_visible(self):
        """Assert that the checkbox tree structure is visible"""
        # Use a more reliable selector - look for any checkbox structure
        checkbox_tree = self.page.locator('.rct-options, .rct-node, [class*="rct"]').first
        expect(checkbox_tree).to_be_visible()
        
    def assert_home_checkbox_visible(self):
        """Assert that the Home checkbox is visible"""
        home_checkbox = self.page.locator('label:has-text("Home")')
        expect(home_checkbox).to_be_visible()
        
    def assert_checkbox_fields_visible(self):
        """Assert that all main checkbox components are visible"""
        self.assert_toggle_button_visible()
        self.assert_checkbox_tree_visible()
        self.assert_home_checkbox_visible()
        
    def expand_all_checkboxes(self):
        """Expand all checkbox nodes to make nested items visible"""
        # Click the main toggle button to expand all
        self.toggle_button.click()
        
        # Wait a moment for the expansion to complete
        self.page.wait_for_timeout(500)
        
    def assert_checkbox_output_visible(self):
        """Assert that checkbox selection output/results are visible"""
        # Look for the result section that shows selected checkbox names
        result_section = self.page.locator("#result")
        expect(result_section).to_be_visible()
        
        # Check that "home" appears in the output (since Home checkbox was selected)
        result_text = result_section.text_content()
        print(f"Checkbox output result: {result_text}")
        
        # Assert that the word "home" appears in the output 
        assert "home" in result_text.lower(), f"Expected 'home' to appear in output, but got: {result_text}"
        
    def assert_checkbox_state(self, checkbox_name: str, expected_state: str):
        """Assert that a checkbox is in the expected state"""
        actual_state = self.get_checkbox_state(checkbox_name)
        assert actual_state == expected_state, f"Expected '{checkbox_name}' to be '{expected_state}', but found '{actual_state}'."
        
    def assert_text_visible(self, text: str):
        """Assert that specific text is visible on the page"""
        text_locator = self.page.get_by_text(text, exact=True)
        expect(text_locator).to_be_visible()
        
    def assert_text_visible_tree(self):
        """Recursively assert that all texts in the tree structure are visible"""
        self.assert_text_visible_recursive(self.label_tree)
        
    def get_result_listed_items(self) -> list:    
        """Get a list of items displayed in the results section"""
        selected = self.results_list.all_text_contents()
        return selected
        
    
    def assert_text_visible_recursive(self, tree_dict):
        """Helper method to recursively assert text visibility"""
        for key, value in tree_dict.items():
            if isinstance(value, list):
                # It's a list of leaf nodes
                for item in value:
                    self.assert_text_visible(item.lower())
                    print(f"*****Asserted visibility of text: {item}***********")
            elif isinstance(value, dict):
                # It's a nested dictionary
                self.assert_text_visible(key)  # Assert parent node
                self.assert_text_visible_recursive(value)  # Recurse into children
                
    def tree_to_list(self, node, result=None) -> list:
        if result is None:
            result = []

        if isinstance(node, dict):
            for key, value in node.items():
                result.append(key)              # add the key
                self.tree_to_list(value, result)     # recurse into the value

        elif isinstance(node, list):
            for item in node:
                result.append(item)             # add list items

        print(f"***Current flattened list: {result}")
        return result

    def selectedKeys_to_list(self, tree, selected_keys: list) -> list:
        result = []
    
        def extract_all_strings(node, include_key=None):
            # Add the key itself if specified
            if include_key:
                result.append(include_key)
                
            if isinstance(node, dict):
                for key, value in node.items():
                    result.append(key)  # Add the key
                    extract_all_strings(value)  # Recurse into the value
                    
            elif isinstance(node, list):
                for item in node:
                    if isinstance(item, str):
                        result.append(item)  # Add string items
                    else:
                        extract_all_strings(item)  # Recurse if not string
        
        # Process each selected key
        for selected_key in selected_keys:
            if selected_key in tree:
                extract_all_strings(tree[selected_key], include_key=selected_key)
                print(f"***Processed selected key: {selected_key}")
        
        print(f"***Final result: {result}")
        return result