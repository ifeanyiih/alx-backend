#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        The method should return a dictionary with the following
        key-value pairs:
            index: the current start index of the return page.
            next_index: the next index to query with.
            page_size: the current page size
            data: the actual page of the dataset
        Args:
            index (int): the current start index
            page_size (int): the current page size
        Returns:
            (dict): a dictionary with listed key value pairs
        """
        indexed_data = self.indexed_dataset()
        use_index = index
        try:
            assert index in indexed_data.keys()
        except AssertionError as e:
            if index + 1 in indexed_data:
                use_index = index + 1
            else:
                raise e
        next_index = use_index + page_size
        collection = {}
        data = []

        try:
            for i in range(use_index, next_index):
                data.append(indexed_data[i])
        except KeyError as e:
            pass

        collection['index'] = index
        collection['data'] = data
        collection['page_size'] = page_size
        collection['next_index'] = next_index

        return collection
