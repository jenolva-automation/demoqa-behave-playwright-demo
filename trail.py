def flatten_tree(node, result=None):
    if result is None:
        result = []

    if isinstance(node, dict):
        for key, value in node.items():
            result.append(key)              # add the key
            flatten_tree(value, result)     # recurse into the value

    elif isinstance(node, list):
        for item in node:
            result.append(item)             # add list items

    print(f"***Current flattened list: {result}")
    return result

def get_selected_keys_and_values(tree, selected_keys: list) -> list:
    """
    Get all strings from selected keys including the keys themselves and all nested values
    
    Args:
        tree: The dictionary tree structure
        selected_keys: List of keys to extract data from
        
    Returns:
        List containing the selected keys and all their nested string values
    """
    result = []
    
    def extract_all_strings(node, include_key=None):
        """Helper function to recursively extract all strings from a node"""
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
 
def main():
    print("Hello World!")
    
    tree = {
        "Home": {
            "Desktop": ["Notes", "Commands"],
            "Documents": {
                "WorkSpace": ["React", "Angular", "Veu"],
                "Office": ["Public", "Private", "Classified", "General"]                
            }
        }
    }
    
    # Now you can use the tree with your functions
    result = []
    flatten_tree(tree, result)
    print("*******************")
    print(f"Final flattened list: {result}")
    
    # Test the new function with selected keys
    selected_keys = ["Desktop", "Documents"]
    selected_result = get_selected_keys_and_values(tree["Home"], selected_keys)
    print("________________________")
    print(f"Selected keys and all their values: {selected_result}")
    
    # Test with just one key
    single_key_result = get_selected_keys_and_values(tree["Home"], ["Desktop"])
    print("________________________")
    print(f"Single key result: {single_key_result}")      

if __name__ == "__main__":
    main()