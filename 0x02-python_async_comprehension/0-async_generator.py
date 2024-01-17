sk 0 module.

This module defines an asynchronous generator function that yields a sequence
of 10 random floating-point numbers between 0 and 10.
'''

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
        '''Generate a sequence of 10 random numbers.

            Yields:
                        float: A random floating-point number between 0 and 10.
                            '''
                                for _ in range(10):
                                        await asyncio.sleep(1)
                                                yield random.uniform(0, 10)

