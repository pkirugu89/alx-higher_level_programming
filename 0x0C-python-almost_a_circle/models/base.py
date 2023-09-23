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
    
    @staticmethod
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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.
        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dicts.
        Args:
            json_string (str): The JSON string rep.
        Returns:
            list: The list of dicts represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set based on a dict.
        Args:
            **dictionary (dict): A dict containing attribute-value pairs.
        Returns:
            cls: An instance of the class with attributes.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(dictionary)
            return new
