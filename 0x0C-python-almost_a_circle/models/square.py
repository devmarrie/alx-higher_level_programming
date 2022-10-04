#!/usr/bin/python3

from rectangle import Rectangle

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

    """

    1st argument should be the id attribute
    2nd argument should be the size attribute
    3rd argument should be the x attribute
    4th argument should be the y attribute
    **kwargs must be skipped if *args exists and is not empty
    """
    def update(self, *args, **kwargs):
        self.id = args[0]
        self.width = args[1]
        self.x = args[2]
        self.y = args[3]
        if args is  None and len(args) == 0:
            for key,value in kwargs:
                print("{}:{}".format(key,value))
        return ("[Square] ({}) {}/{} - {}".format(self.id,self.width,self.x,self.y))
        