k 2's module.

This module provides a function measure_time, which computes the average runtime of wait_n.
'''
import asyncio
import time
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
        '''
            Executes wait_random n times and returns a sorted list of wait times.

                Args:
                        n (int): The number of times to execute wait_random.
                                max_delay (int): The maximum delay in seconds.

                                    Returns:
                                            List[float]: A sorted list of wait times.
                                                '''
                                                    wait_times = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
                                                        return sorted(wait_times)


                                                    def measure_time(n: int, max_delay: int) -> float:
                                                            '''
                                                                Computes the average runtime of wait_n.

                                                                    Args:
                                                                            n (int): The number of times to execute wait_n.
                                                                                    max_delay (int): The maximum delay in seconds.

                                                                                        Returns:
                                                                                                float: The average runtime of wait_n.
                                                                                                    '''
                                                                                                        start_time = time.time()
                                                                                                            asyncio.run(wait_n(n, max_delay))
                                                                                                                return (time.time() - start_time) / n

