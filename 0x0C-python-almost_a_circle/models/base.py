#!/usr/bin/python3
"""Class that defines a Base."""
import json


class Base:
    """ Base Model class.
    Represents the base class for other classes in this project.
    There's private class attribute:
        __nb_objects (int): number of initiated bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initiates a new Base instance
        Args:
            id (int): new base class identity.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string representation.
        Args:
            list_dictionaries (list): A list of dictionaries to be
            converted to JSON.
        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
