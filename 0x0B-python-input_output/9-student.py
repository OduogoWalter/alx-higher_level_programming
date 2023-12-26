#!usr/bin/python3
"""Module to define a Student class."""


class Student:
    """Student class with attributes first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first_name,
        last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a Student instance."""
        return {
            'first_name': self.fisrt_name,
            'last_name': self.age
        }


if __name__ == "__main__":
    pass
