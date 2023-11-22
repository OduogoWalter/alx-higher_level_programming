#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Square class with private size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new instance of the Square class."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Setter method to retrieve the value of size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method to set the value of size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer.""")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the value of position."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter method to set the value of position with validation."""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Computes the area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
