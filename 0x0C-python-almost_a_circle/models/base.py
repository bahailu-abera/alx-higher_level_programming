#!/usr/bin/python3
""" The base of all other classes in this project. """
import json


class Base:
    """ Object to manage id attribute in all other classes
    and to avoid duplicating the same code.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        filename = "{}.json".format(cls.__name__)
        list_dict = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())

        lst = cls.to_json_string(list_dict)

        with open(filename, 'w') as fs:
            fs.write(lst)
            fs.close()
