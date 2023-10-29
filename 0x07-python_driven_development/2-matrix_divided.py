#!/usr/bin/python3
""" Matrix divided method. """


def matrix_divided(matrix, div):
    # Check if the matrix is a list of integers or floats
    if not all(isinstance(x, list) and
            all(isinstance(el, (int, float)) for el in x) for x in matrix):
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
    # Check if each row of matrix is of the same size
    if not all(len(rw) == len(matrix[0]) for rw in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    # Check if the div is a number (integer / float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # Check if div is not equal to zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Divide all matrix elements by div and round to 2 decimal places
    results = [[round(y / div, 2) for y in row] for row in matrix]
    return results
