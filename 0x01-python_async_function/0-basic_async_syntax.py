#!/usr/bin/env python3
"""import asyncio
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait and return the delay

    Args:
        max_delay (int, optional): max delay. Defaults to 10.

    Returns:
        float: delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
