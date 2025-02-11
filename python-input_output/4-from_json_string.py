#!/usr/bin/python3
import json
"""
Contains a function for deserializing a JSON to an object
"""


def from_json_string(my_str):
    """
    Deserialize a JSON to an object

    Args:
        my_str (str): JSON formated string

    Returns:
        object: Corresponding python data structure
    """
    return json.loads(my_str)
