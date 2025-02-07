#!/usr/bin/python3


def add_attribute(obj, name_value, value):
    """
    Function for add an attribute to a class

    Args:
        obj (class): it's for check if is a class
        name_value (string): the name for stock the new attribute
        value (): the value of new attribute

    Raises:
        TypeError: if obj is not a object of a class you can't add attribute
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name_value, value)
    else:
        raise TypeError("can't add new attribute")
