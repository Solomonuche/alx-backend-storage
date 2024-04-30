#!/usr/bin/env python3
"""
List all MongoDb documents in Python
"""


def list_all(mongo_collection):
    """
    a Python function that lists all documents in a collection
    """

    if mongo_collection.count_documents(filter={}):
        return mongo_collection.find()
    else:
        return []


if __name__ == "__main__":
    list_all()
