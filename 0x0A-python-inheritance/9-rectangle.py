#!/usr/bin/python3
""" Module for Rectangle """
from 7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Returns the string representation of rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height))
