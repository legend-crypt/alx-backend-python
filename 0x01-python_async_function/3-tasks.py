#!/usr/bin/env python3
"""Imported wait_random"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay):
    """Create a function that create task wait for random"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
