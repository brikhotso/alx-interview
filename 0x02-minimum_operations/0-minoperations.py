#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Minimum Operations
    """
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n = n // divisor
        divisor += 1
    return operations
