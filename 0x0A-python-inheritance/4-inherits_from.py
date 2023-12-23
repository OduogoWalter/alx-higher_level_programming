#!/usr/bin/python3
"""Module containing a function to check
if an object is an object is an instance of
a class that inherited from a specified class"""


def inherits_from(obj, a_class):
    """Check if the object is an instance of a
    class that inherited from the specified class"""
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
