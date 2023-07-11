#!/usr/bin/python3
"""
This module reads stdin line by line
"""

import sys

def print_stats(total_size, status_codes):
    """
    Prints the statistics including total file size and number of lines by status code.

    Args:
        total_size (int): The total file size.
        status_codes (dict): Dictionary containing the counts of each status code.
    """
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes):
        print("{:d}: {:d}".format(code, status_codes[code]))

def parse_line(line):
    """
    Parses a line and extracts the status code and file size.

    Args:
        line (str): The line to parse.

    Returns:
        tuple: A tuple containing the status code (int) and file size (int).
    """
    parts = line.split(" ")
    code = int(parts[-2])
    size = int(parts[-1])
    return code, size

def compute_stats():
    """
    Reads stdin line by line, computes metrics, and prints the statistics.
    """
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            code, size = parse_line(line)
            total_size += size
            status_codes[code] = status_codes.get(code, 0) + 1

            if i % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

compute_stats()
