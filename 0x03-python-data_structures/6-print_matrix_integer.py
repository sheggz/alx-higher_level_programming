#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    column, row = len(matrix[0]), len(matrix)
    if column >= 1:
        for i in range(row):
            for j in range(column):
                if j == column - 1:
                    print("{:d}".format(matrix[i][j]))
                else:
                    print("{:d}".format(matrix[i][j]), end=" ")
    else:
        print("".format())
