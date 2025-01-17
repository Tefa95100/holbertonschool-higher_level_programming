#!/usr/bin/python3

def remove_char_at(str, n):
    str_cpy = str + ''

    if n < len(str_cpy):
        str_cpy = str_cpy.replace(str_cpy[n], '')
    return str_cpy
