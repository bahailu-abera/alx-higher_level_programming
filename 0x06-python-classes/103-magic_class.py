#!/usr/bin/python3
import math


class MagicClass:
    def __init__(self):
        self._MagicClass__radius = 0

        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError("radius must be a number")
        else:
            self._MagicClass__radius = radius

    def area(self):
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        return 2 * math.pi * self._MagicClass__radius
