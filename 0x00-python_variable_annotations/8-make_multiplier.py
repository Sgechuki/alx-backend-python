#!/usr/bin/env python3
from typing import Callable
"""
Module holds make_multiplier function
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    type-annotated function make_multiplier
    that takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier
    """
    return lambda x: x * multiplier
