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
    m_count = b_count = 0
    m_choice = b_choice = 1
    prime_ls = []

    while x <= 10_000:
        for n in nums:
            ls = list(range(n + 1))[1:]
            for no in ls:
                if no > 1 and no % no == 0 and no % 1 == 0:
                    prime_ls.append(no)
            for i in range(len(prime_ls)):
                if i < len(prime_ls) and m_choice in prime_ls\
                        and prime_ls.index(m_choice)\
                        < len(prime_ls) and b_choice in prime_ls\
                        and prime_ls.index(b_choice)\
                        < len(prime_ls):
                    if prime_ls[i] == m_choice:
                        for p_nums2 in prime_ls:
                            if p_nums2 % prime_ls[i] == 0:
                                prime_ls.remove(p_nums2)
                        prime_ls.remove(prime_ls[i])
                        m_count += 1
                    elif prime_ls[i] != m_choice:
                        m_choice = prime_ls[i + 2]
                    if prime_ls[i] in prime_ls:
                        if prime_ls[i] == b_choice:
                            for p_nums2 in prime_ls:
                                if p_nums2 % prime_ls[i] == 0:
                                    prime_ls.remove(p_nums2)
                            prime_ls.remove(prime_ls[i])
                            b_count += 1
                    else:
                        b_choice = prime_ls[i + 1]
    if m_count > b_count:
        return "Maria"
    elif m_count < b_count:
        return "Ben"
    else:
        return None
