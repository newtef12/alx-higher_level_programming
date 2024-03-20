#!/usr/bin/python3
"""
0-square_matrix_simple.py
"""


def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix"""
    return [[x ** 2 for x in row] for row in matrix]


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)
