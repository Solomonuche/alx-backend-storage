#!/usr/bin/env python3
"""
Where can I learn Python?
"""


def schools_by_topic(mongo_collection, topic):
    """
     a Python function that changes all topics
     of a school document based on the name
    """
    topic_filter = {
            'topics': {
                '$elemMatch': {
                    '$eq': topic,
                    },
                },
            }
    return [doc for doc in mongo_collection.find(topic_filter)]


if __name__ == "__main__":
    schools_by_topic()
