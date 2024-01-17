#!/usr/bin/env python3
'''
Task 3's module.

This module provides a function task_wait_random, which creates an asynchronous task for wait_random.
'''
import asyncio


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

