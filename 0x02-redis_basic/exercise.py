#!/usr/bin/env python3
""" writting strings to redis"""
import uuid
from typing import Union, Callable
import redis
import struct


class Cache:
    """ a cach class using reddis"""
    def __init__(self):
        """ initialize the redis client and flushes database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ genrate random key and store"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(key: str, fn: Callable = None) -> Union[None, str, bytes, int, float]:
        """ return the value of the key"""
        if self._redis.exists(key):
            data = self._redis.get(key)
            if fn:
                return fn(data)
            return data
        return None

    def get_str(self, key: str) -> Union[None, str]:
        """ return a string"""
        return self.get(key, lambda x: x.decode("utf-8") if x else None)

    def get_int(self, key: str) -> Union[None, int]:
        """return a int"""
        return self.get(key, lambda x: int.from_bytes(x, "big") if x else None)

