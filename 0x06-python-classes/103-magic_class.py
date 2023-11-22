#!/usr/bin/python3
"""Defines the MagicClass class that replicates given bytecode."""


class MagicClass:
    """MagicClass class with the same behavior as the provided bytecode."""

    def __init__(self, radius=0):
        """Initializes a new instance of the MagicClass class."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Computes the area of the circle."""
        return (self.__radius ** 2 * 3.141592653589793)

    def circumference(self):
        """Computes the circumference of the circle."""
        return (2 * 3.141592653589793 * self.__radius"
