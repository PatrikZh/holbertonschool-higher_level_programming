#!/usr/bin/python3
""" Function returns True if object is exactly an instance of a_class otherwise False"""


def is_same_class(obj, a_class):
    ''' Check it using is to compare'''
    if type(obj) is a_class:
        return True
    return False
