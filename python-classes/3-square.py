#!/usr/bin/python3
"""
1-square.py

This module contain one class Square
"""


class Square:
    """
    Class Square contain a function to init attribute of object

    Args:
    size (int): the size of square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Return: return the area of square
        """
        return self.size ** 2
