#!/usr/bin/python3
"""
Contain a class Square
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Class Square inherit of Rectangle

    Args:
        Rectangle (class): class herited
    """
    def __init__(self, size):
        """
        initialize the square

        Args:
            size (int): call super for initialize the square
        """
        if self.integer_validator("size", size):
            super().__init__(size, size)

    def __str__(self):
        """
        Methods to print the rectangle

        Returns:
            str: return the method to print the rectangle
        """
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height)

    def area(self):
        """
        call super for the area function

        Returns:
            int: the area of square
        """
        return super().area()
