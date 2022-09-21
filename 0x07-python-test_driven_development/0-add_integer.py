#!/usr/bin/bash

"""A function that adds two numbers"""
def add_integer(a, b=98):
    """
    In this case we are given the value of b but it is not always given.
    """
    if not isinstance(a, int) or  not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or  not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
    