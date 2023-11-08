#!/usr/bin/python3
"""
Inherit from method.
"""


def inherits_from(obj, a_class):
    """
    Method that returns True if the class instance \
            that inherited (directly/ indirectly)
    from the base class; otherwise False.

    Args:
        obj: object to check.
        a_class: class to compare against.

    Returns:
        True: obj is an instance of subclass of a_class.\
                False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
