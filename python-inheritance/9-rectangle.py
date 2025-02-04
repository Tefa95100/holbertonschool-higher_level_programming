#!/usr/bin/python3
"""
Contain a class Rectangle
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle inherit of BaseGeometry

    Args:
        BaseGeometry (class): class herited
    """
    def __init__(self, width, height):
        """
        Initialize the parameters when you create the object

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        print("{}, {}".format(width, height))
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height

    def __str__(self):
        """
        Methods to print the rectangle

        Returns:
            str: return the method to print the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Function to calculate the area of rectangle

        Returns:
            int: The area of rectangle is width multiplied by height
        """
        return self.__width * self.__height
