#!/usr/bin/python3
"""
Module: 5-text_indentation

This module defines a function text_indentation that prints a text with 2 new lines
after each occurrence of the characters '.', '?', and ':'.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':'.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    new_text = ''

    for char in text:
        new_text += char
        if char in special_chars:
            new_text += '\n\n'

    lines = new_text.split('\n')
    for line in lines:
        print(line.strip())  # Remove leading and trailing whitespace

if __name__ == "__main__":
    text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
    Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
    Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
    Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
    rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
    stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
    cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
    beatiorem! Iam ruinas videres"""
    text_indentation(text)
