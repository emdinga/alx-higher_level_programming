#!/usr/bin/python3
"""
This module create a file and count the number of char
"""

def write_file(filename="", text=""):
    """
    Function to write a string to a text file (UTF8) and return the number of characters written.

    Args:
        filename (str): The name or path of the file to write to.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars = file.write(text)
        return num_chars
