#!/usr/bin/env python3
"""
Task 0: Async Generator
"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    coroutine will loop 10 times
    each time asynchronously wait 1 second
    then yield a random number
    """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
