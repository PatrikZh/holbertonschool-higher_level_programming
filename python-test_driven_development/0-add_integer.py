#!/usr/bin/python3
""" Function that adds integers"""


def add_integer(a, b=98):
    ''' Checking if type of a, b aren't int or float'''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    ''' If type a, b are float, convert them to int'''
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
