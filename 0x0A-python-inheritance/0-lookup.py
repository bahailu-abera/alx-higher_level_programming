#!/usr/bin/python3
""" Module for lookup available attributes of an object
"""


def lookup(obj):
    """ Return a list of available attributes
    """
    attributes = []
    for attr in obj.__slots__:
        attributes.append(attr)

    return attributes
