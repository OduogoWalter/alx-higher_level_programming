#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit


# Test case
print_last_digit(98)
print_last_digit(0)
result = print_last_digit(-1024)
print(result)
