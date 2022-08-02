#!/usr/bin/python3
"""test if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """this function tests if an object is an instance of a class"""

    if type(obj) == a_class:
        return True
    else:
        return False
