#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """Returns a new matrix with each value squared using map."""
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
