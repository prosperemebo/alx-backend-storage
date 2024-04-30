#!/usr/bin/env python3
""" module for the function schools_by_topic """


def schools_by_topic(mongo_collection, topic):
    """ function implementation of schools_by_topic """
    return mongo_collection.find({"topics": topic})
