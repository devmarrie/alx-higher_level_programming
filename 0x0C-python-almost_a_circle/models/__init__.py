#!/usr/bin/python3

"""
Defining a class Base.
"""
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

             