#!/usr/bin/python3
""" Function that will print newline after encoutering specified symbols"""


def text_indentation(text):
    ''' Checking and iterating over text for symbols'''
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in text:
        print("{}".format(i), end="")
        if i in ('.', '?', ':'):
            print('\n')
