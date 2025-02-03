#!/usr/bin/python3
"""
Contain a subclass to inheriths from list who print in ascending sort
"""


class MyList(list):
    """
    Subclass to inherit from list

    Args:
        list (object): object which is inherited by MyList
    """
    def print_sorted(self):
        """
        print a list sorted
        """
        print(sorted(self))
