# Name: Debasish Kanhar

from .SchemaBuilder import SchemaBuilder
from .index.CompositeIndexBuilder import CompositeIndexBuilder
from .index.MixedIndexBuilder import MixedIndexBuilder
from .index.VertexCentricIndexBuilder import VertexCentricIndex
from .Helpers import StringTemplate


class IndexBuilder(SchemaBuilder):
    def __init__(self, connection):
        super(IndexBuilder, self).__init__(connection)
        self.connection = connection

        self.query = "graph.tx().rollback();"
        pass

    def buildCompositeIndex(self, index_name, element):
        """

        Args:
            index_name (str): Name of Index to be registered
            element (str): Either Vertex or Edge depending which element the property belongs to

        Returns:

        """

        query = "mgmt.buildIndex('{}', {}.class)".format(index_name, element)

        self.query += query

        composite_idx_builder = CompositeIndexBuilder(self.connection, self.query, index_name, element)

        return composite_idx_builder

    def buildMixedIndex(self, index_name, element):
        """

        Args:
            index_name (str): Name of Index to be registered
            element (str): Either Vertex or Edge depending which element the property belongs to

        Returns:

        """

        query = "mgmt.buildIndex('{}', {}.class)".format(index_name, element)

        self.query += query

        mixed_index_builder = MixedIndexBuilder(self.connection, self.query, index_name, element)

        return mixed_index_builder

    def buildVertexCentricIndex(self, index_name):
        q = StringTemplate("mgmt.buildEdgeIndex({label}, '{index_name}', Direction.{dir}, Order.{odr}, {props});\n")
        q.format(index_name=index_name)

        query = StringTemplate(self.query + str(q))

        vertex_centric_index_builder = VertexCentricIndex(self.connection, query, index_name)

        return vertex_centric_index_builder
