#!/usr/bin/python3
""" Module for reading file """


def read_file(filename=""):
    """ Read file filename """
    with open(filename, 'r') as fs:
        content = fs.read()
        print(content.strip())
        fs.close()
