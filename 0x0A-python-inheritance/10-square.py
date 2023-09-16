#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that defines a Square."""

    def __init__(self, size):
        """
        Initializes a square
        Args:
            self: local variable.
            size (int): The size of a square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
