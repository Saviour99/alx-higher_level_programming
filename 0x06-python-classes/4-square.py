#!/usr/bin/python3
"""A Square Module"""


class Square:
    """A Square Class"""
    def __init__(self, size=0):
        """Initializing the object"""
        self.__size = size

    @property
    def size(self):
        """Getter function"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of a square"""
        return self.__size ** 2
