# Name: Debasish Kanhar

import string


class Helpers(object):
    REPEAT_AWAIT_AFTER_INDEX = 3

    @staticmethod
    def open_graph_management():
        query = "mgmt = graph.openManagement();\n"
        return query

    @staticmethod
    def close_graph_management():
        query = "mgmt.commit();\n"
        return query

    @staticmethod
    def awaitGraphIndexStatus(index_name):
        q = "mgmt.awaitGraphIndexStatus(graph, '{}').status(SchemaStatus.REGISTERED).call();\n".format(index_name)
        return q

    @staticmethod
    def updateIndex(index_name):
        q = "mgmt.updateIndex(mgmt.getGraphIndex('{}'), SchemaAction.REINDEX).get();\n".format(index_name)
        return q


class StringTemplate(object):
    class FormatDict(dict):
        def __missing__(self, key):
            return "{" + key + "}"

    def __init__(self, template):
        self.substituted_str = template
        self.formatter = string.Formatter()

    def __repr__(self):
        return self.substituted_str

    def format(self, *args, **kwargs):
        mapping = StringTemplate.FormatDict(*args, **kwargs)
        self.substituted_str = self.formatter.vformat(self.substituted_str, (), mapping)
