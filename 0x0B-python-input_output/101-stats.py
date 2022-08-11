#!/usr/bin/python3
""" Module for logging parsing """
import sys


def print_pretty(size, code_dict):
    """ parse important data """
    print("File size: {}".format(size))
    for key, value in sorted(code_dict.items()):
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    """ print parsed data """
    size = 0
    code_dict = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    line_counter = 0
    try:
        for line in sys.stdin:
            line_counter += 1
            if (len(line.split()) < 2):
                continue
            code = line.split()[-2]
            size += int(line.split()[-1])
            if code in code_dict:
                code_dict[code] += 1
            if (line_counter % 10 == 0):
                print_pretty(size, code_dict)
        print_pretty(size, code_dict)
    except KeyboardInterrupt:
        print_pretty(size, code_dict)
        raise