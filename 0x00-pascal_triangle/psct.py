#!/usr/bin/python3
""" Pascal's Triangle """


def fact(n):
    """ Calculate the factorial of a no.
    Assumes n is always a +ve int
    """
    if n < 2:
        return 1
    else:
        return n * fact(n-1)


def pascal_triangle(n):
    """
    Args:
    ----
        n: int

    Returns:
    -------
        List of lists of int representing Pascal's triangle
    """
    for i in range(n):
        for j in range(i+1):
            ans = fact(i)//(fact(j)*fact(i-j))
            print(ans, end=",")
        print()
