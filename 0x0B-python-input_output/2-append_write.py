#!/usr/bin/python3
"""Module to append a string to the end of
a text file and return the number of characters added."""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file and return
    the number of characters added.

    Args:
        filename (str): The name of the text file.
        text (str): The string to be appended to the file.


    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return (file.write(text))


if __name__ == "__main__":
    nb_characters_added = append_write("file_append.txt",
                                       "This School is so cool!\n")
    print(nb_characters_added)
