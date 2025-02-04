#!/usr/bin/python3
"""
Contain a empty class BaseGeometry
"""


class BaseGeometry:
    """
    Contain a function who raise an exception
    """
    def __init__(self):
        """
        Empty init
        """
        pass

    def area(self):
        """
        Raise an exception

        Raises:
            Exception: Raise when the function area is call
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Raise exception for error integer

        Args:
            name (string): name of variable
            value (): value to check if is an int

        Raises:
            TypeError: if value is not an int
            ValueError: if value is equal or less to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
