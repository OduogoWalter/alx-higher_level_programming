#!/usr/bin/python3
output = ""
for char in range(ord('a'), ord('z') + 1):
    output += "{}".format(chr(char))
print(output, end="")
