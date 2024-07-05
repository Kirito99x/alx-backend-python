#!/usr/bin/python3
"""sum of a mixed list"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum of a mixed list"""
    return float(sum(mxd_lst))
