#!/usr/bin/python3
"""
Function that defines class to JSON.
"""


def class_to_json(obj):
    """
    Function that converts class objects to JSON.
    Args:
        obj: param to be converted.
    Returns:
        dict of a simple structure.
    """
    return obj.__dict__
