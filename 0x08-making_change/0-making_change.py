#!/usr/bin/python3
"""0-making_change"""


def makeChange(coins, total):
    """ Make change on Coins"""
    if total < 0:
        return 0
    # Sort coins in descending order
    coins.sort(reverse=True)

    # Initialize number of coins
    num_coins = 0

    # Try to use each coin
    for coin in coins:
        while total >= coin:
            total -= coin
            num_coins += 1

    if total == 0:
        return num_coins
    else:
        return -1
