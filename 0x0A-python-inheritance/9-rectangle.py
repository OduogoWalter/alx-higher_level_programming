#!/usr/bin/python3
"""Module containing a rectangle class"""

class BaseGeometry:
    """A class with area and integer_validator methods"""
    
    def area(self):
        """Raises an exception with the message 'area() is not implemented'"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates the value parameter"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        
        
class Rectangle(BaseGeometry):
    """A class representing a rectangle"""
    
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        
    def area(self):
        """Compute the area of the rectangle"""
        return (self.__width * self.__height)
    
    def __str__(self):
        """Return a srting representation of the rectangle"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))