#!/usr/bin/python3
"""
2-matrix_divided.py

module with one function for divided the different element on a matrix
"""


def matrix_divided(matrix, div):
    """
    Take the different element on a list and divided by a number.
    The function check if the element is an integer or a float and if
    all line on the matrice as the same lenght

    Parameters:
    matrix: the matrix with the element to divided
    div: the divisor

    Return:
    return a new list with contain all the new element if the element
    is a float he's has two number
    """
    len_row = len(matrix[0])
    new_row = []
    new_matrix = []

    for matrix_row in matrix:
        if len(matrix_row) != len_row:
            raise TypeError("Each row of the matrix must have the same size")
        for element in matrix_row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a\
 matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for matrix_row in matrix:
        for element in matrix_row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row.copy())
        new_row.clear()

    return new_matrix
