# Name: Debasish Kanhar
# Emp ID: 05222V


from ..structure.io.GraphsonReader import JanusGraphSONReader
from ..structure.io.GraphsonWriter import JanusGraphSONWriter
from ..driver.JanusGraphManagement import JanusGraphManagement

from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.driver.client import Client
from gremlin_python.structure.graph import Graph


class JanusGraph(object):
    def __init__(self):
        self.remote_connection = None
        self.management_connection = None
        self.URL = None
        self.graph = None
        self.bindings = None
        self.connection_keyword_properties = ["protocol_factory", "transport_factory", "pool_size", "max_workers",
                                              "username", "password", "message_serializer", "graphson_reader",
                                              "graphson_writer"]
        self.args = dict()
        pass

    def connect(self, url="loclahost", port="8182", bindings="g", graph="graph", **kwargs):
        self.URL = "ws://{}:{}/gremlin".format(url, port)
        self.bindings = bindings
        self.graph = graph

        self.args = kwargs

        if not kwargs:

            graphson_reader = JanusGraphSONReader().build()
            graphson_writer = JanusGraphSONWriter().build()

        else:
            kwargs_provided = kwargs.keys()

            if all(k in self.connection_keyword_properties for k in kwargs_provided):
                pass
            else:
                raise AttributeError("Additional parameters except url, port, graph needs to be the available"
                                     "Gremlin client connection parameters. Refer docs")

            if "graphson_reader" in kwargs and "graphson_writer" in kwargs:
                graphson_reader = kwargs["graphson_reader"]
                graphson_writer = kwargs["graphson_writer"]

            else:
                graphson_reader = None
                graphson_writer = None

        args = {k: v for k, v in self.args.items() if k not in ["graphson_reader", "graphson_writer"]}

        self.remote_connection = DriverRemoteConnection(self.URL, self.bindings, graphson_reader=graphson_reader,
                                                        graphson_writer=graphson_writer, **args)

        self.management_connection = Client(self.URL, self.bindings, **args)

        return self

    def traversal(self):
        if self.remote_connection is None:
            raise AttributeError("The Graph is not connected to any Remote Graph. Use connect() first.")

        g = Graph().traversal().withRemote(self.remote_connection)

        return g

    def openManagement(self):
        if self.management_connection is None:
            raise AttributeError("The Graph is not connected to any Remote Graph. Use connect() first.")

        mgmt = JanusGraphManagement(self.management_connection)

        return mgmt

    def close(self):
        self.remote_connection.close()
        self.management_connection.close()
        return True

    def drop(self):
        query = "JanusGraphFactory.drop({});".format(self.graph)
        result_set = self.management_connection.submit(query)
        future_results = result_set.all()
        results = future_results.result()

        self.close()

        return results
