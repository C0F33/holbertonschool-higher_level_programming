#!/usr/bin/python3
"""Prints the list, but sorted (ascending sort)"""


class MyList(list):
    """Class that prints a list, but sorted (ascending sort)"""

    def print_sorted(self):
        print(sorted(self))
