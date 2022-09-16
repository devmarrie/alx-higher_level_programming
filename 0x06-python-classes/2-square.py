#!/bin/usr/python3

"""Defining a class as the blueprint of all the objects we shall define"""
class Square:
    """Instantiating our class using __init__"""
    def __init__(self, size=0):
       """Testing the size input for errors and raising them"""
       if not type(size) == int:
         raise TypeError("Size must be an integer")
       elif size < 0:
            raise ValueError("size must be >= 0")
       self.__size = size

   




        