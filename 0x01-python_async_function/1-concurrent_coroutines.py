k 1's module.

This module provides an asynchronous function wait_n,
which executes wait_random n times and returns a sorted list of wait times.
'''
import asyncio
from typing import List
from random import random


async def wait_random(max_delay: int) -> float:
        '''
            Asynchronous function to simulate a random delay.

                Args:
                        max_delay (int): The maximum delay in seconds.

                            Returns:
                                    float: The generated random wait time.
                                        '''
                                            await asyncio.sleep(random() * max_delay)
                                                return max_delay


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

