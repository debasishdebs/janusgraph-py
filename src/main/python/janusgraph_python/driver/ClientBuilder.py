# Name: Debasish Kanhar

from ..structure.io.GraphsonReader import JanusGraphSONReader
from ..structure.io.GraphsonWriter import JanusGraphSONWriter

from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.structure.graph import Graph


class JanusGraphClient(object):
    REMOTE_CONNECTION = None

    def __init__(self, version=3.0):
        self.graphsonVersion = version
        pass

    def build(self, url="loclahost", port="8182", graph="g"):

        URL = "ws://{}:{}/gremlin".format(url, port)

        graphson_reader = JanusGraphSONReader().build()
        graphson_writer = JanusGraphSONWriter().build()

        self.REMOTE_CONNECTION = DriverRemoteConnection(URL, graph, graphson_reader=graphson_reader,
                                                        graphson_writer=graphson_writer)

        return self

    def get_traversal(self):
        graph = Graph()
        g = graph.traversal().withRemote(self.REMOTE_CONNECTION)
        return g
