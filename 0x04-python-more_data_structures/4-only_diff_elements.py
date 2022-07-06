#!/usr/bin/python3

# a function that returns a set of all elements present in only one set
# i.e letters in a or be but not in both

def only_diff_elements(set_1, set_2):
    return set(set_1) ^ set(set_2)
