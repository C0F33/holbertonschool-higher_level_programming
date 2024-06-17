#!/usr/bin/python3
"""Write an object to a text file using JSON representation"""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file"""
    with open(filename, "r") as f:
        return json.load(f)
