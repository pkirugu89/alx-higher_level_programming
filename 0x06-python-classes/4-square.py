#!/usr/bin/python3
""" This class defines a square."""


class Square:
    """ This class defines a Square. """
    def __init__(self, size=0):
        """ initialize the size argument.
        Args:
        size (int): size of square.

        Returns:
        int: The size of square.
        """
        self.__size = size

    # square area
    def area(self):
        """Method that returns the square area.

        Args:
        self: local variable.

        Returns:
        int: square area.
        """
        return self.__size**2

    # getter method
    @property
    def size(self):
        """ Method returns the size of the square.

        Args:
        self: local variable.

        Returns:
        int: the size of square
        """
        return self.__size

    # size setter method
    @size.setter
    def size(self, value):
        """ size setter method.

        Args:
        self: local variable.
        value: variable that holds user input.

        Returns:
        int: square size.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
