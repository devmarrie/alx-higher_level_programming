#!/usr/bin/python3

from models.rectangle import Rectangle

"""
Defining a class square that inherits from rectangle
"""
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, width=size,height=size)
    
    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id,self.x,self.y,self.width))
    """
    Adding a public getter and setter.
    width and the height - with the same value
    """
    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
