#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.

    Args:
        my_list (list): The input list.
        idx (int): The index of the item to be deleted.

    Returns:
        list: The modified list.
    """
    # Check if the index is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return (my_list)

    # Iterate through the list and remove the item at the specific index
    for i in range(len(my_list)):
        if i == idx:
            del my_list[i]
            break

    return (my_list)
