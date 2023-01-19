#!/usr/bin/python3

my_string = ['denio', 'patrik', 'vivian']
upper_list = []
for i in reversed(range(len(my_string))):
    upper_list.append(str.upper(my_string))

print(upper_list)
# ['VIVIAN', 'PATRIK', 'DENIO']
# [0:0:0]
