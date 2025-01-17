#!/usr/bin/python3

def remove_char_at(str, n):
    str_cpy = str + ''
    if n < 0:
        return str_cpy
    elif n < len(str_cpy):
        str_cpy = str_cpy.replace(str_cpy[n], '')
    return str_cpy
