#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            element = element ** 2 
            new_row.append(element)
        new_matrix.append(new_row)
    return new_matrix



    # Another way to do it is :
# new_matrix = [[value ** 2 for value in row] for row in matrix]
# return new_matrix

