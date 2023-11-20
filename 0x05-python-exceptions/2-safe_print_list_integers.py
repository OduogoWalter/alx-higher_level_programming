#!usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if type(my_list[i], end=""):
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except TypeError:
        pass
    finally:
        print()
        if count == x:
            raise IndexError("list index out of range")
        return (count)
