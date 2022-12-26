#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """ 
    Args:
    ----
        n: int

    Returns:
    -------
        List of lists of int representing Pascal's triangle
    """
    ls = []
    if n <= 0:
        return []
    else:
        for i in range(n):
            ans = (','.join(map(str, str(11**i))))
            for ele in ans:
                if ele != ',':
                    ls.append(int(ele))
            print(ls)
            ls.clear()
