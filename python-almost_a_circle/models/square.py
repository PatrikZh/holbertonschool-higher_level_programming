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
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        '''Update method that keeps track of args and kwargs'''
        attribute_list = ["id", "size", "x", "y"]
        if args:
            for idx, element in enumerate(args):
                if idx < len(attribute_list):
                    setattr(self, attribute_list[idx], args[idx])
        elif kwargs:
            for key, value in kwargs.items():
                if key in attribute_list:
                    setattr(self, key, value)

    def to_dictionary(self):
        ''' Method that returns the dictionary representation of a Rectangle'''
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
        }
