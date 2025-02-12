#!/usr/bin/python3
"""
Contain a function for serializing an object to a JSON
"""
from json import dumps


def to_json_string(my_obj):
    """
    Serialized an object to a JSON

    Args:
        my_obj (object): The object to serialize

    Returns:
        str: The JSON-formatted string representation of the object.
    """
    return dumps(my_obj)
