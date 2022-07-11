#!/usr/bin/python3
""" Module for the Square Object """
from models.rectangle import Rectangle


class Square(Rectangle):
    """  The class Square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Returns the size of the square """
        return self.width
    @size.setter
    def size(self, value):
        """ Sets the size of the square """
        self.width = value
        self.height = value

    def __str__(self):
        """ Return the string representation of Square """
        result = ("[Square] ({}) {}/{} - {}").\
            format(self.id, self.x, self.y, self.width)
        return result
