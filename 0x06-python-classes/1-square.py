#!/usr/bin/python3
"""This module implents some of the Class basics

"""


class Square:
    """A Class to implement a square
    """
    def __init__(self, size):
        """Initialize the size attribute

        Args:
            size (int): the size of the square
        """

        self.__size = size  #: private size attribute
