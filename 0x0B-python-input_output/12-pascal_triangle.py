#!/usr/bin/python3
"""
This module  returns a lists of integers representing the Pascal’s triangle
"""
def pascal_triangle(n):
    """
    Generates Pascal's traiangle up to a given number of rows

    Args:
        n (int): The number of rows in a Pascal traingle

    Returns: 
        Lists: A list of List representing Pascal traingle
    """
    traingle = []

    if n <= 0:
        return traingle

    for i in range(n):
        row = []
        for a in range(i + 1):
            if a == 0 or a == i:
                row.append(1)
            else:
                prev_row = traingle[i - 1]
                num = prev_row[a - 1] + prev_row[a]
                row.append[num]
        traingle.append(row)
    return traingle
