#!/usr/bin/python3
"""
5-text_indentation.py

This module contain a function for print string
"""


def text_indentation(text):
    """
    This function print a string and add 2 new line after .?:

    Parameters:
    text: the string for print

    Return:
    return nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        print(char, end='')
        if char in [".", "?", ":"]:
            print()
            print()
