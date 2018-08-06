# Name: Debasish Kanhar
# Emp ID: 05222V

from gremlin_python.process.traversal import P


class Text(object):
    def __init__(self):
        pass

    def textContains(self, value):
        predicate = P("textContains", value)
        return predicate

    def textContainsPrefix(self, value):
        predicate = P("textContainsFuzzy", value)
        return predicate

    def textPrefix(self, value):
        predicate = P("textPrefix", value)
        return predicate

    def textContainsRegex(self, value):
        predicate = P("textContainsPrefix", value)
        return predicate

    def textRegex(self, value):
        predicate = P("textRegex", value)
        return predicate

    def textFuzzy(self, value):
        predicate = P("textFuzzy", value)
        return predicate

    def textContainsFuzzy(self, value):
        predicate = P("textContainsFuzzy", value)
        return predicate
