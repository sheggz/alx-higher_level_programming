#!/usr/bin/python3
"""matrix_divided will divide the given matrix
by the parameter "div", and returns the divided matrix"""


def matrix_divided(matrix, div):
    """a function that divids all elements of a matrix
    and returns a new matrix
    checks if the entire list is int/float
    checks if each list in the matrix are the same size
    checks if "div" is an int/float or is 0
    """

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for x in matrix:
        if not isinstance(x, list):
            raise TypeError(msg)
        if len(matrix[0]) != len(x):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for y in x:
            if not isinstance(y, (int, float)):
                raise TypeError(msg)
            new_row.append(round(y / div, 2))
        new_matrix.append(new_row)
    return new_matrix
