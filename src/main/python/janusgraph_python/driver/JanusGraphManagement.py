# Name: Debasish Kanhar
# Emp ID: 05222V

from ..core.schema.PropertyKeyBuilder import PropertyKeyBuilder
from ..core.schema.VertexLabelBuilder import VertexLabelBuilder
from ..core.schema.EdgeLabelBuilder import EdgeLabelBuilder
from ..core.schema.IndexBuilder import IndexBuilder
from ..core.schema.index.AwaitGraphIndex import AwaitGraphIndex
from ..core.schema.index.UpdateIndex import UpdateIndex
from ..core.schema.ManagementExecutors import ManagementExecutors

from gremlin_python.driver.client import Client


class JanusGraphManagement(object):
    def __init__(self, connection):
        """

        Args:
            connection (Client):
        """

        self.connection = connection
        self.executor = ManagementExecutors(connection)
        pass

    def propertyKeyBuilder(self):
        builder = PropertyKeyBuilder(self.connection)
        return builder

    def vertexLabelBuilder(self):
        builder = VertexLabelBuilder(self.connection)
        return builder

    def edgeLabelBuilder(self):
        builder = EdgeLabelBuilder(self.connection)
        return builder

    def buildVertexCentricIndex(self, index_name):
        builder = IndexBuilder(self.connection).buildVertexCentricIndex(index_name)
        return builder

    def buildCompositeIndex(self, index_name, element):
        builder = IndexBuilder(self.connection).buildCompositeIndex(index_name, element)
        return builder

    def buildMixedIndex(self, index_name, element):
        builder = IndexBuilder(self.connection).buildMixedIndex(index_name, element)
        return builder

    def awaitGraphIndexStatus(self, index_name):
        builder = AwaitGraphIndex(self.connection, index_name)
        return builder

    def updateIndex(self, index_name):
        builder = UpdateIndex(self.connection, index_name)
        return builder

    def getOpenInstances(self):
        instances = self.executor.getOpenInstances()
        return instances

    def forceCloseInstance(self, instance_id):
        self.executor.forceCloseInstance(instance_id)

    def commit(self):
        self.executor.commit()
