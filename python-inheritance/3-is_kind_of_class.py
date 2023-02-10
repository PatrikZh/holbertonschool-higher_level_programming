#!/usr/bin/python3
""" Function that checks obj against a class if its an instance of"""


def is_kind_of_class(obj, a_class):
    ''' Check it using isinstance, takes an obj and class as arugments'''
    return isinstance(obj, a_class)
