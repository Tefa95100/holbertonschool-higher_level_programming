#!/usr/bin/python3
def roman_to_int(roman_string):
    value = 0
    prev_value = 0
    result = 0
    roman_number = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

    if not roman_string or not isinstance(roman_string, str):
        return 0

    for char in reversed(roman_string):
        value = roman_number.get(char, 0)
        if value < prev_value:
            result -= value
        else:
            result += value
            prev_value = value

    return result
