#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initializing the object
        Args:
            width (integer or optional): width of the rectangle
            height (integer or optional): height of the rectangle

        Raises:
            TypeError: if it is not an integer
            ValueError: if it is less than 0
        """
        self.width = width
        self.height = height

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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
