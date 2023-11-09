#!/usr/bin/python3
"""
Write to file function.
"""


def write_file(filename="", text=""):
    """
    Method that writes a string to a UTF-8 file.
    Args:
        filename (str): file name to be written.
        text (str): text to be written in the file.
    Returns:
        str: written string.
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
