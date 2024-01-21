import asyncio
from 0-basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Regular Function: Converts wait_random coroutine into an asyncio.Task.

    Args:
        max_delay (int): Maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: Task representing the execution of wait_random.
    '''
    return asyncio.ensure_future(wait_random(max_delay))
