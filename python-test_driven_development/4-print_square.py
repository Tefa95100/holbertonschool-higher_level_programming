#!/usr/bin/python3
"""
4-print_square.py

module contains a function for print a square
"""


def print_square(size):
    """
    This function print a square of the size of value receive

    Parameter:
    size: the size of square

    Return:
    return nothing
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")
    for index_row in range(size):
        for index in range(size):
            print("#", end='')
        print()
