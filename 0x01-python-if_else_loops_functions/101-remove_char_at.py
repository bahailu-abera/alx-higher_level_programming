#!/usr/bin/python3

def remove_char_at(str, n):
    string = str()
    for i in range(len(str)):
        if (i != n):
            string += str[i]
    return string
