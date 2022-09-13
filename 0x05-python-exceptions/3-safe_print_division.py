#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        print("Division by zero")
    finally:
       print("Inside result:{}".format(div))
