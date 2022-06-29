#!/usr/bin/python3
for x in range(100):
    if x < 99:
        print("{:02}, ".format(x), end="")
    elif x == 99:
        print("{:02d}".format(x))  ''' i'm not changing the end since
        last mumber should be follwed by new line'''
