#!/usr/bin/python3
"""
0-add_integer.py

This modul contain a function for add 2 numbers
"""


def add_integer(a, b=98):
    """
    Add two numbers and return result

    Parameters:
    a: the first number
    b: the second number

    Return:
    return the sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
