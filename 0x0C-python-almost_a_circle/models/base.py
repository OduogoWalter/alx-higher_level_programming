#!/usr/bin/python3
"""Module for the Base class."""

import json


class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance with an optional id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation
        of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
