#!/usr/bin/python3
"""Rectangle inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle data inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """the constructor"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__height = height
        self.__width = width
