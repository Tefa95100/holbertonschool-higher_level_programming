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
        self.__size = size
