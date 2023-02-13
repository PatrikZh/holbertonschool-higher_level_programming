#!/usr/bin/python3
""" Write method argument"""


def write_file(filename="", text=""):
    ''' Previous was read now we're in write mode'''
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
