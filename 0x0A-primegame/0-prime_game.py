#!/usr/bin/python3
""" Prime Game """

def isWinner(x, nums):
    """
    Determines the winner of multiple rounds of a prime number game.

    Parameters:
    x (int): The number of rounds to play.
    nums (list of int): A list where each element represents the maximum number n for that round.

    Returns:
    str: The name of the player with the most wins ("Maria" or "Ben").
    None: If there's a tie between Maria and Ben.
    """
    def sieve(n):
        """
        Checks if a given number n is prime.
        """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """
        Simulates one round of the prime number game.
        """
        primes = sieve(n)
        moves = 0
        while primes:
            prime = primes.pop(0)
            primes = [p for p in primes if p % prime != 0]
            moves += 1
        return moves % 2 == 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
