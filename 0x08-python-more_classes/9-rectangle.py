#!/usr/bin/python3
""" class that defines a rectangle."""


class Rectangle:
    """ class that defines a rectangle."""
    number_of_instances = 0  # tracks the number of instances
    print_symbol = '#'  # attribute for symbol used in string rep

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # increment the instance count

    # width getter method
    @property
    def width(self):
        """ Width getter method
            Args:
                self: local variable.
            Returns:
            int: rectangle width.
        """
        return self._width

    # width setter method
    @width.setter
    def width(self, value):
        """ width setter method
        Args:
            self: local variable.
            value (int): variable holding rectangle width
        Returns:
        int: width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    # height getter method
    @property
    def height(self):
        """ height getter method.
        Args:
            self: local variable.
        Returns:
        int: returns rectangle height.
        """
        return self._height

    # height setter method
    @height.setter
    def height(self, value):
        """ Height setter method.
        Args:
            self: local variable.
            value (int): variable holding rectangle height.

        Returns:
        int: height of rectangle.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    # area of a rectangle
    def area(self):
        """ Returns the area of a rectangle."""
        return self.width * self.height

    # perimeter of a rectangle
    def perimeter(self):
        """ Returns the perimeter of a rectangle."""
        return 2 * (self.width + self.height)

    # __str__() return visual representation of rectangle using #
    def __str__(self):
        """ Method that returns the visual rep of rectangle using '#'."""

        if self.width == 0 or self.height == 0:
            return ""
        rect_str = ""
        for _ in range(self.height):
            rect_str += str(self.print_symbol) * self.width + "\n"
        return rect_str[:-1]  # removes trailing newline

    # method that provides string rep that recreates the object
    def __repr__(self):
        """ method that provides string rep that recreates the object."""

        return f"Rectangle({self.width}, {self.height})"

    # delete rectangle method
    def __del__(self):
        """ Method that deletes the rectangle."""
        # Decrement the instance count
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    # compares two Rectangles instances based on area
    # returns the one with larger or equal area
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
    # method that creates a new rectangle instance equal to width n height

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
