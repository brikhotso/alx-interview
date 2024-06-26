#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle with n rows.

    Parameters:
    n (int): Number of rows in Pascal's Triangle.

    Returns:
    List[List[int]]: A list of lists representing Pascal's Triangle.
    """

    if n <= 0:
        return []
    # Initialize the triangle with the first row
    triangle = [[1]]  # row 0

    # Start from row number 1
    i = 1  # row number 1

    # Continue generating rows until we reach the desired number of rows (n)
    while i < n:
        # Initialize the current row as an empty list
        row = []

        # Construct the current row
        for j in range(i + 1):  # element in each row
            # The first and last elements of each row are always 1
            if j == 0 or j == i:
                row.append(1)
            else:
                # Each interior element is sum of two elements above it
                row.append(triangle[i-1][j-1] + triangle[i-1][j])

        # Append the constructed row to the triangle
        triangle.append(row)

        # Move to the next row
        i += 1

    # Return the complete Pascal's Triangle
    return triangle
