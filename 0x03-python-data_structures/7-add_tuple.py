#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # If the tuples are smaller than 2, use 0 for each missing integer
    if len(tuple_a) < 2:
        tuple_a += (0, ) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0, ) * (2 - len(tuple_b))

    # Use only the first 2 integers if the tuples are bigger than 2
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]

    # Add the elements of the tuples
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
