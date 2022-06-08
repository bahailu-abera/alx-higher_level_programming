#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list:
        new_list = []
        for idx in range(len(my_list)):
            if my_list[idx] == search:
                new_ist[idx] = replace
            else:
                new_list[idx] = my_list[idx]
        return new_list
