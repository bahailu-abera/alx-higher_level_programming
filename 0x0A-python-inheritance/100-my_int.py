#!/usr/bin/python3
""" Module for MyInt """


class MyInt(int):
    """ Custom int class """
    def __eq__(self, __x):
        return not super().__eq__(__x)

    def __ne__(self, __x):
        return not super().__ne__(__x)
