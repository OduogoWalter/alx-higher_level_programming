#!/usr/bin/python3
"""
Module: 2-matrix_divided

This module defines a function matrix_divided
that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The matrix containing integers or floats.
        div (int or float): The number to divide the elements of the matrix by.

    Returns:
        list of lists: A new matrix with elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    num_columns = len(matrix[0])
    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != num_columns:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row]
                  for row in matrix]
    return (new_matrix)
