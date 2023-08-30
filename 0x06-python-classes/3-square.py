#!/usr/bin/python3
class Square:
    """ This class defines a square."""
    def __init__(self, size=0):
        """ initialize the size argument"""
        self.__size = size

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")


    """ Function that defines an area of a square."""
    def area(self):
        """Returns the square area."""
        return self.__size**2
