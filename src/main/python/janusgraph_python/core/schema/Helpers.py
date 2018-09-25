# Name: Debasish Kanhar
# Emp ID: 05222V


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
