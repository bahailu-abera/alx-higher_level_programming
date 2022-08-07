#!/usr/bin/python3
""" Module for reading file """


def read_file(filename=""):
    """ Read file filename """
    with open(filename, 'r', encoding="utf-8") as fs:
        for line in fs:
            print(line, end="")
