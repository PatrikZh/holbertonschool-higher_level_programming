#!/usr/bin/python3
def uniq_add(my_list=[]):
    seen = set()
    total = 0
    for num in my_list:
        if num not in seen:
            seen.add(num)
            total += num
    return total

# You can also do it another way and faster mehtod: return sum(set(my_list) -> which finds the sum of the set list of my_list
