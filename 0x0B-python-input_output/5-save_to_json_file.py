#!/usr/bin/python3
""" Module for saving object using json representation """
import json


def save_to_json_file(my_obj, filename):
    """ Save my_obj to a text file """
    with open(filename, 'w') as fs:
        json.dump(my_obj, fs)
        fs.close()
