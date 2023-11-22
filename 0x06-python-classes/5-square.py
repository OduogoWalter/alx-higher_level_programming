#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Square class with private size attribute."""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class."""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the value of size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the value of the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Computes the area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square using the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
