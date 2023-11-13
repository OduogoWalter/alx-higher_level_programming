#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Use list comprehension to create a new list with True or False
    # depending on whether the integer is a multiple of 2
    result_list = [num % 2 == 0 for num in my_list]


if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_result = divisible_by_2(my_list)

    i = 0
    while i < len(list_result):
        print("{:d} {:s} divisible by 2".format(
            my_list[i], "is" if list_result[i] else "is not"))
        i += 1
