#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for index_row in matrix:
        for element in index_row:
            if isinstance(element, int):
                print("{}".format(element), end=" ")
        print()
