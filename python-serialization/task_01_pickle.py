#!/usr/bin/python3
"""
Contains a class custom object
"""
import pickle


class CustomObject:
    """
    A custome object for learn serialization
    """
    def __init__(self, name, age, is_student):
        """
        Initialize an instance

        Args:
            name (str): name of student
            age (int): age of student
            is_student (bool): Say if is a student or others
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """
        Serialize an instance with pickle

        Args:
            filename (str): path of file for save

        Returns:
            exception: return exception
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self.__dict__, file)
        except Exception:
            return None

    def display(self):
        """
        Display information of student
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    @classmethod
    def deserialize(cls, filename):
        """
        Initialize a student after load from a file

        Args:
            filename (str): path of file

        Returns:
            exception: return an exception if fail
        """
        try:
            with open(filename, "rb") as file:
                dict = pickle.load(file)
                return cls(dict["name"], dict["age"], dict["is_student"])
        except Exception:
            return None
