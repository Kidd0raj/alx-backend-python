#!/usr/bin/env python3

'''Task 12's module.
'''
from typing import List, Tuple, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> List[Any]:
    '''Creates multiple copies of items in a tuple.'''
    zoomed_in: List[Any] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3)
