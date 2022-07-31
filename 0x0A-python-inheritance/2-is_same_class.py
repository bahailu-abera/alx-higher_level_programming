#!/usr/bin/python3
""" Module to check exact isntance of class """


def is_same_class(obj, a_class):
    """ Return True if obj id instance of a_class
    or False if not
    """
    return obj.__class__ == a_class().__class__
