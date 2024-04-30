#!/usr/bin/env python3
""" module for the function update_topics """


def update_topics(mongo_collection, name, topics):
    """ function implementation of update_topics """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
