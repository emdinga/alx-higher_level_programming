#!/usr/bin/python3
import json

""""
This module  returns an object (Python data structure) represented by a JSON string
"""

def from_json_string(my_str):
    """
    Function to return an object represented by a JSON string.

    Args:
        my_str (str): The JSON string representing the object.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)

