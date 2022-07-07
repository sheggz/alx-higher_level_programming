#!/usr/bin/python3

# a function that returns a new dictionary with all values multiplied by 2

def multiply_by_2(a_dictionary):
    localcpy = a_dictionary.copy()
    for i in localcpy:
        localcpy[i] = localcpy[i] * 2
    return localcpy
