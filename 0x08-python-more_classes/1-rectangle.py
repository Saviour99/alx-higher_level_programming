#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, height=0, width=0):
        """Initializing the object
        Args:
            width (integer or optional): width of the rectangle
            height (integer or optional): height of the rectangle

        Raises:
            TypeError: if it is not an integer
            ValueError: if it is less than 0
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get width"""
        return self.__width

    @property
    def height(self):
        """get height"""
        return self.__height

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        elif self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
