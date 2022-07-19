#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        if x >= 0:
            for i in range(x - 1):
                print(my_list[i], end="")
                count += 1
            # print last entry with a new line after
            print(my_list[x-1])
            count += 1
            return count
    except IndexError:
        print()
    return count
