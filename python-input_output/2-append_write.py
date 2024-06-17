#!/usr/bin/python3
"""Append a string to a text file"""


def append_write(filename="", text=""):
    """Append a string to the end of a text file"""
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
