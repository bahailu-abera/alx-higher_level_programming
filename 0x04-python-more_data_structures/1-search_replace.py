#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list:
        for idx in range(len(my_list)):
            if my_list[idx] == search:
                my_list[idx] = replace
    return my_list
