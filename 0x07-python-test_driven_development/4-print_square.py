#!/usr/bin/python3
""" Print Square Method. """


def print_square(size):
    """ Print Square method."""
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    # Check if size is non-negative
    if size < 0:
        raise ValueError("size must be >= 0")
    # Check if size is a float and is less than 0
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    # Print the square
    for _ in range(size):
        print("#" * size)
