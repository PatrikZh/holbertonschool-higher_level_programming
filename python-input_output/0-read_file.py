#!/usr/bin/python3
""" Function reads content of a file and outputs it to the console"""


def read_file(filename=""):
    ''' with function to wrap the opening of the file'''
    with open(filename="", encoding="utf-8") as f:
        print(f.read(), end="")
