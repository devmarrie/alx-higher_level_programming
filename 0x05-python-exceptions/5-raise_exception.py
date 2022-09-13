#!/usr/bin/python3

def raise_exception():
    try:
        num = int(input("Enter an integer"))
    except TypeError as err:
        print("Nonono", err)
