#!/usr/bin/python3
"""A Square Module"""


class Square:
    """A Square Class"""
    def __init__(self, size=0):
        """Initializing the object
        Args:
            size (int, optional): size of a square.

        Raises:
            TypeError: If it is not an integer.
            ValueError: If it is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the Area of a square"""
        return self.__size ** 2
