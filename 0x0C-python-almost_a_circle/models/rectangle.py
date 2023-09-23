#!/usr/bin/python3
"""Rectangle Base Class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from the Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize the Rectangle instances.
        Args:
            width (int): rectangle's width.
            height (int): rectangle's height.
            x (int): X-coordinate of the rectangle's position. Defaults to 0.
            y (int): Y-coordinate of the rectangle's position. Defaults to 0.
            id (int, optional): The ID for the instance. Defaults to None.
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
        """width setter method."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter method."""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Rectangle x co-ordinate getter method."""
        return self.__x

    @x.setter
    def x(self, value):
        """x co-ordinate setter method."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Rectangle y co-ordinate getter method."""
        return self.__y

    @y.setter
    def y(self, value):
        """y co-ordinate setter method."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of a Rectangle."""
        return self.width * self.height

    def display(self):
        """
        print # symbol to display a rectangle based on input values
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print("", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """
        Return the print() and str() rectangle representation.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}\
                ".format(self.id, self.x, self.y, self.width, self.height)
