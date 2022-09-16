#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    """Using a getter to retrive the size"""
    @property
    def size(self):
        return self.__size  

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
    
    """Public instance method that print the square in stdout"""
    def my_print(self):
        for i in range (0,self.__size):
           [print("#",end="") for j in range(self.__size) ]
           print("")
        if self.size == 0:
            print("")