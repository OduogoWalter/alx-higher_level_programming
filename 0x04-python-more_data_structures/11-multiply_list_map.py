#!/usr/bin/python3

def multuiply_list_map(my_list=[], number=0):
    """Returns a new list with values multiplied by a number."""
    return list(map(lambda x: x * number, my_list))
