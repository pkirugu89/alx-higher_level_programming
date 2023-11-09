#!/usr/bin/python3
"""
Function that defines JSON file reading.
"""
import json


def load_from_json_file(filename):
    """
    Function that define JSON file reading.
    Args:
        filename (str): file to be read.
    Returns:
        file been read by JSON.
    """
    with open(filename) as f:
        return json.load(f)
