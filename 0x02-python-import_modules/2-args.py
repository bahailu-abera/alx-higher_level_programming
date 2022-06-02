#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    length = len(argv)

    print("{} arguments{}".format(length - 1, '.' if length == 1 else ':'))

    for argnum in range(1, length):
        print("{}: {}".format(argnum, argv[argnum]))
