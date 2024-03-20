#!/usr/bin/python3
"""
8-simple_delete.py
"""


def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary"""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary


if __name__ == "__main__":
    a_dictionary = {'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3]}
    new_dict = simple_delete(a_dictionary.copy(), 'track')
    for key, value in a_dictionary.items():
        print("{}: {}".format(key, value))
    print("--")
    for key, value in new_dict.items():
        print("{}: {}".format(key, value))
    print("--")
    print("--")
    new_dict = simple_delete(a_dictionary.copy(), 'c_is_fun')
    for key, value in a_dictionary.items():
        print("{}: {}".format(key, value))
    print("--")
    for key, value in new_dict.items():
        print("{}: {}".format(key, value)))
