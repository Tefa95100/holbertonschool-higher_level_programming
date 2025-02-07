#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi
"""
Contains class and function for use methods
"""


class Shape(ABC):
    """
    Contain abstract method
    """
    @abstractmethod
    def area():
        """
        abstract method for area
        """
        pass

    @abstractmethod
    def perimeter():
        """
        abstract method for perimeter
        """
        pass


class Circle(Shape):
    """
    Class for create a circle with method for recuperate info
    """
    def __init__(self, radius):
        """
        Initialize the circle

        Args:
            radius (int): the radius of circle
        """
        if radius < 0:
            self.radius = 0
        else:
            self.radius = radius

    def area(self):
        """
        Calculate the area of circle

        Returns:
            int: return the area of circle
        """
        return (self.radius ** 2) * pi

    def perimeter(self):
        """
        Calculate the perimeter of circle

        Returns:
            int: return the perimer of circle
        """
        return (self.radius * 2) * pi


class Rectangle(Shape):
    """
    Class for create a rectangle with method for recuperate info
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of rectangle

        Returns:
            int: return the area of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of rectangle

        Returns:
            int: return the perimer of rectangle
        """
        return (self.width + self.height) * 2


def shape_info(object):
    """
    Print the are and the perimeter of the object receive

    Args:
        object (object): object for recuperate the area and perimeter
    """
    print(f"Area: {object.area()}")
    print(f"Perimeter: {object.perimeter()}")
