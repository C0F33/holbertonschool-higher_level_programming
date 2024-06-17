#!/usr/bin/python3

import json
"""This module contains functions to serialize and deserialize data."""


def serialize_and_save_to_file(data, filename):
    """
    Serializes the given data and saves it to a file.

    Args:
            data: The data to be serialized.
            filename: The name of the file to save the serialized data to.

    Returns:
            The serialized data.

    Raises:
            IOError: If there is an error while writing to the file.
    """
    with open(filename, 'w') as f:
        json.dump(data, f)
    return data


def load_and_deserialize(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        return data
