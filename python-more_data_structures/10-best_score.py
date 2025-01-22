#!/usr/bin/python3
def best_score(a_dictionary):
    best_value = 0
    best_key = []
    if not a_dictionary:
        return None
    for key in a_dictionary:
        if best_value < a_dictionary[key]:
            best_value = a_dictionary[key]
            best_key = key
    return best_key
