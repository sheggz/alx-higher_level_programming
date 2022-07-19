#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    counted = 0

    for elem in range(x):
        try:
            # if type(my_list[elem]) is int:
            print("{:d}".format(my_list[elem]), end="")
            counted += 1
            # else:
            # continue
        except (ValueError, TypeError):
            continue
    print()
    return counted
