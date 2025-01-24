#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for index_row in matrix:
        line = " ".join("{:d}".format(element) for element in index_row)
        print("{}".format(line))
