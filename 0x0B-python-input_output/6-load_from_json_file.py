#!/usr/bin/python3

"""
Creating an object from a JSON file
"""
import json

def load_from_json_file(filename):
    """
    using with keyword
    using json.load()
    """
    with open(filename) as f:
        return json.load(f)