#!/usr/bin/python3
"""
7-update_dictionary.py
"""


def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary"""
    a_dictionary[key] = value
    return a_dictionary


if __name__ == "__main__":
    update_dictionary(a_dictionary, 'language', "Python")
