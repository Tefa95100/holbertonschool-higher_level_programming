#!/usr/bin/python3
"""
1-rectangle.py

This module contain one class Rectangle
"""


class Rectangle:
    """
    Class for create Rectangle object
    """

    def __init__(self, width=0, height=0):
        """
        The function for init the dimensions of rectangle

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If value is not an integer
            ValueError: If the value less of 0
            TypeError: If value is not an integer
            ValueError: If the value less of 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
        Retrieve the width of rectangle

        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieve the height of rectangle

        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle

        Args:
            width (int): The width of the rectangle. Defaults to 0.

        Raises:
            TypeError: If value is not an integer
            ValueError: If the value less of 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle

        Args:
            height (int): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If value is not an integer
            ValueError: If the value less of 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.getter
    def width(self):
        """
        Get the width of the rectangle

        Returns:
            width: return the width of the rectangle
        """
        return self.__width

    @height.getter
    def height(self):
        """
        Get the height of the rectangle

        Returns:
            height: return the height of the rectangle
        """
        return self.__height
