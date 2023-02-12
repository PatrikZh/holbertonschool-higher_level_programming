#!/usr/bin/python3
""" Creating an class called square"""


Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    ''' Constructor function(init), size must be private'''
    def __init__(self, size):
        BaseGeometry.integer_validator(self, "size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    ''' Area function that returns area'''
    def area(self):
        return self.__size ** 2
