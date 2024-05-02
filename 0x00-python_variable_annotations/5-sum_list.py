#!/usr/bin/env python3
from typing import List

"""
Module holds sum_list function
"""


def sum_list(input_list: List[float]) -> float:
    """
    type-annotated function sum_list which
    takes a list input_list of floats as
    argument and returns their sum as a float
    """
    total: float = 0.0
    for i in input_list:
        total += i
    return total
