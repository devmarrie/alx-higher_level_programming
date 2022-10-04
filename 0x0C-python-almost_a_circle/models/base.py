#!/usr/bin/python3

"""
Defining a class Base.
"""
import json


class Base():
    """
    A private class variable  __nb_objects
    """
    __nb_objects = 0
    def __init__(self, id=None):
        self.id = id
        if self.id is not None:
            return self.id
        else:
            """
            Increment the base class and retrn it as the new id
            """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    """
    Static methods
    """
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None and list_dictionaries == []:
            return "[]"
        """
        Decerialise the list
        """
        json.dumps(list_dictionaries)

    """
    Writting a json representation to a file using json.dump
    It takes in two argments , the file and what is to be dumped.
    This is a class method since it takes the class as the first argument
    """
    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename,"w") as f:
            if list_objs is None:
                f.write("[]")
            f.write(Base.to_json_string(list_objs))


             