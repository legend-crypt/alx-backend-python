#!/usr/env python3
"""import asyncio"""
wait_random = __import__("0-basic_async_syntax").wait_random
import asyncio


async def wait_n(n, max_delay):
    """Wait and return the delay"""
    result = await asyncio.gather(*[wait_random(max_delay) for _ in range(n + 1)])
    result.sort()
    return result
