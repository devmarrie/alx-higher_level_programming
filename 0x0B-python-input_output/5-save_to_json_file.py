#!/usr/bin/python3

"""
Writes an object to a textfile

"""

import json


def save_to_json_file(my_obj, filename):
    """
    Whenever you write remember to use the with kenyword
    """
    with open(filename,"w", encoding="utf-8") as f:
        return json.dump(my_obj,f)
        