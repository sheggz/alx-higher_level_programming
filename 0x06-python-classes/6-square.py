#!/usr/bin/python3
"""This module implents some of the Class basics

"""


class Square:
    """A Class to implement a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the size attribute

        Args:
            size (int): the size of the square
        """

        self.size = size  #: call the setter property fn
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """function to set the value of the private position attribute"""
        msg = "position must be a tuple of 2 positive integers"
        if type(value) is tuple and len(value) == 2:
            if type(value[0]) is int and type(value[1]) is int:
                self.__position = value
            else:
                raise TypeError(msg)
        else:
            raise TypeError(msg)

    def area(self):
        """function to compute area"""
        return (self.__size ** 2)

    def my_print(self):
        """A function that prints the square using '#'"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("".join([" " * self.__position[0], "#" * self.__size]))
