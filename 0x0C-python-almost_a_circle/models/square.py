#!/usr/bin/python3
"""Module for the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter for size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the square."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, val in zip(attrs, args):
                setattr(self, attr, val)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
