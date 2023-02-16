#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    Prototype: def rotate_2d_matrix(matrix):
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will
    not be empty.
"""


def rotate_2d_matrix(matrix):
    """ 0. Rotate 2D Matrix """
    n = len(matrix[0])
    x = n // 2
    y = n - 1
    for i in range(x):
        for j in range(i, y - i):
            k = matrix[i][j]
            matrix[i][j] = matrix[y - j][i]
            matrix[y - j][i] = matrix[y - i][y - j]
            matrix[y - i][y - j] = matrix[j][y - i]
            matrix[j][y - i] = k
