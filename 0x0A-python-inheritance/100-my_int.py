#!/usr/bin/python3
""" Module for MyInt """


class MyInt(int):
    def __eq__(self, __x):
        return not super().__eq__(__x)
