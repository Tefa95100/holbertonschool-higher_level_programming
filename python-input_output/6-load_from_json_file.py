#!/usr/bin/python3
"""
Contains a function to load a object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Loads a python object frome a JSON file

    Args:
        filename (str): Name of the file to read from

    Returns:
        object: The python data structure
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
