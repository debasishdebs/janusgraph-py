# Name: Debasish Kanhar

from ..SchemaBuilder import SchemaBuilder
from ..Helpers import Helpers as helpers


class MixedIndexBuilder(SchemaBuilder):
    def __init__(self, connection, query, index_name, element):
        super(MixedIndexBuilder, self).__init__(connection)

        open_management = helpers.open_graph_management()
        self.query = open_management + query

        self.index_name = index_name
        self.element = element

        self.label_constraint = False
        self.keys_added = None
        pass

    def __str__(self):
        return self.index_name

    def addKey(self, property_name, mapping):

        if not self.label_constraint:
            self.keys_added = property_name

            if mapping is not None:
                q = ".addKey(mgmt.getPropertyKey('{}'), Mapping.{}.asParameter())".format(property_name, mapping)
            else:
                q = ".addKey(mgmt.getPropertyKey('{}'))".format(property_name)
                pass

            self.query += q
        else:
            raise AttributeError("addKey() can't be invoked once indexOnly() is already called")

        return self

    def indexOnly(self, label):

        self.label_constraint = True

        q = ".indexOnly(mgmt.get{}Label('{}'))".format(self.element, label)
        self.query += q

        return self

    def make(self, indexing_key="search"):
        if self.keys_added is None:
            raise AttributeError("addKey() needs to be called before make()")

        q = ".buildMixedIndex('{}');".format(indexing_key)
        self.query += q

        self.query += helpers.close_graph_management()

        self.create(self.query)

        return self.index_name
