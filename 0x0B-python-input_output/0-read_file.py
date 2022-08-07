#!/usr/bin/python3
""" Module for reading file """


def read_file(filename=""):
    """ Read file filename """
    with open(filename, 'r', encoding="utf-8") as fs:
        content = fs.read()
        if content:
            print(content.strip())
        fs.close()
