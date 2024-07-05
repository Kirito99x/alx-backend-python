#!/usr/bin/env python3
"""multiplier function module"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplier function module"""
    return lambda x: x * multiplier
