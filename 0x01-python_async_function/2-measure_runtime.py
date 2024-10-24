#!/usr/bin/env python3

"""Measure the runtime"""

import time
import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure Execution time

    Args:
        n (int): n times
        max_delay (int): max delay
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - start) / n
