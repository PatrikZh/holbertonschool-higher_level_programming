#!/usr/bin/python3
def uppercase(str):
    new_string = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 123:
            a = ord(i) - 32
            new_string += chr(a)
        else:
            new_string += i
    print(new_string)
