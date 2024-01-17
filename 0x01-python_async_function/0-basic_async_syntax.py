#!/usr/bin/env python3
'''
Task 0's module.

This module provides an asynchronous function wait_random,
which waits for a random number of seconds.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
        '''
            Asynchronous function to simulate a random delay.

                Args:
                        max_delay (int): The maximum delay in seconds. Default is 10.

                            Returns:
                                    float: The generated random wait time.
                                        '''
                                            wait_time = random.random() * max_delay
                                                await asyncio.sleep(wait_time)
                                                    return wait_time

