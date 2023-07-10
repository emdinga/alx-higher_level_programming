#!/usr/bin/python3
"""
THis module returns True if the object is an instance of a class that inherited
"""

def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class inherited (directly \
            \or indirectly) from a specified class.
     """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

