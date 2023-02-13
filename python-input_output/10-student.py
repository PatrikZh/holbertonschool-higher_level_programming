#!/usr/bin/python3
""" Creating class called Student"""


class Student:
    ''' Constructing the required contents'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    ''' Method in order to return attributes and values of object(self)'''
    def to_json(self, attrs=None):
        result = {}
        if attrs is None:
            for key, value in self.__dict__.items():
                result[key] = value
        else:
            for attr in attrs:
                if attr in self.__dict__:
                    result[attr] = self.__dict__[attr]
        return result
