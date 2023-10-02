#!/usr/bin/python3
"""
Module matrix_divided.
Divides each element of a matrix of numbers by a number
Returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    Method that returns a new matrix.
    The result of the division of matrix by div
    rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or len(matrix) == 0 \
            or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
    for rw in matrix:
        if len(rw) == 0:
            raise TypeError("matrix must be a matrix (list of lists)\
                    of integers/floats")
        for r in rw:
            if type(r) is not int and type(r) is not float:
                raise TypeError("matrix must be a matrix (list of lists)\
                        of integers/floats")

    rw_len = []
    for row in matrix:
        rw_len.append(len(row))
    if not all(element == rw_len[0] for element in rw_len):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
