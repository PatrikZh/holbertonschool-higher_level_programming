#!/usr/bin/python3
"""  Function that stores matrix in a new one divided"""


def matrix_divided(matrix, div):
    ''' Create new matrix to store rows as list and elements divided'''
    new_matrix = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
            new_row.append(round(i / div, 2))
        new_matrix.append(new_row)
    return new_matrix
