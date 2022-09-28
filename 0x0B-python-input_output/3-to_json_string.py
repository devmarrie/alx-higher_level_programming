#!/usr/bin/python3

"""
JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    use the json.dumps() ethod to convert to string
    """
    return json.dumps(my_obj)