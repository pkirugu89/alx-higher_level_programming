#!/usr/bin/python3
""" Method that prints a square with # character."""


def print_square(size):
    """
    Print the square based on integer
    Args:
        size (int): size of printed square
    Returns:
    char: prints the # square based on the size

    """
    # check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # check if the size is non-negative
    if size < 0:
        raise ValueError("size must be >= 0")

    # check if size is float or less than 0
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # print the square
    for _ in range(size):
        print("#" * size)
