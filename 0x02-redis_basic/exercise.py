#!/usr/bin/env python3
""" writting strings to redis"""
import uuid
from typing import Union
import redis


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
