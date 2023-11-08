#!/usr/bin/python3
output = ""
for char in range(ord('a'), ord('z') + 1):
    if chr(char) not in 'qe':
        output += "{}".format(chr(char))
print("{}".format(output), end="")
