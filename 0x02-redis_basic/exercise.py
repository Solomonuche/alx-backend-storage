#!/usr/bin/env python3
"""
Writing strings to Redis
"""
from uuid import uuid4
import redis


class Cache():
    """
    Cache class
    """

    def __init__(self):
        """
        constructor class
        """
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: any) -> str:
        """
        store input data in redis
        """

        key = str(uuid4())
        self._redis.set(key, data)
        return key
