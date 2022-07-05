#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # since a tuple is immutable, we make a list out of them
    a = list(tuple_a)
    b = list(tuple_b)
    while len(b) < 2:
        b.append(0)
    while len(a) < 2:
        a.append(0)
    return (a[0] + b[0], a[1] + b[1])
