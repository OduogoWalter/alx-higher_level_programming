#!/usr/bin/python3
"""Module containing a Rectangle class"""


# Import the BaseGeometry class from the current module
from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """A class representing a rectangle"""

    def __init__(self, width, height):
        """Initialize the rectangle instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
