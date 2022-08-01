#!/usr/bin/python3
""" Module for Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square classs
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Returns the size of the square """
        return self.__size * self.__size
