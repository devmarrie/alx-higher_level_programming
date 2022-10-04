#!/usr/bin/python3

"""
Defining a class Base.
"""
import json

from models.square import Square


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

    """
    A static method behaves like a normal method and does not pass an instance or a class
    We use the json.loads() method to convert to string
    """
    @staticmethod
    def from_json_string(json_string):
        if json_string is None and json_string == "[]":
            return []
        json.loads(json_string)

    """
    class method that returns an instance with all attributes already set
    """
    @classmethod
    def create(cls, **dictionary):
        sq = Square(12,1,2,6)
        sq.update(**dictionary)
    
    """
    Returns a list of all instances
    """
    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            f = open(filename)
            lst = Base.from_json_string(f.read())
            return [Base.create(**lst)]
        except FileNotFoundError:
            return []


        


             