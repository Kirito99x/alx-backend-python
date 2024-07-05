#!/usr/bin/env python3
"""augmenting the code with the correct type annotations"""


from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Augment the code with the correct type annotations"""
    if lst:
        return lst[0]
    else:
        return None
