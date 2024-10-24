#!/usr/bin/env python3
"""import asyncio"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Wait and return the delay"""
    result = await asyncio.gather(*[wait_random(max_delay) for _ in range(n + 1)])
    result.sort()
    return result
