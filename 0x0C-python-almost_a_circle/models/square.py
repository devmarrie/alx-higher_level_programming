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
