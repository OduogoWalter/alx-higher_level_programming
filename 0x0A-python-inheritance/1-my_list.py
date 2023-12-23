#!/usr/bin/python3
"""Module with class MyList"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
