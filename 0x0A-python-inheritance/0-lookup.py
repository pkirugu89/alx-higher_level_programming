#!/usr/bin/python3
"""Method that lookup an object."""


def lookup(obj):
    """
    Method that returns a list of avaliable
    attributes & methods of an object.
    Args:
        obj: The object to be checked.

    Returns:
        List of attribute and method names.
    """
    return dir(obj)
