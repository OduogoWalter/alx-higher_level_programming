#!/usr/bin/python3
"""Module containing a class BaseGeometry
with area and integer_validator methods"""


from multiprocessing import Value


class BaseGeometry:
    """A class with integer_validator methods"""

    def area(self):
        """Raises an exception with the message 'area() is not implemented'"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, Value):
        """Validates the value and raises exceptions if necessary"""
        if not isinstance(Value, int):
            raise TypeError("{} must be an integer".format(name))
        if Value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
