#!/usr/bin/python3

"""
Finding a list of available attributes & methods of an object
"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    Args:
        - obj: object to look into
    """
    return dir(obj)
