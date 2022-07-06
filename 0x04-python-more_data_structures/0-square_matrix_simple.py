#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # let's creatre a copy of the 2D array
    # idk why my first approach (commented out below) didnt work

    # localcpy = matrix.copy()
    # for i in range(len(localcpy)):
    # for j in range(len(localcpy[1])):
    # localcpy[i][j] = localcpy[i][j] ** 2
    return list(list(map((lambda x: x ** 2), item)) for item in matrix)
    # return localcpy
