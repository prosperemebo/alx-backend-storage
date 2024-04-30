#!/usr/bin/env python3
""" module for the function insert_school """


def insert_school(mongo_collection, **kwargs):
    """ function implementation of insert_school """
    return mongo_collection.insert_one(kwargs).inserted_id
