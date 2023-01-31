#!/usr/bin/python3
""" Class called Square"""


class Square:
    ''' __init__ method foucs on errors'''
    def __init__(self, size=0):
        self.__self = self
        if type(size) == int:
            True
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
