#!/usr/bin/python3
""" Module for loading from json file"""
import json


def load_from_json_file(filename):
    """ Load from json file """
    my_obj = None
    with open(filename, 'r') as fs:
        my_obj = json.load(fs)
        fs.close()
    return my_obj
