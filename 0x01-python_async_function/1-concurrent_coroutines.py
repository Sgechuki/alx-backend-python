#!/usr/bin/env python3
"""
Task 1: Let's execute multiple coroutines
at the same time with async
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    async routine
    """
    result: List[float] = await asyncio.gather(
       *(wait_random(max_delay) for _ in range(n)))
    return sorted(result)
