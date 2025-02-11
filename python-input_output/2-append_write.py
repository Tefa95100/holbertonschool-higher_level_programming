#!/usr/bin/python3
"""
Contain a function for append text in a file
"""


def append_write(filename="", text=""):
    """
    Append a text to a file

    Args:
        filename (str): Path to the file. Defaults to "".
        text (str): Text to append. Defaults to "".

    Returns:
        int: Return the number of character write.
    """
    with open(filename, "a", encoding="utf-8") as file:
        char_wri = file.write(text)
        return char_wri
