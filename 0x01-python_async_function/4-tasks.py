#!/usr/env python3
"""import asyncio"""
wait_random = __import__("3-tasks").task_wait_random
import asyncio


async def task_wait_n(n, max_delay):
    """Wait and return the delay"""
    result = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    result.sort()
    return result
