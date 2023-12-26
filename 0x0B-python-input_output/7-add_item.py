#!/usr/bin/python3
"""Scripts to add command line
arguments to a Python List and save
to a JSON file."""
import sys
from os import path
from json import dump, load
from importlib.machinery import SourceFileLoader

save_to_json_file = SourceFileLoader('module.name',
                                     path.join(path.dirname(__file__),
                                               '5-save_to_json_file.py'
                                               )
                                     ).load_module().save_to_json_file
load_from_json_file = SourceFileLoader('module.name',
                                       path.join(path.dirname(__file__),
                                                 '6-load_from_json_file.py'
                                                 )
                                       ).load_module().load_from_json_file

filename = 'add_item.json'

# Check if the file exists, if not, create an empty list
if path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add command line args to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(my_list, filename)
