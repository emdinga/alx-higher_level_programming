#!/usr/bin/python3

"""
Finding a list of available attributes & methods of an object
"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    return dir(obj)
