#!/usr/bin/env python3
""" LRU Cache module """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Defines an LRUCache class """

    usage = {}

    def __init__(self):
        """ Constructor """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            pass
        else:
            if key in self.cache_data:
                del self.cache_data[key]
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    least_freq = min(list(self.usage.values()))
                    min_keys = [key for key, value in list
                                (self.usage.items()) if value == least_freq]
                    for mykey in self.cache_data.keys():
                        if mykey in min_keys:
                            del self.cache_data[mykey]
                            del self.usage[mykey]
                            print(f"DISCARD: {mykey}")
                            break
                    self.cache_data[key] = item
                else:
                    self.cache_data[key] = item
        if key in self.usage:
            self.usage[key] += 1
        else:
            self.usage[key] = 0

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        else:
            if key in self.usage:
                self.usage[key] += 1
            else:
                self.usage[key] = 0
            return self.cache_data[key]
