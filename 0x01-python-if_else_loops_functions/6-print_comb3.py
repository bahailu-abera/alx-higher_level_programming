#!/usr/bin/python3

for i in range(10):
    for j in range(i+1, 10):
        print("{}{}{}".format(i, j, ", " if i != 8 else "\n"), end="")
