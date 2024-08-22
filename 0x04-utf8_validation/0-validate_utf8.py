#!/usr/bin/python3
"""
UTF-8 Validation Quiz
"""


def validUTF8(data):
    """
    data: a list of integers to validate
    Return: Return 'true' if data is a valid UTF-8
    encoding, else return 'false'
    """
    count = 0

    for i in data:
        if count == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                count = 1
            elif i >> 4 == 0b1110:
                count = 2
            elif i >> 3 == 0b11110:
                count = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            count -= 1
    return count == 0
