#!/usr/bin/python3
"""100-weight_average.py"""


def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple"""
    if not my_list:
        return 0
    weighted_sum = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)
    return weighted_sum / total_weight
