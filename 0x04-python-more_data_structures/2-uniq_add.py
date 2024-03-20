#!/usr/bin/python3
"""
2-uniq_add.py
"""


def uniq_add(my_list=[]):
    """Adds all unique integers in a list"""
    unique_numbers = set(my_list)
    return sum(unique_numbers)


if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
