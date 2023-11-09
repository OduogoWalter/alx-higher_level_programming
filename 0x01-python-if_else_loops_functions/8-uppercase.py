#!/usr/bin/python3
def uppercase(s):
    result = ""
    for c in s:
        if 'a' <= c <= 'z':
            result += "{}".format(chr(ord(c) - 32))
        else:
            result += "{}".format(c)
    print(result)


# Example of use
uppercase("best")
uppercase("Best School 98 Battery street")
