#!/bin/bash/python3

"""Prints is true if an object is an instance of a class or an inherited class"""

def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
       """So long as the class is defined the object will always ingherit from the class"""
       return True
    return False