#!/usr/bin/python3
"""
Contain a function for check if the object is a class inherited
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class inherited

    Args:
        obj (object): An object receive to compare
        a_class (class): a class for comparaison

    Returns:
        Boolean: Return True only if the object is inherited of the class
          else return False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
