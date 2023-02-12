#!/usr/bin/python3
""" Creating an class called square"""


Rectangle = __import__('9-rectangle').Rectangle


class Sqaure(Rectangle):
    ''' Constructor function(init), size must be private'''
    def __init__(self, size):
        self.__size = size

    '''Area function that returns area'''
    def area(self):
        return self.__size
