#!/usr/bin/python3
def uppercase(s):
    for c in s:
        if 'a' <= c <= 'z':
            print("{}".format(chr(ord(c) - 32)), end='')
        else:
            print("{}".format(c), end='')
    print()


# Example of use
uppercase("best")
uppercase("Best School 98 Battery street")
