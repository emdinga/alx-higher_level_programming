#!/usr/bin/python3
"""
This module create a class to read files
"""
def read_file(filename=""):
    """
    Function to read a text file (UTF8) and print its contents to stdout.

    Args:
        filename (str): The name or path of the file to be read.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end='')
