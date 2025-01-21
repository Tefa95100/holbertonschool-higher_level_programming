#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    new_list = my_list.copy()
    while new_list.count(search) != 0:
        position = new_list.index(search)
        new_list[position] = replace
    return new_list
