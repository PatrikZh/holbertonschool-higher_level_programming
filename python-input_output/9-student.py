#!/usr/bin/python3
""" Creating class called Student"""


class Student:
    ''' Constructing the required contents'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    ''' Method in order to return attributes and values of object(self)'''
    def to_json(self):
        return self.__dict__
