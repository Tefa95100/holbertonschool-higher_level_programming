#!/usr/bin/python3
"""
Contain a function for write a text in a file
"""


def write_file(filename="", text=""):
    """
    Write a text in a file and create the file if doesn't exist

    Args:
        filename (str): path of the file to write. Defaults to "".
        text (str): The text to write in the file. Defaults to "".

    Returns:
        int: The number of char write.
    """
    with open(filename, "w", encoding="utf-8") as file:
        char_wri = file.write(text)
        return char_wri
