#!/usr/bin/python3
""" This module contains a function that writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation"""
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
