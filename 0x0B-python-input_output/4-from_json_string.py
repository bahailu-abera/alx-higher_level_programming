#!/usr/bin/python3
""" Module for deserilazing json to python DT """
import json


def from_json_string(my_str):
    """ Return python datastructure form json """
    return json.loads(my_str)
