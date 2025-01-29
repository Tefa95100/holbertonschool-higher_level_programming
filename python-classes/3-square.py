#!/usr/bin/python3
"""
1-square.py

This module contain one class Square
"""


class Square:
    """
    Class square define a square by size

    Args:
        size (int): the size of square

    Raises:
        TypeError: if size is not an integer
        TypeError: if size is less than 0
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calcule and return the area of the square.

        Returns:
            int: The area of square
        """
        return self.__size ** 2
