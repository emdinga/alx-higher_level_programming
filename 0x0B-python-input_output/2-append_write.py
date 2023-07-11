#!/usr/bin/python3
"""
This Module create a function to append a file
"""

def append_write(filename="", text=""):
    """
    Function to append a string at the end of a text file (UTF8) and return the number of characters added.

    Args:
        filename (str): The name or path of the file to append to.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.seek(0, 2)
        num_chars = file.write(text)
        return num_chars
