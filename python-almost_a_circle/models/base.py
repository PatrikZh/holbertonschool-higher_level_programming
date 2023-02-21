#!/usr/bin/python3
""" Class called Base"""


import json
import os

class Base:
    ''' Init function that has two conditions, if id exists or not'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' JSON string representation of list_dictionaries .dumps() func'''
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' Method writes JSON string representation of list_objs to a file'''
        filename = cls.__name__ + ".json"
        empty_list = []
        if list_objs is not None:
            for obj in list_objs:
                empty_list.append(obj.to_dictionary())

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(empty_list))

    @staticmethod
    def from_json_string(json_string):
        ''' json_string is a string representing a list of dictionaries'''
        empty_list = []
        if json_string is None:
            return empty_list
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' Method that returns an instance with all attributes already set'''
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        ''' Method that returns a list of instances'''
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                json_string = f.read()
                list_of_dicts = cls.from_json_string(json_string)
                list_of_instances = []
                for d in list_of_dicts:
                    instance = cls.create(**d)
                    list_of_instances.append(instance)
                return list_of_instances
        else:
            return []
