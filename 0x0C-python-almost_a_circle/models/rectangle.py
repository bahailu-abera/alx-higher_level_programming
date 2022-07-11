#!/usr/bin/python3
""" rectangle.py """


class Rectangle(Base):
    """ The class Rectangle that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Returns the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the new for the width of the rectangle """
        self.__width = value

    @property
    def height(self):
        """ Returns the height of the rectangle """
        return self.__height
    @height.setter
    def height(self, value):
        """ Sets the new value for the height of rectangle """
        self.__height = value

    @property
    def x(self):
        """ Returns the x coordinates of the rectangle """
        return self.__x

    @width.setter
    def x(self, value):
        """ Sets the new for the x coordinates of the rectangle """
        self.__x = value

    @property
    def y(self):
        """ Returns the y coordinates of the rectangle """
        return self.__y
    @height.setter
    def y(self, value):
        """ Sets the new value for the y coordinates of rectangle """
        self.__y = value
