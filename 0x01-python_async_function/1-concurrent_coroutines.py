#!/usr/env python3
wait_random = __import__("0-basic_async_syntax").wait_random
import asyncio


async def wait_n(n, max_delay):
    result = await asyncio.gather(*[wait_random(max_delay) for _ in range(n + 1)])
    return result
