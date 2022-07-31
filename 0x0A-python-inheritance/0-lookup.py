#!/usr/bin/python3
""" Module for lookup available attributes of an object
"""


def lookup(obj):
    """ Return a list of available attributes
    """
    return dir(obj)
