#!/usr/bin/python3
class Square:
    """ This class defines a Square."""
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize both size and position arguments."""
        self.__size = size
        self.__position = position

    def area(self):
        """Returns the square area."""
        return self.__size**2

    # getter method
    @property
    def size(self):
        """Returns the size of a square."""
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter method."""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """print square method."""
        if self.size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
                for x in range(self.__size):
                    for j in range(self.__position[0]):
                        print('', end='')
                    for y in range(self.__size):
                        print("#", end='')
                    print()

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
