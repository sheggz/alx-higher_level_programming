#!/usr/bin/python3
"""this module contains a function to add ONLY intergers"""

def add_integer(a, b=98):
    """Checks if not int, otherwise return sum"""
    if type(a) is float:
        a = int(a) #convert to int
    if type(b) is float:
        b = int(b) #convert to int
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b,int):
        raise TypeError("b must be an integer")
    return a + b
