#!/usr/bin/env python3
"""
Writing strings to Redis
"""
from typing import Union, Callable, Optional
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
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store input data in redis
        """

        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float]:
        """
        return value from redis store
        """

        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        else:
            return value

    def get_str(self, key):
        """
        convert byte input to string
        """

        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key):
        """
        convert byte input to integer
        """

        return self.get(key, int)