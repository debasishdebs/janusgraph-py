# Name: Debasish Kanhar

from ..SchemaBuilder import SchemaBuilder
from ..Helpers import Helpers as helpers


class UpdateIndex(SchemaBuilder):
    def __init__(self, connection, index_name):
        super(UpdateIndex, self).__init__(connection)

        self.query = ""

        self.index_name = index_name
        self.__build()
        pass

    def __build(self):
        q = helpers.open_graph_management()
        self.query += q

        q = helpers.updateIndex(self.index_name)
        self.query += q

        q = helpers.close_graph_management()
        self.query += q

        return self

    def get(self):
        query = self.query

        r = self.create(query)

        return r
