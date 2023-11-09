#!/usr/bin/python3
"""
Function that converts string to json.
"""
import json


def to_json_string(my_obj):
    """
    Method that returns a JSON format of str param.
    Args:
        my_obj (str): string to be converted.
    Returns:
        str: JSON format of string object.
    """
    return json.dumps(my_obj)
