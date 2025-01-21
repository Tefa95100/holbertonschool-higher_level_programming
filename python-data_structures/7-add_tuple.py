#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    not_two = 0
    while len(tuple_a) < 2 or len(tuple_b) < 2:
        if len(tuple_a) < 2:
            tuple_a += (not_two,)
        if len(tuple_b) < 2:
            tuple_b += (not_two,)

    tuple_add = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return tuple_add
