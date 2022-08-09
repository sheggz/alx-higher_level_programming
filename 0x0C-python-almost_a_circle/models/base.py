#!/usr/bin/python3

"""this module houses the base class"""


class Base:
    """this is the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """this is the constructor with a default ID parameter"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
