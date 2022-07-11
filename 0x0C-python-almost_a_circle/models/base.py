#!/usr/bin/python3
""" The base of all other classes in this project. """
import json

class Base:
    """ Object to manage id attribute in all other classes
    and to avoid duplicating the same code.
    """
    __nb_objects = 0

    def save_to_file(__class__Base, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        filename = str(cls) + ".json"

        with open(filename, 'w') as fs:
            if list_objs is None:
                fs.write("[]")
            else:
                fs.write(to_json_string(list_objs))
            fs.close()

    def __init__(self, id=None):
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    # def save_to_file(cls, list_objs):
    #     """ Writes the JSON string representation of list_objs to a file """
    #     filename = str(cls) + ".json"

    #     with open(filename, 'w') as fs:
    #         if list_objs is None:
    #             fs.write("[]")
    #         else:
    #             fs.write(to_json_string(list_objs))
    #         fs.close()
