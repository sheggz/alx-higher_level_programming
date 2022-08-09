#!/usr/bin/python3
"""..."""

from models.base import Base

class Rectangle(Base):
    """..."""

    __nb_objects = 0
    def __init__(self, width, height, x=0, y=0, id=None):
        """..."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y =y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return self.__height * self.__width

    def display(self):
        print("\n" * self.__y, end="")
        for x in range(self.__height):
            print(" " * self.__y, "#" * self.__width)
    def __repr__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """..."""

        arg_num = len(args)
        if arg_num > 5:
            arg_num = 5
        attr = ['id', 'width', 'height', 'x', 'y']
        if arg_num > 0:
        # if it is less than 5, we update what was provided
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        # to skip kwargs of args is present, we use "else"
        elif len(kwargs) > 0:
            for key, val in kwargs.items():
                if key in attr:
                    setattr(self, key, val)

