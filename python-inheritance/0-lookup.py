#!/usr/bin/python3
"""
Contain a function lookup for list all methods and attributes in a object
"""


def lookup(obj):
    """_summary_

    Args:
        obj (object): An object for list all methods and attr

    Returns:
        list: Return a list with all methods and attributes
    """
    return dir(obj)
