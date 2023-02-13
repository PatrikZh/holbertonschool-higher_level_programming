#!/usr/bin/python3
"""  Append method argument"""


def append_write(filename="", text=""):
    ''' Mode a stands for appending'''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
