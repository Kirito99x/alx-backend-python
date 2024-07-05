#!/usr/bin/python3
"""type-annotated function to_kv module"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """type-annotated function to_kv module"""
    return (k, float(v * v))
