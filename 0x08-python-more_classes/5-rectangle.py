#!/usr/bin/python3
"""Module defining a rectangle class"""


class Rectangle:
    """Rectangle class with private width and height attributes"""

    def __init__(self, width=0, height=0):
        """Initialization method with optional width and height"""
        self.width = width
        self.height = height

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
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Method to calculate and return the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Method to calculate and return the rectangle perimeter"""
        return (0 if self.__width == 0 or
                self.__height == 0 else 2 * (self.__width + self.__height))

    def __str__(self):
        """Method to create a string representaion of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        return ("\n".join(["#" * self.__width] * self.__height))

    def __repr__(self):
        """Method to create representation of the rectagle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Method to print message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
