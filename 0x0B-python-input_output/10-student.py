#!/usr/bin/python3
"""Class that define a Student."""


class Student:
    """Class that represent a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student.

        Args:
            firstname (str): student's first name.
            lastname (str): student's last name.
            age (int): student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Student info in JSON format.
        Args:
            attrs (list): Thr attributes to represent.
        """
        if (type(attrs) == list and
                all(type(el) == str for el in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__
