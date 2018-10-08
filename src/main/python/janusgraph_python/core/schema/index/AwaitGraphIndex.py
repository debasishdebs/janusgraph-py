# Name: Debasish Kanhar

from ..SchemaBuilder import SchemaBuilder
from ..Helpers import Helpers as helpers


class AwaitGraphIndex(SchemaBuilder):
    def __init__(self, connection, index_name):
        super(AwaitGraphIndex, self).__init__(connection)

        self.query = ""

        self.index_name = index_name
        self.__build()
        pass

    def __build(self):
        q = helpers.open_graph_management()
        self.query += q

        q = helpers.awaitGraphIndexStatus(self.index_name)
        self.query += q

        q = helpers.close_graph_management()
        self.query += q

        return self

    def call(self):
        query = self.query

        r = self.create(query)

        return r
