#!/usr/bin/python3
"""
Contains an abstract class and 2 subclass
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class with method for herited
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method for force creation in subclass
        """
        pass


class Dog(Animal):
    """
    Class with one method
    """
    def sound(self):
        """
        methods for give the sound of animal

        Returns:
            string: the sound of a dog
        """
        return "Bark"


class Cat(Animal):
    """
    Class with one method
    """
    def sound(self):
        """
        methods for give the sound of animal

        Returns:
            string: the sound of a cat
        """
        return "Meow"
