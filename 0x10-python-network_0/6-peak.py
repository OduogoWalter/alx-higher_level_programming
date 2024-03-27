#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.
    A peak is defined as an element that is equal to
    or greater than its neighbors.
    This implementation uses a binary search approach to find a peak with
    O(log n) complexity, ensuring efficient handling of large data sets.

    Args:
        list_of_integers: List of integers to search through.

    Returns:
        An integer value representing a peak, or None if the list is empty.
    """
    if not list_of_integers:
        return (None)

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return (list_of_integers[low])
