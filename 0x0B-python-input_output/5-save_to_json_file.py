#!/usr/bin/python3
"""
This module write an object t a text file
"""
import json

def save_to_json_file(my_obj, filename):
    """
    Function to write an object to a text file, using a JSON representation.

    Args:
        my_obj: The object to be written to the file.
        filename (str): The name or path of the file to save the object to.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
