#!/usr/bin/python3
"""
Contain a class who inherit from class int
"""


class MyInt(int):
    """
    Class for modify the comportment of an int

    Args:
        int (class): class herited
    """

    def __init__(self, value):
        """
        Initialize the class

        Args:
            value (int): an int
        """
        self.value = value

    def __eq__(self, value):
        """
        Methods use when your search an equal

        Args:
            value (int): int receive for comparaison

        Returns:
            boolean: return false if the comparaison is equal
        """
        if self.value == value:
            return False

    def __ne__(self, value):
        """
        Methods use when your search a difference

        Args:
            value (int): int receive for comparaison

        Returns:
            boolean: return true if the comparaison is different
        """
        if self.value == value:
            return True
