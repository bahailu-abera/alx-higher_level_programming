#!/usr/bin/python3

def uppercase(str):

    for let in str:
        if 'a' < let < 'z':
            let = ord(let) - 32
        print("{:c}".format(let), end="")
