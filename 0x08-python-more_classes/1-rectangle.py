#!/usr/bin/python3
""" Class that defines a Rectangle."""


class Rectangle:
    """
    Class that defines a Rectangle.
    """
    def __init__(self, width=0, height=0):
        """ Rectangle class constructor."""
        self.__width = width
        self.__height = height

    # Width getter method
    @property
    def width(self):
        """ width getter method
        Args:
            self: local variable.
        Returns:
            int: the rectangle width
        """
        return self.__width

    # Width setter method
    @width.setter
    def width(self, value):
        """
        Width setter method.
        Args:
            value (int): rectangle width variable
        Return:
            int: the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        # height getter method
        def height(self):
            """ Height getter method
            Args:
                self: local variable
            Returns:
                int: the rectangle height.
            """
            return self.__height

        # height setter method
        def height(self, value):
            """
            Height setter method.
            Args:
                self: local variable
                value (int): variable that holds rectangle height.
            Returns:
                int: the rectangle height.
            """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
