#!/usr/bin/python3
""" Class Rectangle that inherits from previous class Base"""


from models.base import Base


class Rectangle(Base):
    ''' Constructor method that takes all arguments and validates'''
    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        ''' Function that call area of the class'''
        return self.__width * self.__height

    def display(self):
        ''' Use nested loops and print in order to design the rectangle'''
        for h_space in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print('#' * self.__width)

    def __str__(self):
        ''' Str method that required string'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)
    def update(self, *args):
        print(self.__dict__)
        ls = []
        for i in self.__dict__.keys():
            ls.append(i)
        for j in range(len(args)):
            self.__dict__[ls[j]] = args[j]
