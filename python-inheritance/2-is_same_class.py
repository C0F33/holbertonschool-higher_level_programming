#!/usr/bin/python3
"""module that checks if class matche instance"""


def is_same_class(obj, a_class):
    """Function to check if an object is an instance of a class"""
    if type(obj) == a_class:
        return True
    else:
        return False
