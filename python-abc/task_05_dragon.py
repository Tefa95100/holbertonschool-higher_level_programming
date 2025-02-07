#!/usr/bin/python3
"""
Contain a classe SwimMixin, FlyMixin and
 Dragon who inherited from SwimMixin and FlyMixin
"""


class SwimMixin:
    """
    Create a creature SwimMixin
    """
    def swim(self):
        """
        Shows the means of travel
        """
        print("The creature swims!")


class FlyMixin:
    """
    Create a creature FlyMixin
    """

    def fly(self):
        """
        Shows the means of travel
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Create a Dragon who inherited from SwimMixin and FlyMixin

    Args:
        SwimMixin (class): Legacy fact at SwimMixin
        FlyMixin (class): Legacy fact at FlyMixin
    """
    def swim(self):
        """
        Shows the means of travel
        """
        print("The creature swims!")

    def fly(self):
        """
        Shows the means of travel
        """
        print("The creature flies!")

    def roar(self):
        """
        Shows the roar of Dragon
        """
        print("The dragon roars!")
