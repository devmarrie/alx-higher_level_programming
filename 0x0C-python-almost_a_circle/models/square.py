#!/usr/bin/python3

from rectangle import Rectangle

"""
Defining a class square that inherits from rectangle
"""
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)
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

    
    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id,self.x,self.y,self.width))
    
    
    """

    1st argument should be the id attribute
    2nd argument should be the size attribute
    3rd argument should be the x attribute
    4th argument should be the y attribute
    **kwargs must be skipped if *args exists and is not empty
    """
    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    """
    Adding a dictonary defination.
    """
    def to_dictionary(self):
        return {
            "id":self.id,
            "size":self.width,
            "x":self.x,
            "y":self.y
        }
    

if __name__ == "__main__":

    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)