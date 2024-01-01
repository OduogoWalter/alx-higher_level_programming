#!/usr/bin/python3
"""Module defining a Rectangle class"""


class Rectangle:
    """Rectangle class with private width and height attributes"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization method with optional width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Method to create a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        return ("\n".join([str(self.print_symbol) *
                           self.__width] * self.__height))

    def __repr__(self):
        """Method to create a representation of the rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Method to print message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to compare rectangles based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        return (rect_1 if area_1 >= area_2 else rect_2)

    @classmethod
    def square(cls, size=0):
        """Class method to create a square Rectangle instance"""
        return (cls(size, size))
