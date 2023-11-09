#!/usr/bin/python3
"""
Function that defines file appending.
"""


def append_write(filename="", text=""):
    """
    Function that appends a string to UTF-8 file.
    Args:
        filename (str): File to be the appended.
        text (str): string appended into the file.
    Return:
        str: The string appended in the filename.
    """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
