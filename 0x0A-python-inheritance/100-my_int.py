#!/usr/bin/python3
"""
This module represents an internger
"""

class MyInt(int):
    """Class representing a rebel integer."""

    def __eq__(self, other):
        """Overrides the equality operator (==) to invert the behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides the inequality operator (!=) to invert the behavior."""
        return super().__eq__(other)

