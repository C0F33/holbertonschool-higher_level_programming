#!/usr/bin/python3
"""this module reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """
    Read a text file and print its contents to the standard output.

    Args:
            filename (str): The name of the file to be read.

    Returns:
            None
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end="")
