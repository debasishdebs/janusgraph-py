# Name: Debasish Kanhar
# Emp ID: 05222V

from .SchemaBuilder import SchemaBuilder
from .Helpers import Helpers as helpers


class ManagementExecutors(SchemaBuilder):
    def __init__(self, connection):
        super(ManagementExecutors, self).__init__(connection)

        self.query += helpers.open_graph_management()

        pass

    def getOpenInstances(self):
        q = "mgmt.getOpenInstances();"

        self.query += q

        result = self.create(self.query)

        self.query = helpers.open_graph_management()

        return result

    def forceCloseInstance(self, instance_id):
        q = "mgmt.forceCloseInstance({});".format(instance_id)

        self.query += q

        self.query += helpers.close_graph_management()

        self.create(self.query)

        self.query = helpers.open_graph_management()

        return None

    def commit(self):
        q = "mgmt.commit();"

        self.query += q

        self.create(self.query)

        self.query = helpers.open_graph_management()

        return None
