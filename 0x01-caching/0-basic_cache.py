#!/usr/bin/env python3
"""Script contains class BasicCache that inherits
from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache, a caching system"""
    def put(self, key, item):
        """adds an item to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """returns the value in cache linked to key"""
        if key is None or key not in self.cache_data:
            return
        return self.cache_data.get(key)
