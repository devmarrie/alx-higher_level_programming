#!/usr/bin/python3

def raise_exception():
    try:
        num = int(input("Enter an integer"))
        print(num)
    except TypeError as err:
        print("Nonono", err)
    
