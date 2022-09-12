#!/usr/bin/python3

def safe_print_integer(x):
    try:
       print("{x}:d".format())
       print("")
    except TypeError:
        print("{} is not an integer".format(x))