#!/usr/bin/python3
def pow(a, b):
    result = 1
    index = 0
    if b == 0:
        return result
    if b < 0:
        while index < abs(b):
            result /= a
            index += 1
    else:
        while index < b:
            result *= a
            index += 1
    return result
