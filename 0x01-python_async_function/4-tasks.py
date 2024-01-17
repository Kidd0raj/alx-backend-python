#!/usr/bin/env python3
'''
Task 4's module.

This module provides an asynchronous function task_wait_n,
which executes task_wait_random n times and returns a sorted list of wait times.
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


                                            def task_wait_random(max_delay: int) -> asyncio.Task:
                                                    '''
                                                        Creates an asynchronous task for wait_random.

                                                            Args:
                                                                    max_delay (int): The maximum delay in seconds.

                                                                        Returns:
                                                                                asyncio.Task: An asynchronous task for wait_random.
                                                                                    '''
                                                                                        return asyncio.create_task(wait_random(max_delay))


                                                                                    async def task_wait_n(n: int, max_delay: int) -> List[float]:
                                                                                            '''
                                                                                                Executes task_wait_random n times and returns a sorted list of wait times.

                                                                                                    Args:
                                                                                                            n (int): The number of times to execute task_wait_random.
                                                                                                                    max_delay (int): The maximum delay in seconds.

                                                                                                                        Returns:
                                                                                                                                List[float]: A sorted list of wait times.
                                                                                                                                    '''
                                                                                                                                        wait_times = await asyncio.gather(*[task_wait_random(max_delay) for _ in range(n)])
                                                                                                                                            return sorted(wait_times)

