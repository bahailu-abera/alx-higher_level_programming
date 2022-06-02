#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv

    print("{} arguments.".format(len(argv) - 1))

    for argnum in range(1, len(argv)):
        print("{}: {}".format(argnum, argv[argnum]))
