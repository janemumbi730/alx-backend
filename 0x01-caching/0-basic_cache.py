#!/usr/bin/env python3
"""
Module 0-basic_cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class inherits from BaseCaching"""

    def put(self, key, item):
        """Adds an item to the cache dictionary"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache dict"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
