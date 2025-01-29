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
        self.size = size

    def area(self):
        """
        Return:
            return the area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print a square base on the size
        """
        if self.size == 0:
            print()
        else:
            for index in range(self.size):
                for index_row in range(self.size):
                    print("#", end='')
                print()

    @property
    def size(self):
        """
        Retrieve the size of square

        Returns:
            return the size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of square

        Args:
            size (int): the size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @size.getter
    def size(self):
        """
        Get the size of square

        Returns:
            return the size
        """
        return self.__size
