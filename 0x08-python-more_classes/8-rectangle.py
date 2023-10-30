#!/usr/bin/python3
""" This class defines a rectangle."""


class Rectangle:
    """ This class defines a rectangle."""
    # tracks the number of instances
    number_of_instances = 0
    # attribute for symbol used in string rep
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ class constructor that initializes height and width."""
        self.width = width
        self.height = height
        # increment the instance count
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """
        Height getter method.
        Args:
            self: local variable
        Returns:
            int: returns rectangle height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height setter method.
        Args:
            self: local variable.
            value (int): variable holding the rectangle's height.

        Returns:
            int: rectangle height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        Width getter method.
        Args:
            self: local variable
        Returns:
            int: rectangle's width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter method.
        Args:
            value (int): rectangle width variable
            self: local variable
        Returns:
            int: the rectangle width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    # area of a rectangle
    def area(self):
        """ method that returns the rectangle's area."""
        return self.__width * self.__height

    # perimeter of a rectangle
    def perimeter(self):
        """ method that returns a rectangle's perimeter."""
        return 2 * (self.__width + self.__height)

    # print the character '#'
    def __str__(self):
        """ Method that retuens the visual rep of rectangle using '#'."""
        if self.__width == 0 or self.__height == 0:
            return ''
        return '\n'.join([str(self.print_symbol)*self.__width]*self.__height)

    # method that provides string rep that recreates the object
    def __repr__(self):
        """ Method that provides string rep that recreates the object."""

        return f"Rectangle({self.__width}, {self.__height})"

    # delete rectangle method
    def __del__(self):
        """ Method that deletes the rectangle."""
        # Decrement the instance count
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
