#!/usr/bin/python3
"""Module to convert a class instance to JSON format."""


def class_to_json(obj):
    """Converts a class instance to a dictionary in JSON format."""
    # Get the dictionary representation of the object's __dict__
    obj_dict = obj.__dict__

    # Convert any nested objects to their JSON representations
    for key, value in obj_dict.items():
        if hasattr(value, '__dict__'):
            obj_dict[key] = class_to_json(value)

    return (obj_dict)


if __name__ == "__main__":
    pass
