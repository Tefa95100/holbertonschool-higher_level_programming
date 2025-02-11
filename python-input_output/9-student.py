#!/usr/bin/python3
"""
Contains a class Students
"""


class Student:
    """
    Create and initialize a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize students

        Args:
            first_name (str): First name of student
            last_name (str): Last name of student
            age (int): Age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Return a dictionary of instance student

        Returns:
            dict: Dictionary of attribute of this instance
        """
        return self.__dict__
