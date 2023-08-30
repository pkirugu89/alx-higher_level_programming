#!/usr/bin/python3
class Square:
    """ This class defines a Square."""
    def __init__(self, size=0):
        """Initialize the size argument."""
        self.__size = size
    """ Function that defines the area of a square."""
    def area(self):
        """Returns the square area."""
        return self.__size**2
    """size getter method"""
    @property
    def size(self):
        """Returns the size."""
        return self.__size
    # setter method

    @size.setter
    def size(self, value):
        """size setter method."""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    # my_print method
    def my_print(self):
        """print square method."""
        if self.size == 0:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end='')
                print()
