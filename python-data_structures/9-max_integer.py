#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    max_list = my_list[0]
    for num in my_list:
        if num > len(my_list):
            return num
