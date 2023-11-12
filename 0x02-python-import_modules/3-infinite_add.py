#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    # Remove the script name from arguments
    args = argv[1:]

    # Calculate the sum of all arguments
    result = sum(int(arg) for arg in args)

    # Print the result followed by a new line
    print(result)
