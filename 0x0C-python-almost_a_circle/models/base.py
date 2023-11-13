#!/usr/bin/python3
"""
Class that defines a Base.
"""


class Base:
    """
    Base Model class.
    It's a base class for other classes in this project.
    Private class attribute:
    __nb_object (int): number of initiated bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Method initiates a new Base instance.
        Args:
            id (int): new base class identity.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
