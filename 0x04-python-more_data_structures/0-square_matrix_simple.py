#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for b in range(len(matrix)):
        new_matrix[b] = list(map(lambda x: x**2, matrix[b]))

    return (new_matrix)
