#!/usr/bin/python3
"""Square class inherits from Rectangle class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the Square instance.

        Args:
            size (int): Size of the square (both width and height).
            x (int): x-coordinate of the square's position. Defaults to 0.
            y (int): y-coordinate of the square's position. Defaults to 0.
            id (int): The ID for the instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ square size getter method."""
        return self.width

    @size.setter
    def size(self, value):
        """ square size setter method."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns print() and str() for Square representation."""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
