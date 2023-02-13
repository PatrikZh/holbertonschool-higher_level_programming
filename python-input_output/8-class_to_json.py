#!/usr/bin/python3
"""obj.__dict__ you're returning dictionary(key,value) of object attributes"""


def class_to_json(obj):
    ''' Wer are returning all the attributes and their values of obj'''
    return obj.__dict__
