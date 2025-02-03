#!/usr/bin/python3
"""
Contain a function to check if the object belongs to a class or
 a class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of class or a class that inherited from

    Args:
        obj (object): An object receive to compare
        a_class (class): a class for comparaison

    Returns:
        boolean: Return True if the object is an instance of the class or an
         instance of a class that inherited from else return False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
