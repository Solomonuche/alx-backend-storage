#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""
from functools import wraps
import requests
from typing import Callable
import redis


def tracker(func: Callable) -> Callable:
    """
    track how many times a particular URL was accessed
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        decorator function
        """

        r = redis.Redis()
        key = f"count:{args}"
        if not r.exists(key):
            r.setex(key, 10, 0)
        r.incr(key, 1)

        return func(*args, **kwargs)
    return wrapper


@tracker
def get_page(url: str) -> str:
    """
    obtain the HTML content of a particular URL and returns it.
    """

    if url:
        response = requests.get(url)
        return response.text
