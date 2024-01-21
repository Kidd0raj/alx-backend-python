import asyncio
from 1-concurrent_coroutines import task_wait_random  

async def task_wait_n(n: int, max_delay: int) -> None:
    '''
    Asynchronous Coroutine: Spawns task_wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay in seconds for each task_wait_random call.
    '''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    await asyncio.gather(*tasks)
