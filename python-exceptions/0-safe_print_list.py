#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x): # This loop is useful to repeat a certain action a specific number of times
            print(my_list[i], end="")
            count += 1
        print()
    except:
        return count
    return count
