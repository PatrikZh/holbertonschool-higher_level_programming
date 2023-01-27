#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_key = None
    max_value = None
    for key, value in a_dictionary.items():
        if max_key is None or value > max_value:
            max_key = key:
            max_value = value
    return max_key
