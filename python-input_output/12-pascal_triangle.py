#!/usr/bin/python3
""" Pascal triangle format build beneath"""


def pascal_triangle(n):
    ''' Making an pascal triangle'''
    triangle = []
    for i in range(n):
        row = [1]
        prev_row = []
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)
        triangle.append(row)
    return triangle
