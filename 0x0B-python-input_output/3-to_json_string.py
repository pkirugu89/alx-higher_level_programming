#!/usr/bin/python3
"""Function that converts string to JSON."""
import json


def to_json_string(my_obj):
    """
    Returns a JSON format of the string param.
    Args:
        my_obj (str): string to be converted.
    Returns:
        str: JSON format of the string object.
    """
    return json.dumps(my_obj)
