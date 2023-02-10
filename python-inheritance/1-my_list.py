#!/usr/bin/python3
""" Class that creates MyList derived from list"""


class MyList(list):
    ''' Sorting self and storing it in new_list'''
    def print_sorted(self):
        new_list = sorted(self)
        return new_list
