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
        if self.integer_validator(width, width):
            self.__width = width
        if self.integer_validator(height, height):
            self.__height = height
