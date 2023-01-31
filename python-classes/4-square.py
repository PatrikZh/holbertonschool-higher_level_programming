#!/usr/bin/python3
class Square:
        def __init__(self, size=0):
            if type(size) is int:
                True
            else:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                pass
            self.__size = size

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, value):
            if type(value) is int:
                  True
            else:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                pass    
            self.__size = value
        
        def area(self):
            return self.__size ** 2

