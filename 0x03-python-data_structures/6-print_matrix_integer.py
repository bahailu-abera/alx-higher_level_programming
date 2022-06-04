#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        last_indx = len(matrix[i])
        for j in range(last_indx):
            print("{:d}{}".format(matrix[i][j], " "
                                  if j != last_indx - 1 else ""), end="")
        print()
