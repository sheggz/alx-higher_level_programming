#!/usr/bin/python3

#  a function that finds the biggest integer of a list.

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    # we sort the list to make sure largest is at the end
    my_list.sort()  # this sorts in place i.e doesnt return new list
    return my_list[len(my_list) - 1]
