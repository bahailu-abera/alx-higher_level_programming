#!/usr/bin/python3

i = 0

for asc in range(122, 96, -1):
    if (i == 0):
        print("{:c}".format(asc), end="")
        i = 1
    else:
        print("{:c}".format(asc - 32), end="")
        i = 0
