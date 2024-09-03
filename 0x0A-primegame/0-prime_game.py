#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Determine who wins the most rounds of the prime game
    """
    if x < 1 or not nums:
        return None

    marias_wins = 0
    bens_wins = 0

    for i in range(x):
        n = nums[i]
        primes = [True] * (n+1)

        for p in range(2, int(n**0.5)+1):
            if primes[p]:
                for i in range(p*p, n+1, p):
                    primes[i] = False

        primes_count = 0
        for j in range(2, n+1):
            if primes[j]:
                primes_count += 1

        if primes_count % 2 == 1:
            marias_wins += 1
        else:
            bens_wins += 1

    if marias_wins == bens_wins:
        return None
    elif marias_wins > bens_wins:
        return 'Maria'
    else:
        return 'Ben'
