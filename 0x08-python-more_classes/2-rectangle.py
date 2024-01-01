#!/usr/bin/python3
"""Module defining a Rectangle class"""


class Rectangle:
    """Rectangle class with private width and height attributes"""

    @property
    def width(self):
        """Getter method for width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return (self.__heigt)

    @height.setter
    def height(self, value):
        """Setter method forb height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __init__(self, width=0, height=0):
        """Initialization method with optional width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Method to calculate and return the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Method to calculate and return the rectangle perimeter"""
        return (0 if self.width == 0 or
                self.height == 0 else 2 * (self.width + self.height))
