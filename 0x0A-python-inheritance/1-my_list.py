#!/usr/bin/python3

"""
The following contains a class MyList that inherits from a class list.
"""
class MyList(list):
    def __init__(self):
        """We can use the super method to inherit the list"""
        super.__init__()

    def print_sorted(self):
        """Sorting"""
        print(sorted(self))




