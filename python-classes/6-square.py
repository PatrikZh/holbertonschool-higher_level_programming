#!/usr/bin/python3
"""Class called square"""


class Square:
    ''' __init__ method foucs on errors'''
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is int:
            True
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
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
    ''' Printing square with #'s'''
    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for my_square in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                print('#', end="")
            print()
