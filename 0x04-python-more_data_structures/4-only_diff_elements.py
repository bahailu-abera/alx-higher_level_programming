#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diff = set()
    if set_1 and set_2:
        diff = (set_1 - set_2) | (set_2 - set_1)

    return diff
