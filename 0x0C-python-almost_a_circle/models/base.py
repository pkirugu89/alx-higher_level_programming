#!/usr/bin/python3
"""
Class that defines a Base.
"""
import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts dict list to a JSON string rep.
        Args:
            list_dictionaries (list): dict list converted into JSON.
        Returns:
            str: JSON string rep of dict list.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Method that writes json str rep of list_objs to a file.
        Args:
            list_objs (list): List instances that inherits from Base.
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, mode="w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [ob.to_dictionary() for ob in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts JSON str to dict list.
        Args:
            json_sring (str): JSON sring rep.
        Returns:
        list: Dicts list represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Method creates attributes instances based on a dict.
        Args:
            **dictionary (dict): Dict containing attribute-value pairs.
        Returns:
            cls: Instance of the class with attributes.
        """
        if cls.__name__ == "Rectangle":
            nw = cls(1, 1)
        elif cls.__name__ == "Square":
            nw = cls(1)
        else:
            nw = None
        if nw:
            nw.update(**dictionary)
        return nw

    @classmethod
    def load_from_file(cls):
        """
        Method that returns instances list.
        """
        file_name = cls.__name__ + ".json"
        lists = []
        list_dicts = []
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                st = f.read()
                list_dicts = cls.from_json_string(st)
                for dct in list_dicts:
                    lists.append(cls.create(**dct))
        return lists
