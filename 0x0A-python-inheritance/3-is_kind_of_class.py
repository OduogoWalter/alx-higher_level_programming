#!/usr/bin/python3
"""Module containing a function to check
if an object is an instance of, or inherited
from, a specified class"""


def is_kind_of_class(obj, a_class):
    """Check if the object is an intance
    of, or inherited from, the specified class"""
    return (isinstance(obj, a_class))
