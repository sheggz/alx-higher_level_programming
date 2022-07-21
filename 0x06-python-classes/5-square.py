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
    def size(self, value):
        """A setter function
        to set the private Variable with conditions

        Args:
            the size to be set
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  #: if no error is raised, set private attr

    def area(self):
        """function to compute area"""

        return (self.__size ** 2)

    def my_print(self):
        """A function that prints the square using '#'"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
