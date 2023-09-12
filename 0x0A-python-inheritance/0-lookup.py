#!/usr/bin/python3
"""Method that look up object."""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of attribute and method names.
    """
    return dir(obj)
