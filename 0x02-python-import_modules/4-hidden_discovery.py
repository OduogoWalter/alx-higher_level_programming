#!/usr/bin/python3
import marshal


def print_names():
    code = None
    with open("hidden_4.pyc", "rb") as file:
        code = marshal.load(file)

        names = [name for name in code.co_names oif not name.startswith('__')]
        names, sort()

        for name in names:
            print(name)


if __name__ == "__main__":
    print_names()
