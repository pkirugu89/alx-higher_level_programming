#!/usr/bin/python3
""" This class defines a Square."""


class Square:
    """ This class defines a Square."""

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize both size and position arguments.
        Args:
        size (int): size of the square
        position (int): position of squares

        Returns:
        int: returns both size and position values

        """
        self.__size = size
        self.__position = position

    def area(self):
        """ Method that returns the square area.
        Args:
        self: local variable

        Returns:
        int: square area

        """
        return self.__size**2

    # getter method
    @property
    def size(self):
        """ Method that returns the size of a square.
        Args:
        self: local variable

        Returns:
        int: the size of square

        """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter method.

        Args:
        self: local variable.
        value (int): variable that holds user input.

        Returns:
        int: square size.

        """
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """print square method."""
        if self.size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    # position getter method
    @property
    def position(self):
        """ Returns the position."""
        return self.__position

    # position setter method
    @position.setter
    def position(self, value):
        """ position setter method."""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if any(type(x) != int for x in value) or any(y < 0 for y in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
