#!/usr/bin/python3
""" method that add 2 integers
    Args:
    a (int): first parameter.
    b (int): second parameter.
"""


def add_integer(a, b=98):
    """
    Functions that adds 2 integers.
    Args:
    a (int): first parameter.
    b (int): second paramater set to 98
    Returns:
    int: sum of two integers.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return (a + b)
