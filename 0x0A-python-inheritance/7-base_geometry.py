#!/usr/bin/python3
"""
This module represents a goementry class
"""

class BaseGeometry:
    """Base class representing geometry."""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates the value to ensure it is an integer greater than 0."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
