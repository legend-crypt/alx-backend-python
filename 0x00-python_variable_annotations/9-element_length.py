from typing import Iterable, Sequence, List, Tuple

"""No Module imported"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function element_length that takes a list of strings lst as argument"""
    return [(i, len(i)) for i in lst]
