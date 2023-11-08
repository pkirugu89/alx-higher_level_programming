#!/usr/bin/python3
""" Class that defines MyList. """


class MyList(list):
    """ Class that defines MyList."""
    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        """

        sorted_list = sorted(self)
        print(sorted_list)
