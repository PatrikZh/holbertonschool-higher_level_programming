#!/usr/bin/python3
""" issubclass checks if child derives from parent class"""


def inherits_from(obj, a_class):
    ''' the first argument is child and second parent'''
    return issubclass(int, a_class)
