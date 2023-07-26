#!/usr/bin/env python3
"""Script contains class MRUCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A caching system"""
    def __init__(self):
        """initializes the class"""
        super().__init__()
        self.use_count = {}
        self.incr = -1

    def put(self, key, item):
        """puts item in cache with key"""
        if key is None or item is None:
            return

        if len(self.cache_data.keys()) == self.MAX_ITEMS:
            if key in self.cache_data:
                self.incr += 1
                self.use_count[key] = self.incr
                del self.cache_data[key]
                self.cache_data[key] = item
                return

            use_counts = list(self.use_count.values())
            keys = list(self.use_count.keys())
            maximum = max(use_counts)
            index = use_counts.index(maximum)
            delete_candidate = keys[index]

            del self.cache_data[delete_candidate]
            del self.use_count[delete_candidate]

            self.cache_data[key] = item
            self.incr += 1
            self.use_count[key] = self.incr
            print(f"DISCARD: {delete_candidate}")
        else:
            self.cache_data[key] = item
            self.incr += 1
            self.use_count[key] = self.incr

    def get(self, key):
        """gets item from cache with key"""
        if key is None or key not in self.cache_data:
            return None
        self.incr += 1
        self.use_count[key] = self.incr
        return self.cache_data[key]
