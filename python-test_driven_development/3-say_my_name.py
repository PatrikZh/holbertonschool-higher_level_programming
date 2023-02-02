#!/usr/bin/python3
""" Function that prints first&last name"""
def say_my_name(first_name, last_name=""):
    ''' Checks type of first&last name if not strings'''
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is" " {} {}".format(first_name, last_name))
