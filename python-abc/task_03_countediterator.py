#!/usr/bin/python3
"""
Contain a class for iterate a collections
"""


class CountedIterator:
    """
    Class for count and iterate a collection
    """
    def __init__(self, iterable):
        """
        Initialize the componment of instance

        Args:
            iterable (collection): a collection to iterate
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """
        methods for going to next iteration

        Returns:
            item: return the actual item
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """
        get and return the counter

        Returns:
            int: return a counter of the collection
        """
        return self.counter
