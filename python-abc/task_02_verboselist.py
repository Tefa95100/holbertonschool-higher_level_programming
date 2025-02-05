#!/usr/bin/python3
"""
Contains one class who herited of list
"""


class VerboseList(list):
    """
    Class who print a string after different methods
    """

    def append(self, object):
        """
        Print a string before return methods append

        Args:
            object (list): object to add to the list

        Returns:
            list: return to the methods herited after print
        """
        print(f"Added [{object}] to the list.")
        return super().append(object)

    def extend(self, iterable):
        """
        Print a string before return methods extend

        Args:
            iterable (list): iterable use for extend list

        Returns:
            list: return to the methods herited after print
        """
        print(f"Extended the list with [{len(iterable)}] items.")
        return super().extend(iterable)

    def remove(self, value):
        """
        Print a string before return methods remove

        Args:
            value (list): value search for remove to the list

        Returns:
            list: return to the methods herited after print
        """
        print(f"Removed [{value}] from the list.")
        return super().remove(value)

    def pop(self, index=-1):
        """
        Print a string before return methods pop

        Args:
            index (list): pop the object to the index or the last

        Returns:
            list: return to the methods herited after print
        """
        print(f"Popped [{self[index]}] from the list.")
        return super().pop(index)
