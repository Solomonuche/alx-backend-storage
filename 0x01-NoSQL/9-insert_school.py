#!/usr/bin/env python3
"""
Insert a documentn
"""


def insert_school(mongo_collection, **kwargs):
    """
    a Python function that inserts a new document
    in a collection based on kwargs
    """

    obj = {}

    for key, value in kwargs.items():
        obj[key] = value

    result = mongo_collection.insert_one(obj)
    return result.inserted_id


if __name__ == "__main__":
    insert_school()
