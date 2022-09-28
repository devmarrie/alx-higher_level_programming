#!/usr/bin/python3

"""
Writting to a function.

"""
def write_file(filename="", text=""):
    """
    Using the with keyword for easy closing of the file afterwards
    """
    with open(filename,encoding="utf-8") as f:
        return f.write(text)
        