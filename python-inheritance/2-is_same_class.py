#!/usr/bin/python3
"""
A function to check if the object belongs to the class
"""


def is_same_class(obj, a_class):
    """
    Receive a object and a class for check if object belongs to the class

    Args:
        obj (object): An object receive to compare
        a_class (class): a class for comparaison

    Returns:
        boolean: Return True if the object is an instance of the class or False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
