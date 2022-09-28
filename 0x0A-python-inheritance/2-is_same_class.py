#!/usr/bin/python3

"""A function that returns true if an object is the exact instance as the class    iis_same_class(7,int)"""
def is_same_class(obj, a_class):
    """We use an if function to test the condition"""
    if isinstance(obj, a_class):
        return True   

    return False

