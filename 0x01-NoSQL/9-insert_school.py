#!/usr/bin/env python3
"""
Module that contains a function that inserts a new document
in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Function that inserts a new document in a collection based on kwargs
    """
    new_documents = mongo_collection.insert_one(kwargs)
    return new_documents.inserted_id
