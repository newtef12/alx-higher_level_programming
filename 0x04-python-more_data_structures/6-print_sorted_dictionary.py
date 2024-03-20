#!/usr/bin/python3
"""
6-print_sorted_dictionary.py
"""


def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""
    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))


if __name__ == "__main__":
    a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3]}
    print_sorted_dictionary(a_dictionary)
