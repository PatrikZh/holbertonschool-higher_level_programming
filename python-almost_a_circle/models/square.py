#!/usr/bin/python3
""" Function that imports and inherits class Rectangle to Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    '''Method calls parent class and overwrites arguments to size'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self ,size):
        self.width = size
        self.height = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width
        )
