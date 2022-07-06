#!/usr/bin/python3

#  a function that adds all unique integers in a list (only once for each integer)

def uniq_add(my_list=[]):
    # since we are working with unique entries we have to create a set
    sum = 0;
    for x in set(my_list):
        sum += x
    return sum
