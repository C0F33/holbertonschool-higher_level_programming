#!/usr/bin/python3
""" This module contains json"""
import json


def from_json_string(my_str):
    """Return the object represented by a JSON string"""
    return json.loads(my_str)
