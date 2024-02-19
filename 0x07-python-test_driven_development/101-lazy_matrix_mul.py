#!/usr/bin/python3
"""
Module: 101-lazy_matrix_mul

This module defines a function lazy_matrix_mul that multiplies two matrices using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        numpy.ndarray: The result of the matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, or if m_a or m_b is not a list of lists,
                   or if any element in the matrices is not an integer or float,
                   or if the matrices are not rectangular, or if the matrices cannot be multiplied.

    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row) or \
       not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.dot(m_a, m_b)


if __name__ == "__main__":
    m_a = [[1, 2], [3, 4]]
    m_b = [[1, 2], [3, 4]]
    print(lazy_matrix_mul(m_a, m_b))
