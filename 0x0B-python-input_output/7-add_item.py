#!/usr/bin/python3

"""Add all arguments to a Python list and save them to a file."""

import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        # Attempt to load existing data from "add_item.json"
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If "add_item.json" doesn't exist, initialize an empty list
        items = []

    # Extend the list with command-line arguments
    items.extend(sys.argv[1:])

    # Save the updated list to "add_item.json"
    save_to_json_file(items, "add_item.json")
