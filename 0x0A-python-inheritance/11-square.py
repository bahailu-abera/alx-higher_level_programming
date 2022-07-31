#!/usr/bin/python3
""" Module for Square """
from 9-rectangle import Rectangle


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

    def __str__(self):
        """ Returns the string representation """
        return "[Square] {}/{}".format(self.__size, self.__size)
