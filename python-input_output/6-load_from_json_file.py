#!/usr/bin/python3
""" Function that creates an Object from a “JSON file”"""


import json


def load_from_json_file(filename):
    '''.loads() function returns object that was created from JSON data'''
    with open(filename, "r", encoding="utf-8") as f:
        read_file = f.read()
        return json.loads(read_file)
