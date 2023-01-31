#!/usr/bin/python3
""" 0. N queens
The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.
"""


from sys import argv, exit

if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if n < 4:
    print("N must be at least 4")
    exit(1)

col = set()
pos = set()  # row + column
neg = set()  # rom - column

result = []
board = [["0"] * n for i in range(n)]


def btrack(r):
    if r == n:
        cp = ["".join(row) for row in board]
        result.append(cp)
        return

    for c in range(n):
        if c in col or (r + c) in pos or (r - c) in neg:
            continue

        col.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = "Q"

        btrack(r + 1)

        col.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = "0"


btrack(0)
print(result)
