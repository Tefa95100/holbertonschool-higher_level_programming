#!/usr/bin/python3
def roman_to_int(roman_string):
    unit = 0
    if not roman_string or not isinstance(roman_string, str):
        return 0
    if roman_string.count('I') != 0 and roman_string.count('X'):
        if roman_string.index('I') + 1 == roman_string.index('X'):
            unit = -1
        else:
            unit = roman_string.count('I') * 1
    else:
        unit = roman_string.count('I') * 1
    five = roman_string.count('V') * 5
    ten = roman_string.count('X') * 10
    fifty = roman_string.count('L') * 50
    hundred = roman_string.count('C') * 100
    five_hundred = roman_string.count('D') * 500
    thousand = roman_string.count('M') * 1000
    sum = unit + five + ten + fifty + hundred + five_hundred + thousand

    return sum
