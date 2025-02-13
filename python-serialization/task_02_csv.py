#!/usr/bin/python3
"""
Contains a function who convert a CSV in to JSON
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Convert a CSV in to JSON

    Args:
        filename (string): Path of file CSV

    Returns:
        boolean: Return True if success or False if the file don't existed
    """
    data = []
    try:
        with open(filename, "r", encoding="utf-8") as csvfile:
            dict_read = csv.DictReader(csvfile)
            for word in dict_read:
                data.append(word)
        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)
        return True
    except FileNotFoundError:
        return False
