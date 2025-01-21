#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = sorted(a_dictionary)
    for keys in new_dict:
        print(f"{keys}: {a_dictionary[keys]}")
