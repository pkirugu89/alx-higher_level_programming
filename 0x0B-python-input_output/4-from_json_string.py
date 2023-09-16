#!/usr/bin/python3
"""Function that converts JSON to string object."""
import json


def from_json_string(my_str):
    """
    Function that converts JSON to string.
    Args:
        my_str (str): JSON file to be converted.
    Returns:
        str: returns python version of a JSON string.
    """
    return json.loads(my_str)
