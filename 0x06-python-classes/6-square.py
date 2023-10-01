#!/usr/bin/python3
"""This class defines a Square."""


class Square:
    """This class defines a Square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize both size and position arguments.
        Args:
        size (int): size of the square
        position (int): position of squares

        Returns:
        int: returns both size and position values
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Method that returns the square area.
        Args:
        self: local variable

        Returns:
        int: square area

        """
        return self.__size ** 2

    # getter method
    @property
    def size(self):
        """
        Method that returns the size of a square.
        Args:
        self: local variable

        Returns:
        int: the size of square

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter method.

        Args:
        self: local variable.
        value (int): variable that holds user input.

        Returns:
        int: square size.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        print square method.

        Args:
        self: local variable.

        Returns:
        # if True.
        """
        if self.__size == 0:
            print()
            return
        for y in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()

    # position getter method
    @property
    def position(self):
        """
        Returns the position.
        Args:
        position (int): position of the square.

        Returns:
        int: position of the square.

        """
        return self.__position

    # position setter method
    @position.setter
    def position(self, value):
        """
        Position setter method.
        Args:
        self: local variable.
        value (int): variable that holds inputted positions.

        Returns:
        int: square position.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
