#!/usr/bin/python3
""" Creates an class called BaseGeometry"""


class BaseGeometry:
    ''' Makes Empty class using pass function'''
    def __init__(self):
        pass
    ''' Area method that raises error message'''
    def area(self):
        raise Exception("area() is not implemented")
