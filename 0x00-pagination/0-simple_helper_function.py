#!/usr/bin/env python3
"""
Write a function named index_range that takes two integer
arguments page and page_size.

The function should return a tuple of size two containing a
start index and an end index corresponding to the range of indexes
to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple containing the range of items on a page
    Args:
        page (int): page number
        page_size (int): number of elements per page
    Returns:
        (tuple): range of items
    """
    page_x_page_size: int = page * page_size
    return (page_x_page_size - page_size, page_x_page_size)
