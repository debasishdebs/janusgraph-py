# Name: Debasish Kanhar
# Emp ID: 05222V

from gremlin_python.process.traversal import *


class Text(object):
    def __init__(self):
        pass

    def textContains(self, query):
        predicate = P("textContains", query)
        return predicate

    def textFuzzy(self, query):
        predicate = P("textFuzzy", query)
        return predicate