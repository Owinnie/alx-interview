#!/usr/bin/python3
"""
Write a method that determines if a given data set
represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)

Return: True if data is a valid UTF-8 encoding,
else return False

A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers

Each integer represents 1 byte of data,
therefore you only need to handle the 8 least
significant bits of each integer
"""


def validUTF8(data):
    def check(num):
        mask = 1 << (8 - 1)
        i = 0
        while num & mask:
            mask >>= 1
            i += 1
        return i
    i = 0
    while i < len(data):
        j = check(data[i])
        k = i + j - (j != 0)
        i += 1
        if j == 1 or j > 4 or k >= len(data):
            return False
        while i < len(data) and i <= k:
            c = check(data[i])
            if c != 1:
                return False
            i += 1
    return True
