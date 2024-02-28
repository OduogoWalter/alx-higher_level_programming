#!/usr/bin/python3
"""Module for the Base class."""

import json


class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance with an optional id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation
        of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_str = cls.to_json_string([obj.to_dictionary()
                                           for obj in list_objs])
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries represented by json_string."""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            return None
        dummy_instance.update(**dictionary)
        return (dummy_instance)

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from the file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_str = file.read()
                dictionaries = cls.from_json_string(json_str)
                instances = [cls.create(**dictionary)
                             for dictionary in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        # Create a turtle screen
        screen = turtle.Screen()

        # Loop through rectangles and draw them
        for rectangle in list_rectangles:
            # Create a turtle object for the rectangle
            rect_turtle = turtle.Turtle()
            rect_turtle.penup()  # Lift the pen to avoid drawing lines
            rect_turtle.goto(rectangle.x, rectangle.y)  # Move to starting position
            rect_turtle.pendown()  # Put the pen down to start drawing
            for _ in range(2):  # Draw the rectangle
                rect_turtle.forward(rectangle.width)
                rect_turtle.right(90)
                rect_turtle.forward(rectangle.height)
                rect_turtle.right(90)
            rect_turtle.hideturtle()  # Hide the turtle after drawing the rectangle

        # Loop through squares and draw them
        for square in list_squares:
            # Create a turtle object for the square
            square_turtle = turtle.Turtle()
            square_turtle.penup()  # Lift the pen to avoid drawing lines
            square_turtle.goto(square.x, square.y)  # Move to starting position
            square_turtle.pendown()  # Put the pen down to start drawing
            for _ in range(4):  # Draw the square
                square_turtle.forward(square.size)
                square_turtle.right(90)
            square_turtle.hideturtle()  # Hide the turtle after drawing the square

        # Keep the window open until it is manually closed
        screen.mainloop()
