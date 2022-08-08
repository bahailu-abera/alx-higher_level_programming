#!/usr/bin/python3
""" Module for serialzing class to json """


def class_to_json(obj):
    """ Returns the dictionary description with simple data structure """
    my_dict = obj.__dict__
    return my_dict
