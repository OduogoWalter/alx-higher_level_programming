#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]"""
    for i in range(row):
        if (
            board[i] == col
            or board[i] - i == col - row
            or board[i] + i == col + row
        ):
            return (False)
    return (True)


def solve_nqueens(board, row, n, solutions):
    """Recursive function to find all solutions to the N queens problem"""
    if row == n:
        solutions.append([i, board[i]] for i in range(n))
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)
            board[row] = 0  # backtrack


def print_solutions(solutions):
    """Print the solutions in the required format"""
    for solution in solutions:
        print(list(solution))


def nqueens(n):
    """Main function to solve the N queens problem"""
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [0] * n
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
