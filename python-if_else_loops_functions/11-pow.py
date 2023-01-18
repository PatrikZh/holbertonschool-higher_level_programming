#!/usr/bin/python3
def pow(a, b):
    if a < 0 and b < 0:
        a *= -1
        b *= -1
    return a * b
