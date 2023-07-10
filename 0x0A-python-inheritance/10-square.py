#!/usr/bin/python3
"""
THis module represents a class Square that inherit Rectangle
"""

class Square(Rectangle):
    """Class representing a square."""

    def __init__(self, size):
        """Initializes a square with a given size."""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Returns a string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
