#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        if x >= 0:
            for i in range(x):
                print(my_list[i], end="")
                count+=
            return count
    except IndexError:
        pass
    return count

        
