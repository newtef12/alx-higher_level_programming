#!/usr/bin/python3
"""
5-number_keys.py
"""


def number_keys(a_dictionary):
    """Returns the number of keys in a dictionary"""
    return len(a_dictionary)


if __name__ == "__main__":
    a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
    nb_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(nb_keys))
