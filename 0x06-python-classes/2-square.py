#!/usr/bin/python3
"""A Square Module"""


class Square:
    """A Square Class"""
    def __init__(self, size=0):
        """Initializing the object
        Args:
            size (int, optional): size of a square.

        Raises;
            TypeError: If the is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
