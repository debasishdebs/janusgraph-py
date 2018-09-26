# Name: Debasish Kanhar

from ..SchemaBuilder import SchemaBuilder
from ..Helpers import Helpers as helpers


class CompositeIndexBuilder(SchemaBuilder):
    def __init__(self, connection, query, index_name, element):
        """

        Args:
            connection:
            query (str): The already build index query which contains metadata lise Index Name and Graph element
        """

        super(CompositeIndexBuilder, self).__init__(connection)

        open_management = helpers.open_graph_management()
        self.query = open_management + query

        self.index_name = index_name
        self.element = element

        # Sanitation check params
        self.keys_added = None
        self.unique_count = 0
        self.label_constraint = False
        self.unique_constraint = False

        pass

    def __str__(self):
        return self.index_name

    def addKey(self, property_name):

        if not self.label_constraint:
            self.keys_added = property_name

            q = ".addKey(mgmt.getPropertyKey('{}'))".format(property_name)
            self.query += q

        else:
            raise AttributeError("addKey() can't be invoked once indexOnly() is already called")

        return self

    def indexOnly(self, label):

        if not self.unique_constraint:
            self.label_constraint = True

            q = ".indexOnly(mgmt.get{}Label('{}'))".format(self.element, label)
            self.query += q
        else:
            raise AttributeError("indexOnly() can't be invoked once unique() is already called")

        return self

    def unique(self):

        self.unique_constraint = True

        if self.unique_count < 1:
            q = ".unique()"
            self.query += q
        else:
            raise AttributeError("unique() can only be called once. "
                                 "Being called {} times already".format(self.unique_count))

        self.unique_count += 1

        return self

    def make(self):
        if self.keys_added is None:
            raise AttributeError("addKey() needs to be called before make()")

        q = ".buildCompositeIndex();"
        self.query += q

        self.query += helpers.close_graph_management()

        self.create(self.query)

        return self

    def create(self, query):

        i = helpers.REPEAT_AWAIT_AFTER_INDEX

        while i:
            q = helpers.open_graph_management()
            query += q

            q = helpers.awaitGraphIndexStatus(self.index_name)
            query += q

            q = helpers.close_graph_management()
            query += q

            i -= 1

        q = helpers.open_graph_management()
        query += q

        q = helpers.updateIndex(self.index_name)
        query += q

        q = helpers.close_graph_management()
        query += q

        query += "graph.tx().commit();\n"
        print(query)
        super().create(query)

        return self.index_name
