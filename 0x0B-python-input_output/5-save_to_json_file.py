#!/usr/bin/python3
"""
Function that defines JSON file writing.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that defines JSON file writing.
    Args:
        my_obj (str): string object.
        filename (str): name of the JSON file.
    Returns:
        str: JSON text file output.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
