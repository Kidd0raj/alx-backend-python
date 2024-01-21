import time
from 1-concurrent_coroutines import wait_n

def measure_time(n: int, max_delay: int) -> float:
    '''
    Measure Time Function: Measures the total execution time for wait_n(n, max_delay).

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds for each wait_random call.

    Returns:
        float: Average execution time per call.
    '''
    start_time = time.time()

    # Using asyncio.run to run the asynchronous function within a synchronous context
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
