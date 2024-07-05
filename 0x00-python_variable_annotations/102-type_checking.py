#!/usr/bin/env python3
"""mypy type checking module"""


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """mypy type checking module"""
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in
