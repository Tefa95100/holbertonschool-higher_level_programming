#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    new_matrix_row = []
    for index_row in matrix:
        for element in index_row:
            if isinstance(element, int):
                new_element = element ** 2
                new_matrix_row.append(new_element)
            else:
                continue
        new_matrix.append(new_matrix_row.copy())
        new_matrix_row.clear()
    return new_matrix
