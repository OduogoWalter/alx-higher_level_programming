#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Square class with a private size attribute."""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class."""
        if ot isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Computes the area of the square."""
        return self.__size ** 2
