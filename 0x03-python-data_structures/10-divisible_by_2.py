#!/usr/bin/python3

# a function that finds all multiples of 2 in a list.

def divisible_by_2(my_list=[]):
    if len(my_list) > 0:
        boollist = []
        for x in my_list:
            if x % 2 == 0:
                boollist.append(True)
            else:
                boollist.append(False)
        return boollist
