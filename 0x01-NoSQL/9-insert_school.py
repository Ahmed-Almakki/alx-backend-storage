#!/usr/bin/env python3
""" insert new document"""


def insert_school(mongo_collection, **kwargs):
    """ insert a new document in a collection based on kwargs"""
    new_doc = {key: value for key, value in kwargs.items()}
    result = mongo_collection.insert_one(new_doc)
    return result.inserted_id
