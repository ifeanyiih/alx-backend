#!/usr/bin/env python3
"""Script contains class LFUCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A caching system"""
    def __init__(self):
        """initializes the class"""
        super().__init__()
        self.use_count = {}

    def put(self, key, item):
        """puts item in cache with key"""
        if key is None or item is None:
            return

        if len(self.cache_data.keys()) == self.MAX_ITEMS:
            if key in self.cache_data:
                self.use_count[key] += 1
                del self.cache_data[key]
                self.cache_data[key] = item
                return

            use_counts = list(self.use_count.values())
            keys = list(self.use_count.keys())
            minimum = min(use_counts)
            index = use_counts.index(minimum)
            delete_candidate = keys[index]

            del self.cache_data[delete_candidate]
            del self.use_count[delete_candidate]

            self.cache_data[key] = item
            self.use_count[key] = 0
            print(f"DISCARD: {delete_candidate}")
        else:
            self.cache_data[key] = item
            self.use_count[key] = 0

    def get(self, key):
        """gets item from cache with key"""
        if key is None or key not in self.cache_data:
            return None
        self.use_count[key] += 1
        return self.cache_data[key]
