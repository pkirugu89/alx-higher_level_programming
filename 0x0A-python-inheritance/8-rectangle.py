#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Class Rectangle."""


class Rectangle(BaseGeometry):
    """Class that defines a Rectangle."""
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            ValueError: If width or height is not a positive integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """__str__ magic method."""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height
