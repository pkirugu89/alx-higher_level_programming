#!/usr/bin/python3
"""Method that returns the instance of
    a_class or it's subclass."""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or \
            if the object is an instance of a class
    that inherited from, the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or \
                a subclass of a_class; False otherwise.
    """
    return isinstance(obj, a_class)
