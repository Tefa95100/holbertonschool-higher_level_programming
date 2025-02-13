#!/usr/bin/python3
"""
Contains function for treat JSON
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Save data in a file on format JSON

    Args:
        data (dict): A dictionary for save
        filename (_type_): _description_
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load a JSON format in a object python

    Args:
        filename (str): path of file to load

    Returns:
        obj: return an obj after load
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
