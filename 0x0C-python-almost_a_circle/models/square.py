#!/usr/bin/python3
"""
Square class inherits from Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the Square instance.
        Args:
            size (int): Square size (width and height).
            x (int): x co-ordinate of square's position. Defaults to 0.
            y (int): y co-ordinates of square's position. Defaults to 0.
            id (int): Instance Id. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Square size getter method."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Square size setter method.
        Args:
            self: local variable.
            value (int): variable holding size value.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns print() and str() for Square representation.
        """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
