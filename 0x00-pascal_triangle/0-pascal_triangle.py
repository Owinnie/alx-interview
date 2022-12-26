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

    if n <= 0:
        return []
    else:
        for i in range(n):
            #print(' '*(n-i), end='')
            print([','.join(map(str, str(11**i)))])
