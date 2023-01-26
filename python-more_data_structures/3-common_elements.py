#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set()
    for element in set_1:
        if element in set_2:
            new_set.add(element)
        else:
            pass
    return new_set

# or use return set_1 & set_2 -> It will return all the same elements
