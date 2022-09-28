#!/usr/bin/python3
"""
Given a class containing various attributes and methods it returns 
alist of available attributes and methods of the  object.

"""
def lookup(obj):
    """
    We use the dir() method which returns a list containing strings
    """
    return (dir(obj))   