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
        Calling the super method which calls the id from the main class
        """
        super().__init__(id)


    """
    Width getter and setter
    They retrieve the width and change it respectively
    """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("<name of the attribute> must be > 0")
        self.width = width

    """
    height getter and setter
    They retrieve the height and change it respectively
    """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("<name of the attribute> must be > 0")
        self.height = height

    """
    x getter and setter
    They retrieve the x and change it respectively
    """
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x <= 0:
            raise ValueError("x must be >= 0")
        self.x = x
    """
    y getter and setter
    They retrieve the y and change it respectively
    """
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y <= 0:
            raise ValueError("y must be >= 0")
        self.y = y

    """
    Creating a method that calculates the area
    """
    def area(self):
        return self.__width * self.__width

    """
    Printing the rectangle instance
    """
    def display(self):
        if self.width == 0 or self.height == 0:
            print("")
        for i in range(self.__height):
            for j in range(self.__width):
                print("#",end="")
