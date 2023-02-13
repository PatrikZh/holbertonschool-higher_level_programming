#!/usr/bin/python3
""" Function uses with statement and then converts to JSON"""


import json


def save_to_json_file(my_obj, filename):
    ''' Write authority to f and then convert to json file format'''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
