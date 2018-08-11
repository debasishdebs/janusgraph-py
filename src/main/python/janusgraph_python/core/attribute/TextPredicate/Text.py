# Name: Debasish Kanhar

from gremlin_python.process.traversal import P


class Text(object):
    def __init__(self):
        pass

    @staticmethod
    def textContains(value):
        predicate = P("textContains", value)
        return predicate

    @staticmethod
    def textContainsPrefix(value):
        predicate = P("textContainsFuzzy", value)
        return predicate

    @staticmethod
    def textPrefix(value):
        predicate = P("textPrefix", value)
        return predicate

    @staticmethod
    def textContainsRegex(value):
        predicate = P("textContainsPrefix", value)
        return predicate

    @staticmethod
    def textRegex(value):
        predicate = P("textRegex", value)
        return predicate

    @staticmethod
    def textFuzzy(value):
        predicate = P("textFuzzy", value)
        return predicate

    @staticmethod
    def textContainsFuzzy(value):
        predicate = P("textContainsFuzzy", value)
        return predicate
