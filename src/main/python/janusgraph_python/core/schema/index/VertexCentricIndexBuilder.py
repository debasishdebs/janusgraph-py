# Name: Debasish Kanhar

from ..SchemaBuilder import SchemaBuilder
from ..Helpers import Helpers as helpers
from ..Helpers import StringTemplate


class VertexCentricIndex(SchemaBuilder):
    def __init__(self, connection, query, index_name):
        """

        Args:
            connection:
            query (StringTemplate):
            index_name:
        """

        super(VertexCentricIndex, self).__init__(connection)

        query = str(query)

        open_management = helpers.open_graph_management()
        self.query = open_management + query
        self.query = StringTemplate(self.query)

        self.index_name = index_name

        self.edge_added = False
        self.prop_added = False
        self.direction_mentioned = False
        self.order_mentioned = False

        pass

    def __str__(self):
        return self.index_name

    def addEdge(self, label):

        self.edge_added = True

        q = "mgmt.getEdgeLabel('{}')".format(label)

        self.query.format(label=q)

        return self

    def direction(self, dir):

        self.query.format(dir=dir)

        return self

    def order(self, odr):

        self.query.format(odr=odr)

        return self

    def on(self, properties):

        self.prop_added = True

        property_queries = ["mgmt.getPropertyKey('{}')".format(x) for x in properties]

        props = ",".join(property_queries)
        self.query.format(props=props)

        return self

    def make(self):
        if not self.prop_added and not self.edge_added:
            raise AttributeError("addEdge() and on() needs to be called before make()")

        if not self.direction_mentioned:
            self.query.format(dir="BOTH")

        if not self.order_mentioned:
            self.query.format(odr="asc")

        self.query = str(self.query)
        self.query += helpers.close_graph_management()

        self.create(self.query)

        return self
    #
    # def create(self, query):
    #
    #     i = helpers.REPEAT_AWAIT_AFTER_INDEX
    #
    #     while i:
    #         q = helpers.open_graph_management()
    #         query += q
    #
    #         q = helpers.awaitGraphIndexStatus(self.index_name)
    #         query += q
    #
    #         q = helpers.close_graph_management()
    #         query += q
    #
    #         i -= 1
    #
    #     q = helpers.open_graph_management()
    #     query += q
    #
    #     q = helpers.updateIndex(self.index_name)
    #     query += q
    #
    #     q = helpers.close_graph_management()
    #     query += q
    #
    #     query += "graph.tx().commit();\n"
    #     print(query)
    #     super().create(query)
    #
    #     return self.index_name
