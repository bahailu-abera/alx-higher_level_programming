#!/usr/bin/python3
""" Module for Rectangle """


class Rectangle:
    """ A class representation of rectangle
    """
    def __init__(self, width=0, height=0):
        """ Instantiation method """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """ Returns the value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Returns the value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Computes and returns the area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Computes and returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Prints the rectangle """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            string += "#" * self.__width

            if i != self.__height - 1:
                string += "\n"

        return string
