#!/usr/bin/python3

"""Add all arguments to a Python list and save them to a file."""


import sys

if __name__ == "__main__":
    # Checkpoint 3: Ensure that the file "7-save_to_json_file.py" exists in the same directory.
    # If it doesn't, create it and implement the "save_to_json_file" function.
    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
    
    # Checkpoint 4: Confirm that "8-load_from_json_file.py" exists in the same directory.
    # If not, create it and implement the "load_from_json_file" function.
    load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

    try:
        # Checkpoint 5: Verify that the file "add_item.json" exists in the same directory.
        # If not, create it before running the script.
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If the file doesn't exist, initialize an empty list.
        items = []
    
    # Add command-line arguments to the items list.
    items.extend(sys.argv[1:])
    
    # Save the updated items list to "add_item.json".
    save_to_json_file(items, "add_item.json")
