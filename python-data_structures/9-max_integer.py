#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    for num in my_list:
        if num > len(my_list):
            return num
