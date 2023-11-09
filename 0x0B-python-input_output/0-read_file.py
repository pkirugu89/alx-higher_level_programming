#!/usr/bin/python3
"""
Read file method.
"""


def read_file(filename=""):
    """
    Function that reads a textfile and prints it.
    """
    with open(filename, encoding="UTF-8") as f:
        text = f.read()
        print(text, end="")
