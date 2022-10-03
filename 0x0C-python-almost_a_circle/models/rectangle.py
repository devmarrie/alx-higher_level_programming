#!/usr/bin/python3
"""
import the Base class 
"""
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Defining instance variables as private ones
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """
    Width getter and setter
    They retrieve the width and change it respectively
    """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,width):
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width


    """
    height getter and setter
    They retrieve the height and change it respectively
    """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,height):
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height


    """
    x getter and setter
    They retrieve the x and change it respectively
    """
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,x):
       if x <= 0:
            raise ValueError("x must be > 0")
       self.__x = x
    """
    y getter and setter
    They retrieve the y and change it respectively
    """
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self,y):
        if y <= 0:
            raise ValueError("y must be > 0")
        self.__y = y
    
    """
    Calling the super method which calls the id from the main class
    """
    super().__init__(id)

