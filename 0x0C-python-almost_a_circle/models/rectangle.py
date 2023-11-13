#!/usr/bin/python3
"""
Class that defines a Rectangle inherited from Base.
"""
from models.base import Base


class Rectangle (Base):
    """
    Rectangle class inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Method that initializes rectangle class instances.
        Args:
            width (int): rectangle's width
            height (int): rectangle's height.
            x (int): x-coordinates of this class. Defaults to 0.
            y (int): y-coordinates of this class. Defaults to 0.
            id (int, optional): ID for the instance. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter method."""
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter method.
        Args:
            self: local variable.
            value (int): variable holding width value.
        Returns:
            int: returns the width value of rectangle.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Height getter method."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height setter method.
        Args:
            self: local vairiable.
            value (int): value set to height.
        Returns:
            int: returns the height value of rectangle.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x - co-ordinates getter method."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        x - co-ordinates setter method.
        Args:
            self: local variable.
            value (int): variable that holds the x value.
        Returns:
            int: returns the value of rectangle x co-ordinates.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y- co-ordinates getter method."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        y co-ordinate setter method.
        Args:
            self: local variable.
            value (int): variable holding the y value.
        Returns:
            int: returns the rectangle value of y co-ordinate
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Method that returns the area of a rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Method that prints '#' symbol to display a rectangle\
                based on input values.
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """
        Return the print() and str() rectangle representation.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)
