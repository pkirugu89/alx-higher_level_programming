#!/usr/bin/python3
def read_file(filename=""):
    """Function that reads a textfile and prints it."""

    with open(filename) as f:
        text = f.read()
        print(text, end="")
