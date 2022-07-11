#!/usr/bin/python3
""" Module for the Square Object """
from models.rectangle import Rectangle


class Square(Rectangle):
    """  The class Square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Return the string representation of Square """
        result = ("[Square] ({}) {}/{} - {}").\
            format(self.id, self.x, self.y, self.width)
        return result
