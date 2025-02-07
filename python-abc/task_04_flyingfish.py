#!/usr/bin/python3
"""
Contain three class Fish, Bird and
 FlyingFish who inherited from Fish and Bird
"""


class Fish:
    """
    Create a Fish
    """

    def swim(self):
        """
        Shows the means of travel
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Shows the habitat
        """
        print("The fish lives in water")


class Bird:
    """
    Create a Bird
    """

    def fly(self):
        """
        Shows the means of travel
        """
        print("The bird is flying")

    def habitat(self):
        """
        Shows the habitat
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Create a FlyingFish who inherited from Fish and Bird

    Args:
        Fish (class): Legacy fact at FlyingFish
        Bird (class): Legacy fact at FlyingFish
    """

    def fly(self):
        """
        Shows the means of travel
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Shows the means of travel
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Shows the habitat
        """
        print("The flying fish lives both in water and the sky!")
