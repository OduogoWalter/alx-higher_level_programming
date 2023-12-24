#!usr/bin/python3
"""Module to return the JSON representation of an object (string)."""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    Args:
        my_obj: The object to be converted to JSON string

    Returns:
        str: The JSON representation of the object.
    """
    return (json.dumps(my_obj))
