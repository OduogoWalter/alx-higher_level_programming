#!/usr/bin/python3

class MyList(list):
    """
    A class that inherits from list and provides additional functionality.
    """

    def print_sorted(self):
        """
        Print the list sorted in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
