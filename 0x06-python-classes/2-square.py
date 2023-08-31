#!/usr/bin/python3
""" This class defines a square."""


class Square:
    """ This class defines a Square."""
    def __init__(self, size=0):
        """Initialize the size argument"""
        self.__size = size

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
