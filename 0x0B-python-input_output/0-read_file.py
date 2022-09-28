#!/usr/bin/python3

"""Introduction to working with files"""



def read_file(filename=""):
    """
    Remember to open the file using open(), 
    and close it  using closed() due to with keyword

    """
    with open(filename,encoding="utf_8") as f:
        f.read()
        f.closed