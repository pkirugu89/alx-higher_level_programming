#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # create a new matrix to store the squared values
    sq_matrix = []
    # Iterate through the rows in the input matrix
    for rw in matrix:
        # create a new row for the squared values
        sq_rw = []
        # iterate through the elements of the current row
        for element in rw:
            # square the elements and append to the squares row
            sq_rw.append(element ** 2)
        # Append the squared row to the sq_matrix
        sq_matrix.append(sq_rw)
    # Return sq_matrix
    return sq_matrix
