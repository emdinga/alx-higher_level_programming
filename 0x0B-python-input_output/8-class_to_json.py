#!/usr/bin/python3
"""
This module return the dictionary description
"""

def class_to_json(obj):
    """
    Function to return the dictionary description with a simple data structure for JSON serialization of an object.

    Args:
        obj: The object to be serialized.

    Returns:
        dict: The dictionary description of the object.
    """
    json_dict = {}
    for attr in obj.__dict__:
        value = getattr(obj, attr)
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value
    return json_dict
