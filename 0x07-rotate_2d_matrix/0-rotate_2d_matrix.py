#!/usr/bin/env python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
    matrix (list of list of int): The n x n matrix to rotate.

    Example:
    Given matrix:
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    After calling rotate_2d_matrix(matrix), the matrix becomes:
    [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        matrix[i] = matrix[i][::-1]
