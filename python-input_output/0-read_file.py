#!/usr/bin/python3
"""
Contain a function for read and display in stdout
"""


def read_file(filename=""):
    """
    Read and display on stdout

    Args:
        filename (str): The destination fo file you need read. Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
