#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        if isinstance(row, list):
            temp = []
            for col in row:
                temp.append(col ** 2)
            new_matrix.append(temp)
        else:
            new_matrix.append(row ** 2)
    return new_matrix
