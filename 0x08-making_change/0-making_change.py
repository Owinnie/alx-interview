#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed
to meet a given amount total.

    - Prototype: def makeChange(coins, total)
    - Return: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have,
        return -1
    - coins is a list of the values of the coins in your possession
    - The value of a coin will always be an integer greater than 0
    - You can assume you have an infinite number of each
      denomination of coin in the list
    - Your solution’s runtime will be evaluated in this task
"""


def makeChange(coins, total):
    """0. Change comes from within"""
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    if total <= 0:
        return 0
    elif sum(coins) != total:
        return -1
    else:
        count = 0
        for c in coins:
            if c == total:
                count += 1
                return count

        for a in range(1, total + 1):
            for c in coins:
                if (a - c) >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[total] if dp[total] != total + 1 else -1
