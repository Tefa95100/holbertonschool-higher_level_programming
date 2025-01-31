#!/usr/bin/python3
"""
6-square.py

This module contain one class Square
"""


class Square:
    """
    Class Square contain a function to init attribute of object

    Args:
        size (int): the size of square
        position (tuple): define the position of square
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for element in position:
            if not isinstance(element, int):
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            if element < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """
        Return:
            return the area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print a square based on the size and the position
        """
        if self.size == 0:
            print()
        else:
            if self.position[1] > 0:
                for index in range(self.position[1]):
                    print()

            for index in range(self.size):
                for index in range(self.position[0]):
                    print(" ", end="")
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

    @property
    def position(self):
        """
        Retrieve the position of square

        Returns:
            return the position of square
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        Set the position of square

        Args:
            position (tuple): the position of square
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) > 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for element in value:
            if not isinstance(element, int):
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            if element < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        self.__position = value
