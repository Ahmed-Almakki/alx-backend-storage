#!/usr/bin/env python3
""" change all topics"""


def update_topics(mongo_collection, name, topics):
    """find topics and change them"""
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
