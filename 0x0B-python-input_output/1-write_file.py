#!/usr/bin/python3
""" Write File writing function."""


def write_file(filename="", text=""):
    """
    Write a string to a UTF-8 file.
    Args:
        filename (str): name of file to be written.
        text (str): text to be written in the file.
    Returns:
        str: written string.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
