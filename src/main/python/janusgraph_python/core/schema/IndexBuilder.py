# Name: Debasish Kanhar

from .SchemaBuilder import SchemaBuilder
from .index.CompositeIndexBuilder import CompositeIndexBuilder
from .index.MixedIndexBuilder import MixedIndexBuilder


class IndexBuilder(SchemaBuilder):
    def __init__(self, connection):
        super(IndexBuilder, self).__init__(connection)
        self.connection = connection
        pass

    def buildCompositeIndex(self, index_name, element):
        """

        Args:
            index_name (str): Name of Index to be registered
            element (str): Either Vertex or Edge depending which element the property belongs to

        Returns:

        """

        query = "mgmt.buildIndex('{}', {}.class)".format(index_name, element)

        composite_idx_builder = CompositeIndexBuilder(self.connection, query, index_name)

        return composite_idx_builder

    def buildMixedIndex(self, index_name, element):
        """

        Args:
            index_name (str): Name of Index to be registered
            element (str): Either Vertex or Edge depending which element the property belongs to

        Returns:

        """

        query = "mgmt.buildIndex('{}', {}.class)".format(index_name, element)

        mixed_index_builder = MixedIndexBuilder(self.connection, query, index_name)

        return mixed_index_builder

    def buildVertexCentricIndex(self):
        return