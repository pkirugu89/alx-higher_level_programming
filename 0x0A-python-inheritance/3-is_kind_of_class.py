#!/usr/bin/python3
"""
Method that returns the instance of
a_class or it's subclass.
"""


def is_kind_of_class(obj, a_class):
    """
    Method that returns True when the instance of a class that \
            is inherited from, otherwise False.
    Args:
        obj: object to be checked.
        a_class: class to compare against.
    Returns:
        True if obj is an instance of a_class or \
                a subclass of a_class; False otherwise.
    """
    return isinstance(obj, a_class)
