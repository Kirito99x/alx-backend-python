#!/usr/bin/python3
"""length of a list of sequences module"""


from typing import Sequence, Iterable, List, Tuple


def element_length(lst: List[Sequence]) -> List[Tuple[Sequence, int]]:
    """length of a list of sequences module"""
    return [(i, len(i)) for i in lst]
