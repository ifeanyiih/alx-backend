#!/usr/bin/env python3
"""
Write a function named index_range that takes two integer
arguments page and page_size.

The function should return a tuple of size two containing a
start index and an end index corresponding to the range of indexes
to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""
import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a list of list (page) elements
        Args:
            page (int): the page number
            page_size (int): the page size
        Returns:
            (list): a list of list
        """
        datasets = []
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        data_range = index_range(page, page_size)

        with open('Popular_Baby_Names.csv', mode='r') as dataset:
            data_iterator = csv.reader(dataset)
            data_list = list(data_iterator)
            data_list = data_list[1:]
            try:
                for i in range(*data_range):
                    datasets.append(data_list[i])
            except IndexError as e:
                pass
            finally:
                return datasets
