#!/usr/bin/env python3
""" module for the function list_all """


def list_all(mongo_collection):
    """ implementation of list_all functio """
    return mongo_collection.find()
