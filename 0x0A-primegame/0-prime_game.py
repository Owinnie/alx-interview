#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of consecutive
integers starting from 1 up to and including n, they take turns
choosing a prime number from the set and removing that number
and its multiples from the set.
The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for
each round. Assuming Maria always goes first and both players
play optimally, determine who the winner of each game is.

   - Prototype: def isWinner(x, nums)
   - where x is the number of rounds and nums is an array of n
   - Return: name of the player that won the most rounds
   - If the winner cannot be determined, return None
   - You can assume n and x will not be larger than 10000
   - You cannot import any packages in this task

Example:

    x = 3, nums = [4, 5, 1]

First round: 4

    - Maria picks 2 and removes 2, 4, leaving 1, 3
    - Ben picks 3 and removes 3, leaving 1
    - Ben wins because there are no prime numbers
    left for Maria to choose

Second round: 5

    - Maria picks 2 and removes 2, 4, leaving 1, 3, 5
    - Ben picks 3 and removes 3, leaving 1, 5
    - Maria picks 5 and removes 5, leaving 1
    - Maria wins because there are no prime numbers
    left for Ben to choose

Third round: 1

    Ben wins because there are no prime numbers for Maria to choose

Result: Ben has the most wins
"""


def isWinner(x, nums):
    """0.Prime Game"""
    max_n = max(nums)
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i**2, max_n+1, i):
                primes[j] = False

    # Count wins for each player
    wins = {"Maria": 0, "Ben": 0}
    for n in nums:
        prime_set = set()
        for i in range(2, n+1):
            if primes[i]:
                prime_set.add(i)

        current_player = "Maria"
        while prime_set:
            can_move = False
            for prime in prime_set:
                if n % prime == 0:
                    prime_set.discard(prime)
                    for multiple in range(prime, n+1, prime):
                        prime_set.discard(multiple)
                    can_move = True
                    break

            if not can_move:
                break

            if current_player == "Maria":
                current_player = "Ben"
            else:
                current_player = "Maria"

        if current_player == "Maria":
            wins["Ben"] += 1
        else:
            wins["Maria"] += 1

    # Determine winner
    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"
    else:
        return None
