#!/usr/bin/python3
""" Creates an class called BaseGeometry"""


class BaseGeometry:
    ''' Makes Empty class using pass function'''
    def __init__(self):
        pass

    ''' Area method that raises error message'''
    def area(self):
        raise Exception("area() is not implemented")

    ''' Method that validates value and raises errors'''
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.name = name
        self.value = value
