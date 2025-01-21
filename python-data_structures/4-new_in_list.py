#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_list = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        cpy_list.pop(idx)
        cpy_list.insert(idx, element)
        return cpy_list
