#!/usr/bin/python3
"""
5-rectangle.py

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

    def __str__(self):
        """
        Methods to print the rectangle

        Returns:
            str: return the method to print the rectangle
        """
        return "\n".join("#" * self.__width for index in range(self.__height))

    def __repr__(self):
        """
        Methods to represent the class

        Returns:
            str: str to represent the class
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Print a message when you delete the object
        """
        print("Bye rectangle...")

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
            ValueError: If the value less than 0
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
            ValueError: If the value less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Function to calculate the area of rectangle

        Returns:
            int: The area of rectangle is width multiplied by height
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Function to calculate the perimeter of rectangle

        Returns:
            int: The perimeter of rectangle is return after add width with
            height and multiplicate result by two
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
