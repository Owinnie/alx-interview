#!/usr/bin/python3
""" Count no. of copy paste operations """


def minOperations(n):
    """Calculates the fewest number of operations
    needed to result in exactly n H characters in
    the file.

    Returns:
        integer of 0 if impossible
    """
    pasted = 1  # chars present in the file
    copied = 0
    operations = 0  # counter

    while pasted < n:
        # copy operation
        if copied == 0:
            copied = pasted
            operations += 1

        # paste operation
        if pasted == 1:
            pasted += copied
            operations += 1
            continue

        rem = n - pasted  # remaining to be pasted

        if rem < copied:
            return 0

        if rem % pasted != 0:
            pasted += copied
            operations += 1
        else:
            copied = pasted
            pasted += copied
            operations += 2

    if pasted == n:
        return operations
    else:
        return 0
