#!/usr/bin/python3
""" Module for writing  to a file """


def write_file(filename="", text=""):
    """ Write text to the file filename """
    with open(filename, 'w', encoding="utf-8") as fs:
        fs.write(text)
    return len(text)
