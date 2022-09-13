#!/usr/bin/python3

from decimal import DivisionByZero


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0,list_length):
        try:
            out = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("Wrong type")
        except DivisionByZero:
            print("division by 0")
        except IndexError:
            print("Out of range")
        except:
            print("Items cannot be divided")
            out = 0
        finally:
            new_list.append(out)
    return(new_list)    


