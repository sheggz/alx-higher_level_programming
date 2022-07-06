#!/usr/bin/python3
# a func that replaces all occurrences of an element by another in a new list.

def search_replace(my_list, search, replace):
    localcpy = my_list.copy()
    # i'm using a loop because list.index() will only return the index of 1st
    # occurence of the search parameter
    for x in localcpy:
        if x == search:
            localcpy[localcpy.index(search)] = replace
    return localcpy
