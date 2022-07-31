#!/usr/bin/python3
""" Module for my_list object """


class MyList(list):
    """ Object representation of MyList """
    def print_sorted(self):
        """ Sorts a list in ascending order """
        new = []
        if not self or len(self) <= 0:
            pass
        else:
            new = self[:]

        print(sorted(new))
