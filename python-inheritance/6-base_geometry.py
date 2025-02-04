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
        """Raise an exception

        Raises:
            Exception: Raise when the function area is call
        """
        raise Exception('area() is not implemented')
