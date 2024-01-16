#!/usr/bin/python3
"""
Module for adding two integers
"""


def add_integers(a, b=98):
    """
    Adds two intergers.


    Arguments:
    a (int or float): The first number.
    b (int or float, optional): The second number. Defaults to 98.

    Returns:
    int: The sum of a and b.

    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TyperError("b must be an integer")

    return (int(a) + int(b))
