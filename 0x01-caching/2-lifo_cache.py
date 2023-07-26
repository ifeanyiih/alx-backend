#!/usr/bin/env python3
"""
Script contains class LIFOCache that inherits from BaseCaching
and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A caching system"""
    def put(self, key, item):
        """puts item into the cache with key"""
        if key is None or item is None:
            return

        if len(self.cache_data.keys()) == self.MAX_ITEMS:
            if key in self.cache_data:
                del self.cache_data[key]
                self.cache_data[key] = item
                return
            index = self.MAX_ITEMS - 1
            delete_candidate = list(self.cache_data.keys())[index]
            del self.cache_data[delete_candidate]
            self.cache_data[key] = item
            print(f"DISCARD: {delete_candidate}")
        else:
            self.cache_data[key] = item

    def get(self, key):
        """gets item from cache with key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
