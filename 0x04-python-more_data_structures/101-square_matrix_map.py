#!/usr/bin/python3
"""101-square_matrix_map.py"""


def square_matrix_map(matrix=[]):
    """Computes the square value of all integers of a matrix using map"""
    return list(map(lambda row: list(map(lambda x: x * x, row)), matrix))
