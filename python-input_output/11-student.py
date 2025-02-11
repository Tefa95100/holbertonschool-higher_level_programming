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

    def to_json(self, attrs=None):
        """
        Return a dictionary of instance student

        Returns:
            dict: Dictionary of attribute of this instance
        """

        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Set attributes from a JSON

        Args:
            json (dict): Dictionary for set attributes
        """
        for key in json:
            setattr(self, key, json[key])
