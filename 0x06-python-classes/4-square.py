#!/usr/bin/python3
class Square:
    """ This class defines a Square. """
    def __init__(self, size=0):
        """ initialize the size argument."""
        self.__size = size
    # square area
    """ Function that defines an area of a square."""
    def area(self):
        """Returns the square area."""
        return self.__size**2

    # getter method
    @property
    def size(self):
        """ returns the size of the square."""
        return self.__size

    # size setter method
    @size.setter
    def size(self, value):
        """ size setter method."""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
