#!/usr/bin/python3

# a function that replaces an element in a list at a specific position without
# modifying the original list (like in C).

def new_in_list(my_list, idx, element):
    # make a copy of the list and assign to same variable
    my_list = list(my_list)
    # test if index is valid
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return my_list
