#!/usr/bin/python3
import json
"""
Contains a function to save a python object to a file as a JSON string
"""


def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a file using a JSON representation

    Args:
        my_obj (object): Object to save
        filename (str): Name of the file
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
