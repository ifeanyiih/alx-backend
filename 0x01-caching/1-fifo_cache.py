#!/usr/bin/env python3
"""
Script contains a class FIFOCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A caching system"""
    def __init__(self):
        """initializes the class"""
        super().__init__()
        self.oldest = 0

    def put(self, key, item):
        """adds item to the cache"""
        if key is None or item is None:
            return
        if len(list(self.cache_data.keys())) == 0:
            self.cache_data[key] = item
        elif len(list(self.cache_data.keys())) == self.MAX_ITEMS:
            if key in self.cache_data:
                del self.cache_data[key]
                self.cache_data[key] = item
                return
            delete_candidate = list(self.cache_data.keys())[self.oldest]
            del self.cache_data[delete_candidate]
            print(f"DISCARD: {delete_candidate}")
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item

    def get(self, key):
        """return value from cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
