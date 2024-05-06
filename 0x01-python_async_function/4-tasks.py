#!/usr/bin/env python3
"""
Task 4: Let's execute multiple coroutines
at the same time with async
"""
import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    async routine
    """
    result: List[float] = await asyncio.gather(
       *(task_wait_random(max_delay) for _ in range(n)))
    return sorted(result)
