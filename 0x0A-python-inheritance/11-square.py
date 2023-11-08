#!/usr/bin/python3
"""
Class that defines a Rectangle subclass Square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that defines Square.
    """
    def __init__(self, size):
        """
        Initialize a Square.

        Args:
            self: Local variable
            size (int): The size of a square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return a string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
