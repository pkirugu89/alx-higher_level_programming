#!/usr/bin/python3
""" Matrix divided method. """


def matrix_divided(matrix, div):
    """
    Method that returns a new matrix.
    The result of the matrix division by div
    rounded to 2 decimal places.
    """
    # Check if the matrix is a list of integers or floats
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

    row_len = []
    for row in matrix:
        row_len.append(len(row))
    if not all(el == row_len[0] for el in row_len):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    nw_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return nw_matrix
