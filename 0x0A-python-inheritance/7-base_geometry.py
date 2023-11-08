#!/usr/bin/python3
"""
Class that defines a BaseGeometry.
"""


class BaseGeometry:
    """
    Class that defines BaseGeometry.
    """
    def area(self):
        """
        Raises an exception message.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates the given int value.
        Args:
            name (str): value name.
            value: validated value.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
