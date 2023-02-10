#!/usr/bin/python3
""" issubclass checks if child derives from parent class"""


def inherits_from(obj, a_class):
    ''' it also checks if obj is not equal to a_class'''
    return issubclass(type(obj), a_class) and type(obj) != a_class
