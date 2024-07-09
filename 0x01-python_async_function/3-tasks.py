#!/usr/bin/env python3
'''TASK WAIT RANDOM'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''build an asynchronous task for wait_random.'''
    return asyncio.create_task(wait_random(max_delay))
