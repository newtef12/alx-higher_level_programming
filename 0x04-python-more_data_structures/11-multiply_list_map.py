#!/usr/bin/python3
"""11-multiply_list_map.py"""

def multiply_list_map(my_list=[], number=0):
    """Returns a new list with all values multiplied by a number using map"""
    return list(map(lambda x: x * number, my_list))
