#!/usr/bin/python3
"""Class called square"""


class Square:
    ''' __init__ method foucs on errors'''
    def __init__(self, size=0):
        if type(size) is int:
            True
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0") 
        self.__size = size 
    ''' getting the size'''
    @property
    def size(self):
        return self.__size
    ''' setting the new value'''
    @size.setter
    def size(self, value):
        if type(value) is int:
            True
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    ''' method to indicate area''' 
    def area(self):
        return self.__size ** 2
    ''' '''
    def my_print(self):
        for my_square in range(self.__size):
            for i in range(self.__size):
                print('#', end="")
            print()
        if self.__size == 0:
            print()

        
