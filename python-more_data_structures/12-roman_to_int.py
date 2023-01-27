#!/usr/bin/python3
def roman_to_int(roman_string):
    first_dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i in range(len(roman_string)):
        if roman_string[i] in first_dictionary:
            total += first_dictionary[roman_string[i]]
    return total
