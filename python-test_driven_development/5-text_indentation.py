#!/usr/bin/python3
""" Function that will print newline after encoutering specified symbols"""


def text_indentation(text):
    ''' Checking and iterating over text for symbols'''
    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print("{}".format(text[i]), end="")
        if text[i] in ('.', '?', ':'):
            print('\n')
            if i + 1 != len(text):
                while text[i + 1] == ' ':
                    i += 1
        i += 1
