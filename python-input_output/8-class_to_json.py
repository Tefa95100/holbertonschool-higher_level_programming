#!/usr/bin/python3
import json
"""
Contains a function for return a JSON
"""


def class_to_json(obj):
    """
    Returns a dictionnary of attributes from an object in JSON
     compatibles format

    Args:
        obj (object): The object from wich to extract attributes

    Returns:
        dict: A dictionary of attributes in JSON format
    """
    return json.dumps(obj.__dict__)
