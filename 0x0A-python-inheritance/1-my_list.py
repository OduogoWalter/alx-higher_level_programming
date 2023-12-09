#!/usr/bin/python3
"""
Module containing the MyList class.
"""


class MyList(list):
    """
    A class that inherits from the built-in list class.
    """


    def print_sorted(self):
        """
        Print the list in ascending order.
        """
        print(sorted(self))
