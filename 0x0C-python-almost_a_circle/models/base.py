#!/usr/bin/python3
"""
Base class
"""

class Base:
    """
    Base class for managing id attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.

        Args:
            id (int): ID value for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
