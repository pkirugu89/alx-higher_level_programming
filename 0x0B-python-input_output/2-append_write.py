#!/usr/bin/python3
"""Function that defines file appending."""


def append_write(filename="", text=""):
    """
    Function that appends a string to a UTF-8 file.
    Args:
        filename (str): The filename to be appended.
        text (str): string to be appended into the filename.
    Returns:
        str: The string appended in the filename.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
