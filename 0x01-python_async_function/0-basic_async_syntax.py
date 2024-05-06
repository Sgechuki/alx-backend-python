#!/usr/bin/env python3
"""
Task 0: The basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine
    """
    i: float = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
