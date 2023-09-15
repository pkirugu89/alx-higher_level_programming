#!/usr/bin/python3
"""Class that defines BaseGeometry."""


class BaseGeometry:
    """ BaseGeometry class."""
    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented.'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the given integer value.

        Args:
            name (str): The name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
