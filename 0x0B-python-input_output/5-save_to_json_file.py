#!/usr/bin/python3
"""Module to save an object to a text file using a JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """
    Save an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be saved.
        filename (str): The name of the file to save the object to.

    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
