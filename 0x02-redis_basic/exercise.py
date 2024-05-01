#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import functools
from typing import Union, Callable, Optional
from uuid import uuid4
import redis


def count_calls(method: Callable) -> Callable:
    """
    cache.store decorator
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function"""
        key = method.__qualname__
        if not self._redis.exists(key):
            self._redis.set(key, 0)
        self._redis.incr(key, 1)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    decorator to store the history of inputs and outputs
    for a particular function.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function"""
        input_list = f"{method.__qualname__}:inputs"
        output_list = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_list, str(args))

        value = method(self, *args, **kwargs)
        self._redis.rpush(output_list, value)
        return value
    return wrapper


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

    @count_calls
    @call_history
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
