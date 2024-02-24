#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers.
    :param my_list: list of elements
    :param x: number of elements to access in my_list
    :return: the real number of integers printed
    """
    printed_integers = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                printed_integers += 1
    except (IndexError, TypeError):
        pass
    else:
        print()
    finally:
        return (printed_integers)

