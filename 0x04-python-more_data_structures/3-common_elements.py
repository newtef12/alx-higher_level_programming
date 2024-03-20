#!/usr/bin/python3
"""
3-common_elements.py
"""


def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets"""
    return set_1.intersection(set_2)


if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))
