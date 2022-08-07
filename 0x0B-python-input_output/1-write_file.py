#!/usr/bin/python3
""" Module for writing  to a file """


def write_file(filename="", text=""):
    """ Write text to the file filename """
    with open(filename, 'w') as fs:
        fs.write(text)
        fs.close()
    return len(text)
