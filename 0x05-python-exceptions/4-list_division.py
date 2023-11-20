#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, TypeError):
            if isinstance(my_list_1[i], (int, float)) and \
                    isinstance(my_list_2[i], (int, float)):
                print("wrong type")
            elif isinstance(my_list_2[i], int) and my_list_2[i] == 0:
                print("division by 0")
            else:
                print("out of range")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            result_list.append(result)

    return result_list
