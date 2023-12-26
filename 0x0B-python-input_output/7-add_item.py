#!/usr/bin/python3
"""Scripts to add command line
arguments to a Python List and save
to a JSON file."""
from sys import argv
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Check if file exists, load content, or create an empty list
if path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add arguments to the list
for arg in argv[1:]:
    my_list.append(arg)

# Save the updated list to the file
save_to_json_file(my_list, filename)
