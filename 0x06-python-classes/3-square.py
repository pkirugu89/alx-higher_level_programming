#!/usr/bin/python3
""" This class defines a Square."""


class Square:
    """ This class defines a square."""
    def __init__(self, size=0):
        """ initialize the size argument.
        Args:
        size (int): size of square.

        Returns:
        int: The size of square

        """
        self.__size = size

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Method that returns the square area.
        Args:
        self: local variable.

        Returns:
        int: square area.
        """
        return self.__size**2
