#!/usr/bin/python3
"""Function to test for subclass"""


def is_kind_of_class(obj, a_class):
    """this is a function that returns True if obj isinstance of,
    or if the object is an instance of a class that inherited
    from, the specified class; otherwise False"""

    if isinstance(obj, a_class) is not False:
        return True
    else:
        return False
