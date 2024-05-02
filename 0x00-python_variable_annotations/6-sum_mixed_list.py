#!/usr/bin/env python3
from typing import List, Union
"""
Module contains sum_mixed_list function
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    type-annotated function sum_mixed_list which
    takes a list mxd_lst of integers and floats
    and returns their sum as a float
    """
    total: float = 0
    for i in mxd_lst:
        total += i
    return total
