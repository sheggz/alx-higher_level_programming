#!/usr/bin/python3
"""This module implents some of the Class basics

"""


class Square:
    """A Class to implement a square
    """
    def __init__(self, size=0):
        """Initialize the size attribute

        Args:
            size (int): the size of the square
        """

        self.size = size  #: call the setter property fn

        @property
        def size(self):
            """Create a getter

            This will be used for accessing the private element
            """
            return self.__size

        @size.setter
        def size(self, size):
            """A setter function
            to set the private Variable with conditions

            Args:
                the size to be set
            """

            if type(size) is not int:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size  #: if no error is raised, set private attr
