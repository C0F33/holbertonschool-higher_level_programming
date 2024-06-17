#!/usr/bin/python3
"""Module to check if something is inherinting from another class"""


def inherits_from(obj, a_class):
    """Function to check if an object is an instance of a class"""
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    else:
        return False
