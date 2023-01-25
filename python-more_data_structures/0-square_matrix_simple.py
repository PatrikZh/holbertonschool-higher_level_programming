#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for elements in row:
            elements = elements ** 2
            new_row.append(elements)
        new_matrix.append(new_row)
    return new_matrix
