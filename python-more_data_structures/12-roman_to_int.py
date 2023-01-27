#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i in range(len(roman_string)):
        if roman_string[i] in roman_dictionary:
            current_value = roman_dictionary[roman_string[i]]
        if i < len(roman_string) - 1:
            next_value = roman_dictionary[roman_string[i + 1]]
            if current_value < next_value:
                total -= current_value
            else:
                total += current_value
        else:
            total += current_value
    return total
