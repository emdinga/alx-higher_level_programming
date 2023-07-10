#!/usr/bin/python3
"""
This module implement a base class
"""

class BaseGeometry:
    """Base class representing geometry."""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception('area() is not implemented')
