#!/usr/bin/python3



"""
Given a json string,
It returns an object (Python data structure) represented by a JSON string
"""

import json

def from_json_string(my_str):
    """
    We convert to an oblect using json.loads()
    """
    return json.loads(my_str)