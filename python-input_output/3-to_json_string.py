#!/usr/bin/python3
from json import dumps
"""
Contain a function for serializing an object to a JSON
"""


def to_json_string(my_obj):
    """
    Serialized an object to a JSON

    Args:
        my_obj (object): The object to serialize

    Returns:
        str: The JSON-formatted string representation of the object.
    """
    return dumps(my_obj)
