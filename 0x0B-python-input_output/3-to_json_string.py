#!/usr/bin/python3
""" Module for serialization of json """
import json


def to_json_string(my_obj):
    """ Return Json format of my_obj """
    return json.dumps(my_obj)
