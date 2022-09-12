#!/usr/bin/python3

def safe_print_integer(x):
    try:
       print("{x}:d".format())
       return(True)
    except (TypeError, ValueError):
        print("{} is not an integer".format(x))
        return(False)