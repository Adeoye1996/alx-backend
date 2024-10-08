#!/usr/bin/env python3
""" Contains definition of index_range helper function """


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Return a tuple(start_index, end_index) """

    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)
