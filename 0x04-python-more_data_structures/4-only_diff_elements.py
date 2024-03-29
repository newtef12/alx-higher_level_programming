#!/usr/bin/python3
"""
4-only_diff_elements.py
"""


def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set"""
    return set_1.symmetric_difference(set_2)


if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set)))
