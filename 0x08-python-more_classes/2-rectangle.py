#!/usr/bin/python3
""" This class defines a rectangle."""


class Rectangle:
    """ This class defines a rectangle."""
    def __init__(self, width=0, height=0):
        """ class constructor that initializes height and width."""
        self.width = width
        self.height = height

    # height getter method
    @property
    def height(self):
        """
            Height getter method.
            Args:
                self: local variable
            Returns:
                int: returns rectangle height.
        """
        return self._height

    # height setter method
    def height(self, value):
        """
            Height setter method.
            Args:
                self: local variable
                value (int): variable holding rectangles height.

            Returns:
            int: rectangle height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self._height = value

    # width getter method
    def width(self):
        """ Width getter method.
            Args:
                self: local variable
            Returns:
            int: width of rectangle
        """
        return self._width

    # width setter method
    def width(self, value):
        """
        Width setter method.
        Args:
            self: local variable
            value (int): variable holding rectangle width.
        Returns:
        int: returns the width of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    # area of rectangle method
    def area(self):
        """ method that returns area of rectangle."""
        return self.width * self.height

    # perimeter of rectangle method
    def perimeter(self):
        """ method that returns perimeter of a rectangle."""
        return 2 * (self.width + self.height)
