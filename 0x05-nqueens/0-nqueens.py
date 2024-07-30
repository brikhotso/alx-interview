#!/usr/bin/python3
"""
Solves the N queens puzzle and prints all solutions
"""
import sys


def is_safe(board, row, col):
    """
    Checks if a queen can be placed at the position (row, col) without
    being attacked by any other queens already placed on the board
    """
    for i in range(row):
        # Check if there is a queen in the same column
        if board[i][1] == col:
            return False
        # Check if there is a queen in the same diagonal
        if board[i][1] - i == col - row or board[i][1] + i == col + row:
            return False
    return True


def solve_n_queens(n, row, board, solutions):
    """
    Places queens on board using backtracking and stores all valid solutions
    """
    if row == n:
        # We have placed queens in all rows; this is a valid solution
        solutions.append([list(pos) for pos in board])
        return

    for col in range(n):
        if is_safe(board, row, col):
            # Place a queen at (row, col)
            board[row] = [row, col]
            # Move to the next row
            solve_n_queens(n, row + 1, board, solutions)


def main():
    """
    Parses command-line arguments and starts solving the N queens puzzle
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[-1, -1] for _ in range(n)]
    solutions = []
    solve_n_queens(n, 0, board, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
