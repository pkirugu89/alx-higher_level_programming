#!/usr/bin/python3
"""
Method that returns a class instance.
"""


def is_same_class(obj, a_class):
    """
    Method that returns True if the object is exactly a class instance;
    therwise False
    Args:
        obj: The object to check.
        a_class: Class to compare.

    Returns:
        True if obj is a class instance of a_class, False otherwise.
    """
    return type(obj) == a_class
