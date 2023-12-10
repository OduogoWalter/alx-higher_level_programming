#!usr/bin/python3
"""
Module containing the is_same_class function.
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
    obj: Object to check.
    a_class: Class to compare with.


Returns:
    True if obj is an instance of a_class; otherwise, False.
    """
    return type(obj) is a_class
