#!/usr/bin/env python3
"""
Task 9: Let's duck type an iterable object
"""
from typing import List, Iterable, Tuple, Sequence, Union


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotate the below function’s parameters
    and return values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
