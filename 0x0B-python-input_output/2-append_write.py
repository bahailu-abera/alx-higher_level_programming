#!/usr/bin/python3
""" Module to append text to file """


def append_write(filename="", text=""):
    """ Append text to file filename """
    with open(filename, 'a') as fs:
        fs.write(text)
        fs.close()
    return len(text)
