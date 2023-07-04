#!/usr/bin/python3

import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].

    Args:
        board (list): The chessboard representation.
        row (int): The row to check.
        col (int): The column to check.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check for queens in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check for queens in the upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check for queens in the upper-right diagonal
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(board, row):
    """
    Solve the N-queens problem using backtracking.

    Args:
        board (list): The chessboard representation.
        row (int): The current row to place a queen.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    if row == N:
        # Solution found, print the board
        print([[i, j] for i in range(N) for j in range(N) if board[i][j] == 1])
        return True

    for col in range(N):
        if is_safe(board, row, col):
            # Place the queen at board[row][col]
            board[row][col] = 1

            # Recur for the next row
            solve_nqueens(board, row + 1)

            # Backtrack and remove the queen from board[row][col]
            board[row][col] = 0

    return False

if __name__ == "__main__":
    # Parse the command-line argument
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Solve the N-queens problem
    solve_nqueens(board, 0)
